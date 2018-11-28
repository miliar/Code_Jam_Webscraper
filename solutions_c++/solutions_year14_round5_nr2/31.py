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
const int _maxNumberOfTests = 201;
struct Answer {
	int numberOfTest;
	int ans;
	inline void output() {
		printf("Case #%d: %d\n", numberOfTest + 1, ans);
	}
};

struct Solver {
	int _numberOfThread;
	Answer *pAns;
	int p, q, n;
	pii mas[101];
	int dp[102][2002][2];
	inline void readInput() {
		scanf("%d%d%d", &p, &q, &n);
		rept(i, n) {
			scanf("%d%d", &mas[i].x, &mas[i].y);
		}
	}

	inline void upd(int &a, int b) {
		if (a < b) a = b;
	}
	void run() {
		// put an answer into pAns
		memset(dp, -1, sizeof(dp));
		dp[0][0][0] = 0;
		rept(i, n) {
			rept(j, 1011) {
				rept(move, 2) {
					if (dp[i][j][move] < 0) continue;
					int needp = (mas[i].x + p - 1) / p;
					if (needp <= j) {
						upd(dp[i + 1][j - needp][move], dp[i][j][move] + mas[i].y);
					}
					int H = mas[i].x;
					if (move) H = max(0, H - q);
					if (!H) {
						upd(dp[i + 1][j][0], dp[i][j][move]);
						continue;
					}
					// give up
					int need = (H + q - 1) / q;
					upd(dp[i + 1][j + need][0], dp[i][j][move]);
					// attack
					needp = (H + p - 1) / p;
					rept(uf, j + 1) {
						if (uf > needp) break;
						int rem = max(0, H - p * uf);
						if (!rem) {
							upd(dp[i + 1][j - uf][0], dp[i][j][move] + mas[i].y);
						}
						else {
							rept(skip, 11) {
								int hp = rem;
								rept(round, INF) {
									if (round >= skip) hp = max(0, hp - p);
									if (!hp) {
										upd(dp[i + 1][j - uf + skip][1], dp[i][j][move] + mas[i].y);
										break;
									}
									hp = max(0, hp - q);
									if (!hp) break;
								}
							}
						}
					}
				}
			}
		}

		int ans = 0;
		rept(i, 2000) ans = max(ans, max(dp[n][i][0], dp[n][i][1]));
		pAns->ans = ans;
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
	freopen("B-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
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
