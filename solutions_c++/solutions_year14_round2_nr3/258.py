#pragma comment(linker,"/STACK:300000000")
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <stack>

#define gcd(a,b) __gcd((a),(b))
#define sqr(a) ((a)*(a))
#define odd(a) ((a)&1)
#define foru(i,n) for (int i=0;i<(n);i++)
#define ford(i,n) for (int i=(n)-1;i>=0;i--)
#define forab(i,l,r) for (int i=(l);i<=(r);i++)
#define forabd(i,r,l) for (int i=(r);i>=(l);i--)
#define fillchar(a,b) memset((a),(b),sizeof((a)))
#define pb push_back
#define F first
#define S second
#define all(x) x.begin,x.end
#define pw2(x) (1ull<<(x))
#define mp make_pair
#define filename "inp"

const long double eps=1e-20;
const long double pi=acos(-1.0);
const long long inf=1000*1000*1000*1000*1000*1000;
const long long base=1000*1000*1000+7;

using namespace std;

struct node{
	int x,y;
};
int all = 0;
int n,m;
string ans, tmp;
node ed[100];
bool used[111];
vector <int> g[111];
int a[111];
string s[111];

void dfs1(int v){
	used[v] = true;
	foru(j,g[v].size()) if (!used[g[v][j]]) dfs1(g[v][j]);
}

void dfs(int v){
	used[v] = true;
	vector <pair <string, int> > path;
	path.clear();
	foru(j,g[v].size())	if (!used[g[v][j]]){
		path.pb(mp(s[g[v][j]], g[v][j]));
	}
	sort(path.begin(), path.end());
	foru(j,path.size()){
		tmp += path[j].F;
		dfs(path[j].S);
	}
}

void check(){
	
	foru(i,n) g[i].clear();
	foru(i,n - 1){
		g[ed[a[i]].x].pb(ed[a[i]].y);
		g[ed[a[i]].y].pb(ed[a[i]].x);
	}
	foru(i,n) used[i] = false;
	dfs1(0);
	foru(i,n) if (!used[i]) return;
	foru(i,n){
		tmp = s[i];
		foru(j,n) used[j] = false;
		dfs(i);
		if (tmp < ans) ans = tmp;
	}
}

void rec(int pos, int last){
	if (pos == n - 1){
		check();
	
		return;
	}
	forab(i, last, min(m - 1, pos + m - n + 1) ){
		a[pos] = i;
		rec(pos + 1, i + 1);
	}
}

void solve(){
	cin >> n >> m;
	foru(i,n) cin >> s[i];
	foru(i,m){
		cin >> ed[i].x >> ed[i].y;
		ed[i].x--; ed[i].y--;
	}
	ans = "";
	foru(i,n) foru(j,10) ans += '9';
	rec(0,0);	
	cout << ans << endl;
}

int main(){
	freopen (filename".in","r",stdin);
	freopen (filename".out","w",stdout);	
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++){
		cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
