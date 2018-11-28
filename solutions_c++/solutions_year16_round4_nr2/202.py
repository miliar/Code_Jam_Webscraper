#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

double pr[200];
int np = 0;
double prob[220][220];
main() {
	FILE *fin = freopen("B-large.in", "r", stdin);
	FILE *fout = freopen("B-large.out", "w", stdout);
	assert( fin!=NULL );
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int n, k;
		cin >> n >> k;
		double p[n];
		for(int i = 0; i < n; i++) cin >> p[i];
		sort(p,p+n);
		int something[k];
		double ans = 0.0;
		for(int d = 0; d <= k; d++){
			np = 0;
			for(int i = 0; i < d; i++){
				pr[np++] = p[i];
			}
			for(int i = n-(k-d); i < n; i++){
				pr[np++] = p[i];
			}
			for(int i = 0; i < 220; i++){
				for(int j = 0; j < 220; j++){
					prob[i][j] = 0;
				}
			}
			prob[0][0] = 1.0;
			for(int i = 0; i < k; i++){
				for(int j = 0; j <= k; j++){
					prob[i+1][j] += prob[i][j] * (1-pr[i]);
					prob[i+1][j+1] += prob[i][j] * (pr[i]);
				}
			}
			ans = max(ans, prob[k][k/2]);
		}
		printf("%.10lf\n", ans);
	}
	exit(0);
}