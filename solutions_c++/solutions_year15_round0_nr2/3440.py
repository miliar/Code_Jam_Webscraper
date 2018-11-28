#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>
#include <stack>
#include <queue>
#include <sstream>
#include <numeric>
#include <iterator>
using namespace std;

#define maX(a, b) ( (a) > (b) ? (a) : (b))
#define miN(a, b) ( (a) < (b) ? (a) : (b))
#define pb push_back
#define mp make_pair
#define fill(a, v) memset(a, v, sizeof a)
#define tr(v, it) for(typeof((v).begin()) it = (v).begin(); it != (v).end();it++)
#define ff first
#define ss second

const int INF = 1e9;
const double eps = 1e-9;
typedef long long lli;

lli gcd(lli a, lli b) { if(a == 0) return b; return gcd(b%a, a);}
lli exp(lli base, lli expo, lli m) { lli ans = 1;while(expo > 0) {ans = (ans * base) % m; expo >>= 1; base = (base * base) % m;} return ans;}


using namespace std;
#define sz 1010

int dp[sz][sz];

int main()
{
	for (int i = 0; i < sz; ++i) {
	    for (int j = 0; j < i; ++j) {
	        dp[i][j] = 1000000;
	        for (int k = 1; k <= (i / 2); ++k) {
	            dp[i][j] = min(dp[i][j], 1 + (dp[k][j] + dp[i - k][j]));
	        }
	    }
	}

	freopen("B-large.in.txt", "r", stdin);
	freopen("out1.txt", "w", stdout);

	int T, n, maxx;
	int ans, Ans;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; kase++) {
	    scanf("%d", &n);
	    int arr[n];
	    maxx = -1;
	    for (int i = 0; i < n; ++i) {
	        scanf("%d", &arr[i]);
	        maxx = max(maxx, arr[i]);
	    }

	    Ans = INT_MAX;
	    for (int i = 1; i <= maxx; ++i) {
	        ans = i;
	        for (int j = 0; j < n; ++j) {
	            ans += dp[arr[j]][i];
	        }
	        Ans = min(Ans, ans);
	    }

	    printf("Case #%d: %d\n", kase, Ans);
	}

    return 0;
}
