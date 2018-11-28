#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<queue>
#include<sstream>
#include<ctime>
using namespace std;

typedef long long Int;
#define FOR(i,a,b) for(int i=(a); i<=(b);++i)
#define mp make_pair
#define pb push_back
#define sz(s) (int)((s).size())
const int inf = 1000000000;
const int MOD = 1000000007;
const double pi=acos(-1.0);

int h[222], g[222];
int dp[222][222][1101];
int n,p,q;

int get(int pos, int cur, int moves) {
	if(pos>n) return 0;
	if(cur<=0) return get(pos+1, h[pos+1], moves);

	int&ans=dp[pos][cur][moves];
	if(ans!=-1) return ans;
	ans=0;

	//one temp
	if(moves) {
		if(p<cur) ans=max(ans, get(pos, cur-p, moves-1));else
			ans=max(ans, g[pos]+get(pos+1, h[pos+1], moves-1));
	}

	//boom
	if(cur<=p) {
		ans=max(ans, g[pos]+get(pos+1, h[pos+1]-q, moves));
	}else
		ans=max(ans, get(pos, cur-p-q, moves));

	//dont shoot
	if(q>=cur) ans=max(ans, get(pos+1, h[pos+1], moves+1));else
		ans=max(ans, get(pos, cur-q, moves+1));

	return ans;
}

double solve() {
	memset(dp, -1, sizeof(dp));

	cin>>p>>q>>n;
	FOR(i,1,n) cin>>h[i]>>g[i];

	return get(1, h[1], 0);
}

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(tt,1,t) {
		int ans = solve();
		cout<<"Case #"<<tt<< ": "<<ans<<endl;
		cerr<<tt<<endl;
	}
}