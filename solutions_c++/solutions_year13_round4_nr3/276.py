#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int MAXN = 2010;

int A[MAXN], B[MAXN], X[MAXN];
bool ok[MAXN][MAXN];
int cases, cas, N;

void init() {
	scanf("%d",&N);
	for (int i = 0; i < N; i++ )
		scanf("%d",A+i);
	for (int i = 0; i < N; i++ )
		scanf("%d",B+i);
}

void print(int X[] ) {
	for (int i = 0; i < N; i++ )
		printf(" %d",X[i]);
	printf("     ");
}

bool dfs(int run ) {
    if (run == N) return true;
	for (int i = 0; i < N; i++ )
		ok[run][i] = true;
	int index = -1, maxA = 0, maxB = 0;
	for (int i = 0; i < N; i++ )
		if (X[i] == 0) {
			if (A[i] != maxA + 1) ok[run][i] = false;
		}
		else maxA = max(maxA, A[i]);
	for (int i = N-1; i >= 0; i-- )
		if (X[i] == 0) {
			if (B[i] != maxB + 1) ok[run][i] = false;
		}
		else maxB = max(maxB, B[i]);
	for (int i = 0; i < N; i++ )
		if (X[i] == 0 && ok[run][i]) {
			index = i;
			X[index] = run + 1;
			if (dfs(run + 1)) return true;
			X[index] = 0;
		}
	return false;
}

void work() {
	memset(X, 0, sizeof(X));
	for (int run = 0; run < N; run++ ) {
//		print(X);
//		printf("\n");
		/*for (int i = N-1; i >= 0; --i )
			if (A[i] == 1) {
				index = i;
				break;
			}
		X[index] = run + 1;
		for (int i = index; i < N; i++ )
			if (A[i] > 0) A[i]--;
		for (int i = index; i >= 0; i-- )
			if (B[i] > 0) B[i]--;*/
	}
	dfs(0);
	printf("Case #%d:",cas);
	for (int i = 0; i < N; i++ )
		printf(" %d",X[i]);
	printf("\n");
}

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
	for (scanf("%d",&cases), cas = 1; cas <= cases; ++cas ) {
		init();
		work();
	}
	//system("pause");
	return 0;
}
