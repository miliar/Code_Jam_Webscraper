#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
typedef long double ld;

int t;
int n, k;
ld p[222];
vector<ld> st;
ld dp[222][222];
ld ans;
void go() {
	dp[0][0] = 1;
	fo(i,1,k+1) {
		dp[i][0] = dp[i-1][0] * (1 - st[i-1]);
		fo(j,1,i+1) dp[i][j] = dp[i-1][j-1] * st[i-1] + dp[i-1][j] * (1 - st[i-1]);
	}
	//fo(i,0,k+1) fo(j,0,k+1) printf("%d %d %Lf\n", i, j, dp[i][j]);
	ans = max(ans, dp[k][k/2]);
}
int main() {
	scanf("%d", &t);
	fo(_,1,t+1) {
		printf("Case #%d: ", _);
		scanf("%d %d", &n, &k);
		fo(i,0,n) scanf("%Lf", p+i);
		sort(p, p+n);
		fo(i,0,k+1) {
			st.clear();
			fo(j,0,i) st.push_back(p[j]);
			fo(j,n-k+i,n) st.push_back(p[j]);
			go();
		}
		printf("%.10Lf\n", ans);
		ans = 0;
		fo(i,0,222) fo(j,0,222) dp[i][j] = 0;
	}

	return 0;
}