#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;

double fir[300][300], bak[300][300];
double p[1000];
int n, k;

int main(){
	int times;
	scanf("%d", &times);
	for (int t = 1; t<=times; t++){
		scanf("%d %d", &n, &k);
		for (int i=1; i<=n; i++){
			scanf("%lf", &p[i]);
		}
		sort(p+1, p+n+1);
		memset(fir, 0, sizeof(fir));
		fir[0][0] = 1;
		for (int i=1; i<=n; i++)
			for (int j=0; j<=n; j++){
				if (j>0){
					fir[i][j] += fir[i-1][j-1] * p[i];
				}
				fir[i][j] += fir[i-1][j] * (1 - p[i]);
			}
		memset(bak, 0, sizeof(bak));
		bak[0][0] = 1;
		for (int i=1; i<=n; i++)
			for (int j=0; j<=n; j++){
				if (j>0){
					bak[i][j] += bak[i-1][j-1] * p[n-i+1];
				}
				bak[i][j] += bak[i-1][j] * (1 - p[n-i+1]);
			}
		double ans = 0.0;
		for (int i=0; i<=k; i++){
			double tmp = 0;
			for (int j=0; j<=i; j++){
				if (j > k/2) continue;
				tmp += fir[i][j] * bak[k-i][k / 2 - j];
			}
			if (tmp > ans){
				ans = tmp;
			}
		}
		printf("Case #%d: %.10lf\n", t, ans);
	}
	return 0;
}
