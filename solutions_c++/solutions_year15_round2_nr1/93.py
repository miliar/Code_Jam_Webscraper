#ifdef _MSC_VER
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:66777216")
#else
#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")
#endif
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <functional>

#include <thread>
#include <mutex>
#include <condition_variable>
#include <atomic>
#include <chrono>
using namespace std;
#define pb push_back
#define ppb pop_back
#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define pii pair<int,int>
#define pdd pair<double,double>
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).size())
#define C(a) memset((a),0,sizeof(a))
#define VI vector <int>
#define ll long long

//int numThreads = 0;
int HOD;
const int _maxNumberOfThreads = 4;
const int _maxNumberOfTests = 1001;
struct Answer {
	int numberOfTest;
	int ans;
	inline void output() {
		printf("Case #%d: %d\n", numberOfTest + 1, ans);
	}
};

const int di[] = { 0, 1, 0, -1 };
const int dj[] = { 1, 0, -1, 0 };
struct Solver {
	int _numberOfThread;
	Answer *pAns;
	int r, c, n;
	inline void readInput() {
		scanf("%d%d%d", &r, &c, &n);
	}

	void run() {
		int beg = n;
		if (!n) {
			pAns->ans = 0;
			return;
		}
		int cur = 0;
		rept(i, r) {
			rept(j, c) {
				if ((i + j) % 2 == 0) {
					++cur;
				}
			}
		}
		if (cur >= n) {
			pAns->ans = 0;
			return;
		}
		n -= cur;
		VI tmp;
		rept(i, r) {
			rept(j, c) {
				if ((i + j) % 2 == 0) continue;
				int deg = 0;
				rept(z, 4) {
					int ni = i + di[z];
					int nj = j + dj[z];
					if (ni < 0 || ni >= r || nj < 0 || nj >= c) continue;
					++deg;
				}
				tmp.pb(deg);
			}
		}
		SORT(tmp);
		int ans = 0;
		rept(i, n) {
			ans += tmp[i];
		}
		pAns->ans = ans;

		vector<vector<char>> mas(r, vector<char>(c, 1));
		vector<VI> deg(r, VI(c, 0));
		cur = 0;
		set<pair<int, pii>> q;
		rept(i, r) {
			rept(j, c) {
				int dg = 0;
				rept(z, 4) {
					int ni = i + di[z];
					int nj = j + dj[z];
					if (ni < 0 || ni >= r || nj < 0 || nj >= c) continue;
					++dg;
				}
				deg[i][j] = dg;
				q.insert(mp(deg[i][j], mp(i, j)));
				cur += dg;
			}
		}
		cur /= 2;
		while (q.size() > beg) {
			auto t = *q.rbegin();
			q.erase(--q.end());
			cur -= t.x;
			int ci = t.y.x;
			int cj = t.y.y;
			mas[ci][cj] = 0;
			rept(i, 4) {
				int ni = ci + di[i];
				int nj = cj + dj[i];
				if (ni < 0 || ni >= r || nj < 0 || nj >= c) continue;
				if (!mas[ni][nj]) continue;
				q.erase(q.find(mp(deg[ni][nj], mp(ni, nj))));
				--deg[ni][nj];
				q.insert(mp(deg[ni][nj], mp(ni, nj)));
			}
		}
		pAns->ans = min(pAns->ans, cur);
	}
};

Solver solvers[_maxNumberOfThreads];
Answer answers[_maxNumberOfTests];

thread threadPool[_maxNumberOfThreads];
atomic<bool> threadsUsed[_maxNumberOfThreads];
atomic<int> busyThreads;
mutex Mutex;
condition_variable CV;

struct CheckIfThereIsAFreeThread {
	const int totalNumberOfThreads;
	CheckIfThereIsAFreeThread() : totalNumberOfThreads(0) {}
	CheckIfThereIsAFreeThread(int numberOfThreads) : totalNumberOfThreads(numberOfThreads) {}
	inline bool operator ()() const {
		return busyThreads.load() < totalNumberOfThreads;
	}
};
void solverWrapper(Solver *solver, int id) {
	solver->run();
	threadsUsed[id].store(false);
	--busyThreads;
	CV.notify_all();
}
chrono::high_resolution_clock::time_point _startTime = chrono::high_resolution_clock::now();
inline double _getTime() {
	auto cur = chrono::high_resolution_clock::now();
	return 1e-6 * chrono::duration_cast<chrono::microseconds>(cur - _startTime).count();
}
void solveParallel(int numberOfTests, int maxThreads = _maxNumberOfThreads) {
	for (int i = 0; i < maxThreads; ++i) {
		threadsUsed[i].store(false);
	}
	busyThreads.store(0);
	for (int currentTest = 0; currentTest < numberOfTests; ++currentTest) {
		unique_lock<mutex> lock(Mutex);
		CV.wait(lock, CheckIfThereIsAFreeThread(maxThreads));
		int threadNumber = -1;
		for (int i = 0; i < maxThreads; ++i) {
			if (!threadsUsed[i].load()) {
				threadNumber = i;
				break;
			}
		}
		if (threadPool[threadNumber].joinable()) {
			threadPool[threadNumber].join();
		}
		threadsUsed[threadNumber].store(true);
		++busyThreads;
		cerr << "Test #" << currentTest + 1 << " was taken by thread #" << threadNumber << " at " << _getTime() << endl;
		solvers[threadNumber]._numberOfThread = threadNumber;
		solvers[threadNumber].readInput();
		answers[currentTest].numberOfTest = currentTest;
		solvers[threadNumber].pAns = &answers[currentTest];
		threadPool[threadNumber] = thread(solverWrapper, &solvers[threadNumber], threadNumber);
	}
	for (int i = 0; i < maxThreads; ++i) {
		if (threadPool[i].joinable()) {
			threadPool[i].join();
		}
	}

	for (int i = 0; i < numberOfTests; ++i) answers[i].output();
	cerr << _getTime() << endl;
}
inline void solveSequential(int kolt) {
	for (int hod = 0; hod < kolt; ++hod) {
		cerr << hod << " " << _getTime() << endl;
		solvers[0]._numberOfThread = 1;
		solvers[0].readInput();
		answers[hod].numberOfTest = hod;
		solvers[0].pAns = &answers[hod];
		solvers[0].run();
	}

	for (int i = 0; i < kolt; ++i) answers[i].output();
}
inline void stressTest() {
	for (int hod = 0; hod < INF; ++hod) {
		cerr << hod << " " << _getTime() << endl;
		HOD = hod;
		answers[0].numberOfTest = 0;
		solvers[0]._numberOfThread = 1;
		solvers[0].pAns = &answers[0];
		solvers[0].run();
	}
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	char tmp[333];
	int kolt = 0;
	gets(tmp);
	sscanf(tmp, "%d", &kolt);
	if (kolt > _maxNumberOfTests) {
		cerr << "_maxNumberOfTests = " << _maxNumberOfTests << ", but kolt = " << kolt << endl;
		int t = 0;
		while (1) ++t;
	}
	solveParallel(kolt);
	//solveSequential(kolt);
	//stressTest();
}

