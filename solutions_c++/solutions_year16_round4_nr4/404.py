#include <algorithm>
#include <assert.h>
#include <complex>
#include <ctype.h>
#include <functional>
#include <iostream>
#include <limits.h>
#include <locale.h>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <vector>
#include <unordered_set>
#include <unordered_map>

#pragma warning(disable:4996)
using namespace std;

#define mp make_pair
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <ldb, ldb> pdd;

int IT_MAX = 1 << 17;
const int MOD = 10007;
const int INF = 1034567890;
const ll LL_INF = 1234567890123456789ll;
const db PI = acos(-1);
const ldb ERR = 1E-10;

char in[105][105];
char uin[105][105];
int Cnt[100000];
vector <pii> V;
int N;

int r[105];
int gcnt[105];
int cnt[105];
int root(int x) {
	return (r[x] == x) ? x : (r[x] = root(r[x]));
}
bool isValid() {
	int i, j;
	for (i = 0; i < N; i++) r[i] = i;
	
	vector <int> U;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) if (uin[i][j] == '1') U.push_back(j);
		for (j = 0; j + 1 < U.size(); j++) {
			int x = root(U[j]), y = root(U[j + 1]);
			if (x == y) continue;
			r[x] = y;
		}
		U.clear();
	}
	for (i = 0; i < N; i++) gcnt[i] = cnt[i] = 0;
	for (i = 0; i < N; i++) gcnt[root(i)]++;
	for (i = 0; i < N; i++) for (j = 0; j < N; j++) if (uin[i][j] == '1') cnt[j]++;

	for (i = 0; i < N; i++) if (gcnt[root(i)] != cnt[i]) return false;
	return true;
}
int main() {
	freopen("D-small-attempt3.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, i, j, k;
	for (i = 0; i < 70000; i++) {
		for (j = 0; j < 16; j++) if (i & (1 << j)) Cnt[i]++;
	}

	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d", &N);
		for (i = 0; i < N; i++) {
			scanf("%s", in[i]);
			for (j = 0; j < N; j++) if (in[i][j] == '0') V.push_back(pii(i, j));
			for (j = 0; j < N; j++) uin[i][j] = in[i][j];
		}
		
		int ans = INF;
		for (i = 0; i < (1 << V.size()); i++) {
			for (j = 0; j < V.size(); j++) {
				if (i & (1 << j)) uin[V[j].first][V[j].second] = '1';
				else uin[V[j].first][V[j].second] = '0';
			}
			if (isValid()) ans = min(ans, Cnt[i]);
		}
		printf("Case #%d: %d\n", tc, ans);

		V.clear();
	}
	
	return 0;
}
//*/