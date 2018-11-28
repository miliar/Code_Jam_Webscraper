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

int a[1009];
int dp[1009][1009];
int before[1009], after[1009];

int get() {
	int n;cin>>n;
	FOR(i,1,n)cin>>a[i];
	vector<pair<int,int> > g;
	g.pb(mp(-1, 0));
	FOR(i,1,n) g.pb(mp(a[i], i));
	sort(g.begin(), g.end());
	//sort(a+1, a+n+1);

	memset(before, 0, sizeof(before));
	memset(after, 0, sizeof(after));
	FOR(i,1,n) {
		before[i]=0;
		after[i]=0;
		FOR(j,1,i-1) before[i]+=(a[i]<a[j]);
		FOR(j,i+1,n) after[i]+=(a[i]<a[j]);
	}

	memset(dp, 63, sizeof(dp));
	dp[0][0]=0;
	FOR(i,0,n-1) FOR(j,0,i) {
		int pos = g[i+1].second;
		dp[i+1][j+1]=min(dp[i+1][j+1], dp[i][j]+before[pos]);
		dp[i+1][j]=min(dp[i+1][j], dp[i][j]+after[pos]);
	}

	int ans=inf;
	FOR(i,0,n) ans=min(ans, dp[n][i]);
	return ans;
}

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(tt,1,t) {
		cout<<"Case #"<<tt<<": ";
		cout<<get()<<endl;
	}
}