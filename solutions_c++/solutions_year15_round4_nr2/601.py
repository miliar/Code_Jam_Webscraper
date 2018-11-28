#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <thread>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

// compilation:
// g++ -std=c++11 -pthread -O2 file.cpp
// clang++ -std=c++11 -stdlib=libc++ file.cpp
//============================================================

bool PRINT_TESTS_PROGRESS = true;
const int THREADS = 8;

const int MAX_TESTS = 100;

struct TestCase {
  // input/output data goes here
  int N;
  double V, X;
  double R[110];
  double C[110];
  double res;

  void read() {
    scanf("%d", &N);
    scanf("%lf%lf", &V, &X);
    for (int i = 0; i < N; ++i)
      scanf("%lf%lf", &R[i], &C[i]);
  }

  void solve() {
    Double eps = 1e-9;
    // solution goes here
    int i;
    int KL = 0, KG = 0, KE = 0;
    Double VL, VG, VE;
    Double UL, UG;
    VL = VG = VE = 0;
    UL = UG = 0;
    for (int i = 0; i < N; ++i) {
      if (C[i] == X) {
	++KE;
	VE += R[i];
      } else if (C[i] < X) {
	++KL;
	VL += R[i];
	UL += R[i]*C[i];
      } else {
	++KG;
	VG += R[i];
	UG += R[i]*C[i];
      }
    }

    if ((KE == 0 && KL == 0) || (KE == 0 && KG == 0)) {
      res = -1;
      return;
    }

    Double CL, CG;
    CL = KL > 0 ? UL / VL : 0;
    CG = KG > 0 ? UG / VG : 0;
    if (KL == 0 || KG == 0) {
      res = V / VE;
      return;
    }

    Double CR = (UL + UG + VE*X) / (VL+VG+VE);
    if (CR > X + eps) {
      VG = (UL - X*VL) / (X - CG);
      if (VG < 0) {
	VG = 0;
	VL = 0;
      }
    } else if (CR < X - eps) {
      VL = (UG - X*VG) / (X - CL);
      if (VL < 0) {
	VG = 0;
	VL = 0;
      } 
    }
    if (VL+VG+VE < eps) {
      res = -1;
      return;
    }
    CR = (VL*CL + VG*CG + VE*X) / (VL+VG+VE);
    if (CR-X > eps || CR-X < -eps) {
      res = -1;
      return;
    }

    res = V / (VL+VG+VE);
  }

  void print(int testId) {
    printf("Case #%d: ", testId+1);
    if (res < 0)
      printf("IMPOSSIBLE\n");
    else
      printf("%.10lf\n", res);

  }
};

//============================================================


queue<int> _testQueue;
mutex _testQueueMutex;
int _testsDone;
int _allTests;

TestCase Tests[MAX_TESTS];

void _solveTest(int testId) {
  Tests[testId].solve();
}

void _solveTestsFromQueue() {
  while (true) {
    int nextTest = -1;
    {
      lock_guard<mutex> lock(_testQueueMutex);
      if (_testQueue.empty()) break;
      nextTest = _testQueue.front();
      _testQueue.pop();
    }
    _solveTest(nextTest);
    if (PRINT_TESTS_PROGRESS) {
      lock_guard<mutex> lock(_testQueueMutex);
      ++_testsDone;
      fprintf(stderr, "Done %d/%d (test %d)\n", _testsDone, _allTests, nextTest + 1);
    }
  }
}

void _readTests() {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    Tests[t].read();
    _testQueue.push(t);
  }
  _allTests = T;
}

void _solveTests() {
  thread threads[THREADS];
  for (int i = 0; i < THREADS; ++i) {
    threads[i] = thread(_solveTestsFromQueue);
  }
  for (int i = 0; i < THREADS; ++i) {
    threads[i].join();
  }
}

void _printResults() {
  for (int i = 0; i < _allTests; ++i) {
    Tests[i].print(i);
  }
}

int main() {
  _readTests();
  _solveTests();
  _printResults();
  return 0;
};
