#include <bits/stdc++.h>
using namespace std;
#define TR(i,v) 		for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
#define DEBUG(x) 		cout << #x << " = "; cout << x << endl;
#define SIZE(p) 		(int)(p).size()
#define MP(a, b)		make_pair((a), (b))
#define ALL(p)			(p).begin(), (p).end()
#define rep(i, n)		for(int (i)=0; (i)<(int)(n); ++(i))
#define REP(i, a, n)	for(int (i)=(a); (i)<(int)(n); ++(i))
#define FOR(i, a, b)   	for(int (i)=(int)(a); (i)<=(int)(b); ++(i))
#define FORD(i, b, a)  	for(int (i)=(int)(b); (i)>=(int)(a); --(i)) 
typedef long long LL;
typedef pair<int, int> pii;
int dp[(1<<10)+10], p[100005];
int main(int argc, char const *argv[])
{
	#ifndef ONLINE_JUDGE
    freopen("A.in", "r", stdin);	
    freopen("A.out", "w", stdout);
    #endif
	// ios::sync_with_stdio(false);    cin.tie(0);
    int T;	cin>>T;
    FOR(cs,1,T)  {
    	printf("Case #%d: ", cs);
    	int n, m;	cin>>n>>m;
    	rep(i, n)	cin>>p[i];
    	memset(dp, 0x3f, sizeof(dp));
    	dp[0] = 0;
    	rep(mask, 1<<n) {
    		vector<pii> c;
    		rep(i, n) if(mask>>i&1)	c.push_back(pii(p[i], i));
    		int &res = dp[mask];
    		rep(i, SIZE(c)) {
    			res = min(res, dp[mask^(1<<c[i].second)]+1);
    		}
    		rep(i, SIZE(c))
    		REP(j, i+1, SIZE(c)) if(c[i].first+c[j].first <= m) {
    			res = min(res, dp[mask^((1<<c[i].second) | (1<<c[j].second))]+1);
    		}
    	}
    	printf("%d\n", dp[(1<<n)-1]);
    }    
	return 0;
}