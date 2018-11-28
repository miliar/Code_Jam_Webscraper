#include <bits/stdc++.h>
using namespace std;

#ifdef WIN32
    #define lld "%I64d"
#else
    #define lld "%lld"
#endif

#define mp make_pair
#define pb push_back
#define put(x) { cout << #x << " = "; cout << (x) << endl; }

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef double db;

const int M = 1e6 + 15;
const int Q = 1e9 + 7;

ld ans;
ld dp[50][50];
ld p[50];
vector<int> g;
        
void gen(int n, int k, int pos) {
	if (pos == n) {
	   	for (int i = 0; i <= k; i++)
	   		for (int j = 0; j <= k; j++)
	   			dp[i][j] = 0;
	   	dp[0][0] = 1.;
	   	for (int i = 0; i < k; i++) {
	   		for (int x = 0; x <= i; x++) {
	   			dp[i + 1][x] += dp[i][x] * (1 - p[g[i]]);
	   			dp[i + 1][x + 1] += dp[i][x] * p[g[i]];
	   		}
	   	}
	   	ans = max(ans, dp[k][k / 2]);
	   	return;
	}
	if (n - pos - 1 + (int)g.size() >= k)
		gen(n, k, pos + 1);
	if ((int)g.size() < k) {
		g.pb(pos);
		gen(n, k, pos + 1);
		g.pop_back();
	}	
}
int main(){
    srand(time(NULL));
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int it = 1; it <= T; it++) {
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)  {
			cin >> p[i];
		}	
		ans = 0.;
		gen(n, k, 0);
		printf("Case #%d: %.8f\n", it, (double)ans);
	}
		
    return 0;
}   