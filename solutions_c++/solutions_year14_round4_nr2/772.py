#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <memory.h> 
#include <math.h> 
#include <assert.h> 
#include <stack> 
#include <queue> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <string> 
#include <functional> 
#include <vector> 
#include <deque> 
#include <utility> 
#include <bitset> 
#include <limits.h>  

using namespace std; 
typedef long long ll; 
typedef unsigned long long llu; 
typedef double lf;
typedef unsigned int uint;
typedef long double llf;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
#define memset0(x) memset(x, 0, sizeof (x));

int TC, TCC;

const int N_ = 1005;

int N, A[N_], P[N_];
int S[N_][N_];
int Table[N_][N_];

bool cmpP (const int &a, const int &b) { return A[a] < A[b]; }

void init () {
	for(int i = 0; i <= N; i++) for(int j = 0; j <= N; j++) {
		S[i][j] = 0;
	}
}

void upd_min (int &v, int c) {
	if(v > c) v = c;
}

int sum (int x1, int y1, int x2, int y2) {
	return S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1];
}

void solve () {
	scanf("%d", &N);
	for(int i = 1; i <= N; i++) scanf("%d", A+i), P[i] = i;

	sort(P+1, P+N+1, cmpP);

	for(int i = 1; i <= N; i++) S[i][P[i]] = 1;
	for(int i = 1; i <= N; i++) for(int j = 1; j <= N; j++) S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1];
	
	for(int d = 1; d <= N; d++) {
		for(int i = 0, j = d; i <= d; i++, j--) {
			Table[i][j] = (int)1e9;
			if(i > 0) upd_min (Table[i][j], Table[i - 1][j] + sum(d, 1, N, P[d]) - 1);
			if(j > 0) upd_min (Table[i][j], Table[i][j - 1] + sum(d, P[d], N, N) - 1);
		}
	}

	int res = (int)1e9;
	for(int i = 0; i < N; i++) res = min(res, Table[i][N - i]);

	printf("Case #%d: %d\n", TCC, res);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &TC);
	while(++TCC <= TC) {
		init();
		solve();
	}
	return 0;
}