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

int Less[2010][2010];
int A[2010];
int B[2010];
int K[2010];
int R[2010];

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
      scanf("%d", &A[i]);
    for (int i = 0; i < N; ++i)
      scanf("%d", &B[i]);

    CLEAR(Less, 0);
    for (int i = 0; i < N; ++i) {
      bool found = false;
      for (int j = i-1; j >= 0; --j) {
	if (A[j] >= A[i]) {
	  Less[i][j] = 1;
	  Less[j][i] = -1;
	} else if (A[j] < A[i]) {
	  if (!found) {
	    Less[i][j] = -1;
	    Less[j][i] = 1;
	    if (A[j] == A[i] - 1)
	      found = true;
	  }
	}
      }
    }

    //    cout << "less 2,0 = " << Less[2][0] << endl;

    for (int i = N-1; i >= 0; --i) {
      bool found = false;
      for (int j = i+1; j < N; ++j) {
	if (B[j] >= B[i]) {
	  Less[i][j] = 1;
	  Less[j][i] = -1;
	} else if (B[j] < B[i]) {
	  if (!found) {
	    Less[i][j] = -1;
	    Less[j][i] = 1;
	    if (B[j] == B[i] - 1)
	      found = true;
	  }
	}
      }
    }

    //    cout << "less 2,0 = " << Less[2][0] << endl;

    for (int i = 0; i < N; ++i) {
      K[i] = 0;
      for (int j = 0; j < N; ++j)
	if (Less[j][i] == 1)
	  ++K[i];
    }
    priority_queue<int, vector<int>, greater<int> > Q;
    /*    cout << "K = ";
    for (int i = 0; i < N; ++i)
      cout << K[i] << " ";
    cout << endl;
    */
    for (int i = 0 ; i < N; ++i)
      if (K[i] == 0) {
	Q.push(i);
      }
    for (int i = 0; i < N; ++i) {
      int a = Q.top();
      Q.pop();
      R[a] = i+1;
      for (int j = 0; j < N; ++j)
	if (Less[a][j] == 1) {
	  --K[j];
	  if (K[j] == 0)
	    Q.push(j);
	}
    }
    printf("Case #%d:", t+1);
    for (int i = 0; i < N; ++i)
      printf(" %d", R[i]);
    printf("\n");
  }

  return 0;
};
