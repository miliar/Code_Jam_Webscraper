#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int n, k;
double a[555];
double dp[555][555];

double solve(vector<double> e) {
	int k = e.size();
		for (int i = 0; i <= k; i++) for (int j = 0; j <= k; j++) dp[i][j] = 0;
		dp[0][0] = 1;

		for (int i = 0; i < k; i++) for (int j = 0; j < k; j++) {
			dp[i + 1][j] += dp[i][j] * (1 - e[i]);
			dp[i + 1][j + 1] += dp[i][j] * e[i];
		}
	return dp[k][k / 2];		
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> k;
		for (int i = 0; i < n; i++) cin >> a[i];
		sort(a, a + n);
		vector<double> e;
		for (int i = 0; i < k / 2; i++) {
			e.pb(a[i]);
			e.pb(a[n - 1 - i]);		
		}
		double ret = 0;
		for (int i = 0; i <= k; i++) {
			e.clear();
			for (int j = 0; j < i; j++) e.pb(a[j]);
			for (int j = 0; j < k - i; j++) e.pb(a[n - 1 - j]);
			ret = max(ret, solve(e));
		}
		for (int i = 0; i + k <= n; i++) {
			e.clear();
			for (int j = 0; j < k; j++) e.pb(a[i + j]);
			ret = max(ret, solve(e));
		}

		cout << "Case #" << tt << ": ";
		printf("%.10lf\n", ret);

	}
	return 0;
}