#include <bits/stdc++.h>
using namespace std;
#define dd pair<double,double>
#define vi vector<int>
#define vii vector<ii, ii>
#define vvi vector<vi>
#define MAXN 105
#define MAXE 10005
#define FOR(x,n) for(int x = 0; x < n; x++)
#define FOR1e(x,n) for(int x = 1; x <= n; x++)
#define MOD 1000000007

long double prob[205];
long double votos[205][205];

long double conjunto[205];

long double calc(int k) {
	votos[1][1] = conjunto[0];
	votos[1][0] = 1-conjunto[0];

	for(int i = 1; i < k; i++) {
		for(int j = 0; j <= i+1; j++) {
			votos[i+1][j] = votos[i][j]*(1-conjunto[i]);
			if(j > 0) votos[i+1][j] += votos[i][j-1]*conjunto[i];
		}
	}
/*	for(int j = 0; j < k; j++) {
		printf("%.3Lf ", conjunto[j]);
	}
	printf("\n%.5Lf\n", votos[k][k/2]);*/
	return votos[k][k/2];
}

int main() {
	int n, k, t;
	scanf("%d", &t);
	FOR1e(caso, t) {
		scanf("%d %d", &n, &k);
		FOR(x, n) scanf("%Lf", &prob[x]);
		sort(prob, prob + n);

		long double ans = 0.0;
		for(int i = n-k; i < n; i++) {
			conjunto[i-(n-k)] = prob[i];
		}
		ans = max(ans, calc(k));
			
		for(int i = 0; i < k; i++) {
			conjunto[i] = prob[i];
			ans = max(ans, calc(k));
		}

		for(int i = 0; i < n-k; i++) {
			for(int j = 0; j < k; j++) {
				conjunto[j] = prob[i+j];
			}
			ans = max(ans, calc(k));
		}

		printf("Case #%d: %.15Lf\n", caso, ans);
	}
	return 0;
}