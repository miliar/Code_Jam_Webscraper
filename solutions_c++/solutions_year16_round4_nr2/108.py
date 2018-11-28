#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define add(x,y) ((ll)(x)+(y))%mod
#define F(i,n) for(int i = 0; i < n; i++)
#define FF(i,n) for(int i = 1; i <= n; i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const double pi = 3.1415926535897932384626433832795;
//----------------------------------------------------------------------------//

double dyn[200][201];
double p[200];
double curp[200];
int main() {
#ifndef __GNUG__
	freopen("B-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: ", ++casen);
		int n, k; nii(n, k);
		F(i, n) {
			scanf("%lf", p + i);
		}
		sort(p, p + n);
		double ans = -1;
		F(num1, k + 1) {
			F(i, num1) curp[i] = p[i];
			F(i, k - num1) curp[i + num1] = p[n + num1 - k + i];
			dyn[0][1] = curp[0];
			dyn[0][0] = 1 - curp[0];
			FF(i, k - 1) {
				F(j, k + 1) {
					dyn[i][j] = (1-curp[i])*dyn[i-1][j];
					if (j) dyn[i][j] += curp[i] * dyn[i - 1][j - 1];
				}
			}
		//	printf("curans %d %.15f\n", num1, dyn[k - 1][k / 2]);
			ans = max(ans, dyn[k - 1][k / 2]);
		}
		printf("%.15f\n", ans);
	}

	return 0;
}
