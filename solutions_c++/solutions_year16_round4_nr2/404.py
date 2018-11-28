#include<bits/stdc++.h>

using namespace std;

const int MAXN = 1e3 + 10;

double ans;
int n,k;
double a[MAXN],b[MAXN],f[MAXN][MAXN];

int main(){
	freopen("Bl.in", "r", stdin);
	freopen("Bl.out", "w", stdout);
	int T;
	cin>>T;
	for(int o = 1; o <= T; o++){
		printf("Case #%d: ", o);
		cin>>n>>k;
		for(int i = 1; i <= n; i++)
			scanf("%lf", &a[i]);
		sort(a + 1, a + n + 1);
		ans = 0;
		for(int i = 0; i <= k; i++){
			for(int j = 1; j <= i; j++)
				b[j] = a[j];
			for(int j = 1; j <= k - i; j++)
				b[j + i] = a[n - j + 1];
			for(int i = 0; i <= k; i++)
				f[0][i] = 0;
			f[0][0] = 1;
			for(int i = 1; i <= k; i++)
				for(int j = 0; j <= k; j++)
					f[i][j] = f[i-1][j] * (1 - b[i]) + (j > 0 ? f[i - 1][j - 1] * b[i] : 0);
			ans = max(ans, f[k][k/2]);
		}
		printf("%.10f\n", ans);
	}
	return 0;
}
