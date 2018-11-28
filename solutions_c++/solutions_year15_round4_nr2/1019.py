#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

using namespace std;

typedef long long LL;

const int maxn = 2333;
const int maxm = 2333;
const double EPS = 1e-10;

int Sgn(double u){
	return u < -EPS? -1: u > EPS;
}

int avali[maxm], avacnt;
long double a[maxn][maxm];
long double b[maxn], c[maxm];

double C[maxm], R[maxm];

long double *simplex(int n, int m){
	++m;
	int r = n, s = m - 1;
	static long double D[maxn + 2][maxm + 1];
	static int ix[maxn + maxm];
	for (int i = 0; i < n + m; ++i) ix[i] = i;
	for (int i = 0, nm = n + m + 10; i <= nm; ++i)
		for (int j = 0; j <= nm; ++j)
			D[i][j] = 0.0;
	for (int i = 0; i < n; ++i){
		for (int j = 0; j < m - 1; ++j) D[i][j] = -a[i][j];
		D[i][m - 1] = 1.0;
		D[i][m] = b[i];
		if (D[r][m] > D[i][m]) r = i;
	}
	for (int j = 0; j < m - 1; ++j) D[n][j] = c[j];
	D[n + 1][m - 1] = -1.0;
	for (double d; ; ){
		if (r < n){
			int t = ix[s];
			ix[s] = ix[r + m];
			ix[r + m] = t;
			D[r][s] = 1.0 / D[r][s];
			for (int j = 0; j <= m; ++j)
				if (j != s) D[r][j] *= -D[r][s];
			avacnt = 0;
			for (int i = 0; i <= m; ++i)
				if (fabs(D[r][i]) > EPS)
					avali[avacnt++] = i;
			for (int i = 0; i <= n + 1; ++i)
				if (i != r){
					if (fabs(D[i][s]) < EPS) continue;
					long double *cur1 = D[i], *cur2 = D[r], tmp = D[i][s];
					for (int j = 0; j < avacnt; ++j)
						if (avali[j] != s)
							cur1[avali[j]] += cur2[avali[j]] * tmp;
					D[i][s] *= D[r][s];
				}
		}
		r = -1;
		s = -1;
		for (int j = 0; j < m; ++j)
			if (s < 0 || ix[s] > ix[j]){
				if (D[n + 1][j] > EPS || D[n + 1][j] > -EPS && D[n][j] > EPS) s = j;
			}
		if (s < 0) break;
		for (int i = 0 ; i < n; ++i)
			if (D[i][s] < -EPS){
				if (r < 0 || (d = D[r][m] / D[r][s] - D[i][m] / D[i][s]) < -EPS || d < EPS && ix[r + m] > ix[i + m]) r = i;
			}
		if (r < 0) return NULL;
	}
	if (D[n + 1][m] < -EPS) return NULL;
	static long double x[maxm - 1];
	for (int i = m; i < n + m; ++i)
		if (ix[i] < m - 1) x[ix[i]] = D[i - m][m];
//printf("sum == %.9f\n", D[n][m]);
	return x;
}

long double *ans;

int main(){
	int T;
	scanf("%d", &T);
	for (int TI = 1; TI <= T; ++TI){
		int n;
		double X, V;
		scanf("%d%lf%lf", &n, &V, &X);
		for (int i = 0; i < n; ++i)
			scanf("%lf%lf", &R[i], &C[i]);
		for (int i = 0; i < n; ++i)
			a[0][i] = (long double)(R[i] * C[i]);
		b[0] = V * X;
		for (int i = 0; i < n; ++i)
			a[1][i] = (long double)(-R[i] * C[i]);
		b[1] = -V * X;
		for (int i = 0; i < n; ++i)
			a[2][i] = (long double)(R[i]);
		b[2] = V;
		for (int i = 0; i < n; ++i)
			a[3][i] = (long double)(-R[i]);
		b[3] = -V;
		long double ANS = 1e13;
		bool flag = 0;
		for (int i = 0; i < n; ++i){
			int N = 3;
			for (int j = 0; j < n; ++j){
				++N;
				for (int k = 0; k < n; ++k)
					a[N][k] = 0.0;
				a[N][j] += 1.0;
				a[N][i] -= 1.0;
				b[N] = 0.0;
			}
			++N;
			for (int j = 0; j < n; ++j)
				c[j] = 0.0;
			c[i] = -1.0;
			ans = simplex(N, n);
			if (ans != NULL){
				ANS = fmin(ANS, ans[i]);
				flag = 1;
			}
/*
if (ans != NULL){
	for (int j = 0; j < n; ++j)
		printf("%.9f ", ans[j]);
	printf("\n");
for (int k = 0; k < N; ++k){
double sum = 0.0;
for (int j = 0; j < n; ++j)
	sum += a[k][j] * ans[j];
printf("%.9f %.9f\n", sum, b[k]);
printf("\n");
}
}
*/
		}
		printf("Case #%d: ", TI);
		if (flag) printf("%.11f\n", (double)ANS);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
