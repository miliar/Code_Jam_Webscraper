#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <ctime>
using namespace std;

#define rep(i, n) for (int i=0; i<(n); ++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define repd(i, a, b) for (int i=(a); i>=(b); --i)
#define clr(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define sz(a) ((int)(a).size())

#define M 8

int i,j,k,m,n,l;
vector<int> a[4];
int x, y;
string s[M+10];

void dfs(int d){
	if (d==m){
		rep(i, n) if (!sz(a[i])) return;
		int k=0;
		rep(i, n){
			set<string> st;
			rep(l, sz(a[i])){
				int j=a[i][l];
				repf(u,0, sz(s[j]))
					st.insert(s[j].substr(0, u));
			}
			k+=sz(st);
		}	
		if (k>x) x=k, y=1;
		else if (k==x) y++;
		return;
	}
	rep(i, n){
		a[i].pb(d);
		dfs(d+1);
		a[i].pop_back();
	}
}

int main(){
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int ts;
	scanf("%d", &ts);
	repf(te, 1, ts){
		scanf("%d%d", &m, &n);
		rep(i, m) cin>>s[i];
		x=-1;
		dfs(0);
		printf("Case #%d: %d %d\n", te, x, y);
	}
	return 0;
}
