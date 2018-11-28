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

string s[11];
int cnt, best;
vector<int> g[11];
int serv, n;

int getV(int v) {
	set<string> ans;
	FOR(i,0,sz(g[v])-1) FOR(len,0,sz(s[g[v][i]])) ans.insert(s[g[v][i]].substr(0, len));
	return sz(ans);
}

void go(int pos) {
	if(pos==n+1)  {
		int cur=0;
		FOR(i,1,serv) cur+=getV(i);

		if(cur==best) ++cnt;else 
		if(cur>best) {
			cnt=1;
			best=cur;
		}
		return;
	}
	FOR(i,1,serv) {
		g[i].pb(pos);
		go(pos+1);
		g[i].pop_back();
	}
}

pair<int,int> get() {
	cin>>n>>serv;
	FOR(i,1,n) cin>>s[i];

	cnt=0;
	best=-1;

	FOR(i,1,serv) g[i].clear();
	go(1);

	return mp(best, cnt);
}

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(tt,1,t) {
		cout<<"Case #"<<tt<<": ";
		pair<int,int> ans=get();
		cout<<ans.first<<" "<<ans.second<<endl;
	}
}