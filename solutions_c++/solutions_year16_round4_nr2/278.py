#include "bits/stdc++.h"
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define bend(_x) (_x).begin(), (_x).end()
#define szof(_x) ((int) (_x).size())
#define TASK_NAME ""

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int MAXN = 205;

double calc(vector<double> v) {
 	sort(bend(v));

 	vector<double> d[2];
 	d[0].resize(szof(v) * 2 + 1);
	d[1].resize(szof(v) * 2 + 1);
	d[0][szof(v)] = 1;
 	for (double p: v) {
 		fill(bend(d[1]), 0);
 	 	for (int i = -szof(v); i <= szof(v); ++i) {
 	 	 	if (i < szof(v)) {
 	 	 		d[1][i + 1 + szof(v)] += d[0][i + szof(v)] * p;
 	 	 	}
 	 	 	if (i > -szof(v)) {
 	 	 		d[1][i - 1 + szof(v)] += d[0][i + szof(v)] * (1 - p);
 	 	 	}
 	 	}
 	 	d[0] = d[1];
 	}
 	return d[0][szof(v)];
}

double d[MAXN][MAXN][MAXN * 2];

int solve() {
 	int n, k;
 	scanf("%d%d", &n, &k);

 	vector<double> inp;
 	for (int i = 0; i < n; ++i) {
 	 	double num;
 	 	scanf("%lf", &num);
 	 	inp.puba(num);
 	}

 	sort(bend(inp));

 	double ans = -1;
 	//int mem = -1;
 	int bdv = 1 << n;
 	for (int i = 0; i < bdv; ++i) {
 	 	if (__builtin_popcount(i) != k) {
 	 	 	continue;
 	 	}
 	 	vector<double> v;
 	 	int tmp = i;
 	 	for (int j = 0; j < n; ++j) {
 	 	 	if (tmp & 1) {
 	 	 	 	v.puba(inp[j]);
 	 	 	}
 	 	 	tmp >>= 1;
 	 	}
 	 	double val = calc(v);
 	 	if (ans < val) {
 	 	 	ans = val;
 	 	 	//mem = i;
 	 	}
 	}

 	printf("%.15f\n", ans);
 	/*
 	for (auto num: inp) {
 	 	cerr << num << " ";
 	}
 	cerr << endl;
 	for (int i = 0; i < n; ++i) {
 	 	cerr << (mem & 1);
 	 	mem >>= 1;
 	}
 	cerr << endl;
 	*/
 	/*
 	memset(d, 0, sizeof d);
 	d[0][0][MAXN] = 1;
 	for (int i = 0; i < n; ++i) {
 	 	for (int j = 0; j < n; ++j) {
 	 	 	for (int j2 = -k; j2 <= k; ++j2) {
 	 	 	 	d[i + 1][j + 1][j2 + 1 + MAXN] += d[i][j][j2 + MAXN] * inp[i];
 	 	 	 	d[i + 1][j + 1][j2 - 1 + MAXN] += d[i][j][j2 + MAXN] * (1 - inp[i]);
 	 	 	}
 	 	 	for (int j2 = 0; j2 < MAXN * 2; ++j2) {
 	 	 	 	d[i + 1][j + 1][j2] = max(d[i + 1][j + 1][j2], d[i][j + 1][j2]);
 	 	 	}
 	 	}
 	}

 	printf("%.15f\n", d[n][k][MAXN]);*/
 	return 0;
}

int solve2() {
 	int n, k;
 	scanf("%d%d", &n, &k);

 	vector<double> inp;
 	for (int i = 0; i < n; ++i) {
 	 	double num;
 	 	scanf("%lf", &num);
 	 	inp.puba(num);
 	}

 	sort(bend(inp));

 	double ans = -1;
 	
 	for (int i = 0; i <= k; ++i) {
 	 	vector<double> v;
 	 	for (int j = 0; j < i; ++j) {
 	 	 	v.puba(inp[j]);
 	 	}
 	 	for (int j = 0; j < k - i; ++j) {
 	 	 	v.puba(inp[n - j - 1]);
 	 	}
 	 	ans = max(ans, calc(v));
 	}

 	printf("%.15f\n", ans);

 	return 0;
}

int main() {
	//freopen(TASK_NAME ".in", "r", stdin);
	//freopen(TASK_NAME ".out", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; ++i) {
	 	cout << "Case #" << i + 1 << ": ";
	 	solve2();
	}

	return 0;
}