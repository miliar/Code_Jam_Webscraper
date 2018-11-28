#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>

#define sqr(a) (a) * (a)
#define N 30000

using namespace std;

int d[N];
double p[N];
int tt, t, i, j, n, k;

int main()  {

    #ifndef ONLINE_JUDGE
    freopen("a.in", "r" , stdin);
    freopen("a.out", "w", stdout);
    #endif

    cin >> t;
    for (tt = 1; tt <= t; tt++) {
    	cin >> n >> k;
    	double ans = 0;
    	for (i = 1; i <= n; i++)
    		cin >> p[i];

		for (int msk = 1; msk < (1 << n); msk++) {
			int valid = 0;
			for (j = 0; j < n; j++)
				if ((msk & (1 << j)) > 0)
					valid++;

			if (valid == k) {
				double prob2 = 0;
				int sz = 0;
				for (j = 0; j < n; j++)
					if ((msk & (1 << j)) > 0)
						d[sz++] = j + 1;

				for (int msk2 = 1; msk2 < (1 << sz); msk2++) {
					int valid2 = 0;
					for (j = 0; j < sz; j++)
						if ((msk2 & (1 << j)) > 0)
							valid2++;

			 		if (valid2 * 2 == k) {
			 			double prob = 1;
			 			for (j = 0; j < sz; j++)
							if ((msk2 & (1 << j)) > 0)
								prob *= p[d[j]];
							else
								prob *= (1 - p[d[j]]);
						prob2 += prob;
			 		}
				}
				ans = max(prob2, ans);
			}
		}
		printf("Case #%d: %.6lf\n", tt, ans);
    }
          
    return 0;
}