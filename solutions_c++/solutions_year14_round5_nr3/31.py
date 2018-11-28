#define _CRT_SECURE_NO_DEPRECATE
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
#pragma comment(linker, "/STACK:67108864")
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
const int _maxNumberOfTests = 101;
struct Answer {
	int numberOfTest;
	string ans;
	inline void output() {
		printf("Case #%d: %s\n", numberOfTest + 1, ans.c_str());
	}
};

struct Solver {
	int _numberOfThread;
	Answer *pAns;
	int n, k;
	char str[102];
	pair<char, int> mas[1002];
	map<int, int> nm;
	bool dp[2][1 << 15];
	inline void readInput() {
		scanf("%d", &n);
		rept(i, n) {
			scanf("%s%d", str, &mas[i].y);
			mas[i].x = str[0];
		}
	}

	inline int num(int a) {
		if (nm.count(a)) return nm[a]; else
			return nm[a] = k++;
	}

	int check(int m) {
		C(dp);
		int now = 1, nx = 0;
		rept(mask, 1 << m) dp[nx][mask] = 1;
		rept(i, n) {
			swap(now, nx);
			C(dp[nx]);
			rept(mask, 1 << m) {
				if (!dp[now][mask]) continue;
				if (mas[i].x == 'E') {
					if (mas[i].y > 0) {
						int v = mas[i].y - 1;
						if (mask & 1 << v) continue;
						dp[nx][mask | 1 << v] = 1;
					}
					else {
						rept(j, m) {
							if (mask & 1 << j) continue;
							dp[nx][mask | 1 << j] = 1;
						}
					}
				}
				else {
					if (mas[i].y > 0) {
						int v = mas[i].y - 1;
						if (~mask & 1 << v) continue;
						dp[nx][mask ^ 1 << v] = 1;
					}
					else {
						rept(j, m) {
							if (~mask & 1 << j) continue;
							dp[nx][mask ^ 1 << j] = 1;
						}
					}
				}
			}
		}
		int ans = INF;
		rept(mask, 1 << m) {
			if (!dp[nx][mask]) continue;
			int cnt = 0;
			rept(i, m) if (mask & 1 << i) ++cnt;
			ans = min(ans, cnt);
		}
		return ans;
	}
	void run() {
		// put an answer into pAns
		nm.clear();
		k = 1;
		rept(i, n) {
			if (mas[i].y != 0) mas[i].y = num(mas[i].y);
		}
		int ans = INF;
		FOR(i, k - 1, n) {
			int cur = check(i);
			ans = min(ans, cur);
		}
		ostringstream oss;
		if (ans >= INF) oss << "CRIME TIME"; else
			oss << ans;
		pAns->ans = oss.str();
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
void solveParallel(int numberOfTests, int maxThreads = 4) {
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
		cerr << "Test #" << currentTest + 1 << " was taken by thread #" << threadNumber << " at " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
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
	cerr << 1.0 * clock() / CLOCKS_PER_SEC << endl;
}

inline void solveSequential(int kolt) {
	for (int hod = 0; hod < kolt; ++hod) {
		cerr << hod << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
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
		cerr << hod << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
		HOD = hod;
		answers[0].numberOfTest = 0;
		solvers[0]._numberOfThread = 1;
		solvers[0].pAns = &answers[0];
		solvers[0].run();
	}
}
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
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
