#include      <algorithm>
#include      <sstream>
#include      <cmath>
#include      <cstdarg>
#include      <cstdio>
#include      <cstdlib>
#include      <iomanip>
#include      <iostream>
#include      <iterator>
#include      <limits>
#include      <list>
#include      <map>
#include      <set>
#include      <vector>
#define endl '\n'
#define each(c, e) for (typeof(c.begin()) e = c.begin(); e != c.end(); ++e)
typedef long long ll;
using namespace std;

template<typename T1, typename T2> ostream& operator<<(ostream &o, const pair<T1, T2> &p) {return o << '(' << p.first << ", " << p.second << ')';}
template<typename I> ostream& print(ostream &o, I s, I e, int w = 5, int prec = 2, const string &sep = ", ", const string &lhs = "", const string &rhs = "") {
	o << lhs;
	if (s != e) o << setw(w) << setprecision(prec) << *(s++);
	for (; s != e; ++s) o << sep << setw(w) << setprecision(prec) << *s;
	return o << rhs;
}
template<typename T, template<typename E, typename A=std::allocator<E> > class C>
ostream& operator<<(ostream &o, const C<T>& c) {return print(o, c.begin(), c.end(), 0, 2, ", ", "[", "]");}
template<typename T, template<typename E, typename Compare = less<E>, typename Alloc = allocator<E> > class C>
ostream& operator<<(ostream &o, const C<T>& c) {return print(o, c.begin(), c.end(), 0, 2, ", ", "{", "}");}
template<typename K, typename T, template<typename E1, typename E2, typename Compare = std::less<E1>, class Allocator = std::allocator<std::pair<const E1, E2> > > class C>
ostream& operator<<(ostream &o, const C<K, T>& c) {return print(o, c.begin(), c.end(), 0, 2, ", ", "{", "}");}

struct State {
	vector<int> g_vectKeys;
	vector< pair< int, vector<int> > > g_vectWillGetKeys;
	vector<bool> g_vectVisited;
	vector<int> g_vectPath;
	set< pair< vector<int>, vector<bool> > > g_memo;
	int K, N, T, f;
	bool bOk;
};

const int THREADS = 20;
const int SLEEP = 1;
pthread_mutex_t printLock;

#include      <pthread.h>
#include      <unistd.h>
#include      <queue>
template<typename T> class JobQueue {
	private:
		queue<T> m_queueJobs;
		pthread_mutex_t m_lock;
	public:
		JobQueue() {
			pthread_mutex_init(&m_lock, NULL);
		}
		~JobQueue() {
			pthread_mutex_destroy(&m_lock);
		}

		void addJob(const T &job) {
			pthread_mutex_lock(&m_lock);
			m_queueJobs.push(job);
			pthread_mutex_unlock(&m_lock);
		}

		bool getJob(T &job, int nWaitInterval = -1) {
			bool bGot = false;
			while (true) {
				pthread_mutex_lock(&m_lock);
				if (!m_queueJobs.empty()) {
					job = m_queueJobs.front();
					bGot = true;
					m_queueJobs.pop();
				}
				pthread_mutex_unlock(&m_lock);

				if (bGot) return true;
				else if (nWaitInterval != -1) sleep(nWaitInterval);
				else return false;
			}
		}

		int jobCount() {
			int cnt = 0;
			pthread_mutex_lock(&m_lock);
			cnt = m_queueJobs.size();
			pthread_mutex_unlock(&m_lock);
			return cnt;
		}

		void getAll(queue<T> &queueJobs) {
			pthread_mutex_lock(&m_lock);
			queueJobs = m_queueJobs;
			pthread_mutex_unlock(&m_lock);
		}
};
JobQueue< pair<int, string> > jobsResult;
JobQueue< State > jobsQueue;

const int MAX_K_TYPES = 205;
const int MAX_CHESS_TYPES = MAX_K_TYPES;

bool dfs(int chess, State &st) {
	bool bTestOne = false;

	if (st.g_vectKeys[st.g_vectWillGetKeys[chess].first]) {
		st.g_vectKeys[st.g_vectWillGetKeys[chess].first] -= 1;
		each(st.g_vectWillGetKeys[chess].second, it) st.g_vectKeys[*it] += 1;
		st.g_vectVisited[chess] = true;
		st.g_vectPath.push_back(chess);

		pair< vector<int>, vector<bool> > pt(st.g_vectKeys, st.g_vectVisited);
		if (!st.g_memo.count(pt)) {
			st.g_memo.insert(pt);

			for (int i = 1; i <= st.N; i += 1) {
				if (st.g_vectVisited[i]) continue;
				bTestOne = true;
				if (dfs(i, st)) return true;
			}
		} else bTestOne = true;

		st.g_vectVisited[chess] = false;
		each(st.g_vectWillGetKeys[chess].second, it) st.g_vectKeys[*it] -= 1;
		st.g_vectKeys[st.g_vectWillGetKeys[chess].first] += 1;
		if (!bTestOne) return true;
		st.g_vectPath.pop_back();
	}

	return false;
}

State readState(int t) {
	State st;

	st.g_vectKeys.resize(MAX_K_TYPES);
	st.g_vectVisited.resize(MAX_CHESS_TYPES);
	st.g_vectWillGetKeys.resize(MAX_CHESS_TYPES);

	each(st.g_vectKeys, it) *it = 0;
	each(st.g_vectVisited, it) *it = false;
	each(st.g_vectWillGetKeys, it) it->second.clear();
	st.g_vectPath.clear();
	st.g_memo.clear();

	cin >> st.K >> st.N;
	int nTmp1, nTmp2;
	st.g_vectWillGetKeys[0].first = 0;
	for (int i = 0; i < st.K; i += 1) { cin >> nTmp1; st.g_vectWillGetKeys[0].second.push_back(nTmp1); }
	for (int i = 1; i <= st.N; i += 1) {
		cin >> st.g_vectWillGetKeys[i].first >> nTmp1;
		for (int j = 0; j < nTmp1; j += 1) { cin >> nTmp2; st.g_vectWillGetKeys[i].second.push_back(nTmp2); }
	}
	st.T = t;
	return st;
}

void* solve(void*) {
	while (jobsQueue.jobCount()) {
		State st;
		jobsQueue.getJob(st, SLEEP);
		st.g_vectKeys[0] = 1;

		if (dfs(0, st)) {
			stringstream ss;
			for (size_t i = 1; i < st.g_vectPath.size(); i += 1) {
				if (i != 1) ss << ' '; ss << st.g_vectPath[i];
			}
			jobsResult.addJob(make_pair(st.T, ss.str()));
		} else {
			jobsResult.addJob(make_pair(st.T, "IMPOSSIBLE"));
		}

		// pthread_mutex_lock(&printLock);
		// cerr << "Solved: " << st.T << " Left: " << jobsQueue.jobCount() << endl;
		// pthread_mutex_unlock(&printLock);

		st.g_memo.clear();
	}

	return NULL;
}

int main(int argc, char **argv) {
	pthread_mutex_init(&printLock, NULL);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t += 1) {
		jobsQueue.addJob(readState(t));
	}

	for (int t = 1; t <= THREADS; t += 1) {
		pthread_t thread;
		pthread_create(&thread, NULL, solve, NULL);
	}

	while (jobsResult.jobCount() != T) {
		sleep(SLEEP);
	}

	{
		queue< pair<int, string> > queueResult;
		jobsResult.getAll(queueResult);
		vector< pair<int, string> > vectResults;
		while (!queueResult.empty()) { vectResults.push_back(queueResult.front()); queueResult.pop(); }
		sort(vectResults.begin(), vectResults.end());
		each(vectResults, it) cout << "Case #" << it->first << ": " << it->second << endl;
	}

	pthread_mutex_destroy(&printLock);
	return 0;
}
