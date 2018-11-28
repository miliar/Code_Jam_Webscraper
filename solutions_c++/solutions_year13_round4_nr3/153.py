#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>
#include <cctype>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <algorithm>
#include <numeric>
#include <functional>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

#define FILE_IN  "C-small-attempt0.in"
#define FILE_OUT "C-small-attempt0.out"

#define MAXN 20

int N;

int A[MAXN];
int B[MAXN];

int last[MAXN];
bool L[MAXN][MAXN];

int X[MAXN];
bool used[MAXN];

void assign(int i) {
	if (X[i] >= 0)
		return;
	int m = 0;
	for (int j = 0; j < N; ++j)
		if (L[j][i]) {
			assign(j);
			m = max(m, X[j] + 1);
		}
	while (used[m])
		++m;
	used[m] = true;
	X[i] = m;
}

void solve() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
		scanf("%d", &A[i]);
	for (int i = 0; i < N; ++i)
		scanf("%d", &B[i]);
	fill(L[0], L[N], false);
	fill(last, last+N, -1);
	for (int i = 0; i < N; ++i) {
		int a = A[i] - 1;
		if (last[a] >= 0)
			L[i][last[a]] = true;
		if (a > 0)
			L[last[a-1]][i] = true;
		
		last[a] = i;
	}
	fill(last, last+N, -1);
	for (int i = N - 1; i >= 0; --i) {
		int b = B[i] - 1;
		if (last[b] >= 0)
			L[i][last[b]] = true;
		if (b > 0)
			L[last[b-1]][i] = true;
		last[b] = i;
	}
	for (int k = 0; k < N; ++k)
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				if (L[i][k] && L[k][j])
					L[i][j] = true;
	fill(X, X + N, -1);
	fill(used, used + N, false);
	for (int i = 0; i < N; ++i)
		assign(i);
	for (int i = 0; i < N; ++i)
		printf(" %d", X[i] + 1);
	printf("\n");
}

int main() {
	freopen(FILE_IN, "r", stdin);
	freopen(FILE_OUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d:", i);
		fprintf(stderr, "Case #%d: ...", i); fflush(stderr);
		solve();
		fprintf(stderr, " done\n"); fflush(stderr);
	}
	return 0;
}
