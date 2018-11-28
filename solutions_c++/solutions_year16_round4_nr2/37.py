/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define zero(a) memset(a, 0, sizeof(a))
#  define err(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)


const int N = 207;

int n, k;
double p[N], f1[N][N], f2[N][N], f3[N][N], sum[N][N][N];

void add( double *f1, double *f, double p ) {
	forn(t, k + 1) {
		f1[t] += f[t] * p;
		f1[t + 1] += f[t] * (1 - p);
	}
}

void solve() {
	cin >> n >> k;
	double p[n];
	err("solve %d %d\n", n, k);
	forn(i, n) cin >> p[i];
	sort(p, p + n);
	zero(f1);
	zero(f2);
	f1[0][0] = f2[0][0] = 1;
	forn(i, k) add(f1[i + 1], f1[i], p[i]);
	forn(i, k) add(f2[i + 1], f2[i], p[n - i - 1]);
	zero(sum);
	forn(i, k + 1)
		forn(j, k - i + 1) 
			forn(i_get, k / 2 + 1)
				forn(j_get, k / 2 + 1)
					sum[i][j][i_get + j_get] += f1[i][i_get] * f2[j][j_get];
	double res = 0;
	forn(c, n) {
		zero(f3);
		f3[0][0] = 1;
		forn(i, min(n - c, k))
			add(f3[i + 1], f3[i], p[c + i]);
/*
		forn(i, min(n - c, k) + 1) {
			err("%d : ", i);
			forn(j, k + 1)
				err("%.5f ", f3[i][j]);
			err("\n");
		}
*/
		forn(a, k + 1)
			forn(b, k - a + 1) {
				int rest = k - a - b;
				if (rest < 0 || a > c || c + rest > n - b)
					continue;
				double tmp = 0;
				forn(c_get, k / 2 + 1) {
					//err("%d : %.5f * %.5f\n", c_get, f3[rest][c_get] , sum[a][b][k / 2 - c_get]);
					tmp += f3[rest][c_get] * sum[a][b][k / 2 - c_get];
				}
				//err("check a=%d b=%d [c=%d,rest=%d] -> %.9f\n", a, b, c, rest, tmp);
				res = max(res, tmp);
			}
	}
	printf("%.9f\n", res);
}

int main() {
  int n;
  scanf("%d ", &n);
  for (int i = 1; i <= n; i++) {
    printf("Case #%d: ", i);
    solve();
  }
}
