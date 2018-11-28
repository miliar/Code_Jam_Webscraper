#include <iostream>
#include <functional>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <memory>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <utility>
#include <iterator>
#include <bitset>
#include <sstream>
#include <numeric>
#include <complex>

#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define LL long long
#define ULL unsigned LL
#define VI vector<int>
#define X first
#define Y second
#define sz(_v) ((int)_v.size())
#define all(_v) (_v).begin(),(_v).end()
#define FOR(i,a,b) for (LL i(a); i<=(b); ++i)
#define rep(i,a) FOR(i,1,a)
#define rept(i,a) FOR(i,0,(LL)(a)-1)
#define x1 X1
#define y1 Y1
#define sqr(a) ((a)*(a))
#define C(a) memset((a),0,sizeof (a))
#define MS(a,x) memset((a),(x),sizeof (a))
#define INF 1000000000
#define PI 3.141592653589
#define eps 1e-8
#define MOD 1000000007
#define PRIME 149

using namespace std;

//int n,m;
//int grid[105][505];
//
//bool dfs(int x, int y) {
//	if (grid[x][y])
//		return false;
//	grid[x][y]=true;
//
//	if (y==m-1)
//		return true;
//	if (x!=0 && dfs(x-1,y))
//		return true;
//	if (dfs(x,y+1))
//		return true;
//	if (x!=n-1 && dfs(x+1,y))
//		return true;
//	if (y!=0 && dfs(x,y-1))
//		return true;
//
//	return false;
//}
//
//void solvePart() {
//	int b;
//	C(grid);
//	scanf("%d%d%d",&n,&m,&b);
//	rept(i,b) {
//		int x0,y0,x1,y1;
//		scanf("%d%d%d%d",&x0,&y0,&x1,&y1);
//		FOR(i,x0,x1) FOR(j,y0,y1) {
//			grid[i][j]=true;
//		}
//	}
//	int ans(0);
//	rept(i,n)
//		if (dfs(i,0)) {
//			cerr<<i<<endl;
//			++ans;
//		}
//	printf("%d\n",ans);
//}

pii dyn[1<<9][5];

int nxt[100][26];
vector<string> data;
int cnt;
int n;

void init() {
	MS(nxt,-1);
	cnt=1;
}

void add(string &s) {
	int cur(0);
	rept(i,sz(s)) {
		char c(s[i]-'A');
		if (nxt[cur][c]==-1) {
			nxt[cur][c]=cnt;
			++cnt;
		}
		cur=nxt[cur][c];
	}
}

int build(int mask) {
	init();
	rept(i,n) {
		if ((mask&(1<<i)) > 0) {
			// cout<<"add "<<data[i]<<endl;
			add(data[i]);
		}
	}
	// printf("^^ %d %d\n",mask,cnt);
	return cnt;
}

pii getDyn(int mask, int m) {
	if (m==0 && mask!=0)
		return mp(0,0);
	if (mask==0)
		return mp(0,1);
	if (dyn[mask][m].X!=-1) {
		return dyn[mask][m];
	}
	int cur(0);
	int cnt(0);
	for (int s=mask; s!=0; s=((s-1)&mask)) {
		pii d(getDyn(mask^s,m-1));
		int nw(build(s)+d.X);
		int hv(d.Y);
		if (nw>cur) {
			cur=nw;
			cnt=hv;
		} else if (nw==cur) {
			cnt+=hv;
		}
	}
	dyn[mask][m]=mp(cur,cnt);
	// printf("%d %d %d %d\n",mask,m,dyn[mask][m].X,dyn[mask][m].Y);
	return dyn[mask][m];
}

void solvePart() {
	int m;
	scanf("%d%d\n",&n,&m);
	data.resize(n);
	rept(i,n)
		getline(cin,data[i]);
	MS(dyn,-1);
	pii res(getDyn((1<<n)-1,m));
	printf("%d %d\n",res.X, res.Y);
}

void solve() {
	int tst;
	scanf("%d",&tst);
	rept(t,tst) {
		cerr<<t<<endl;
		printf("Case #%d: ",t+1);
		solvePart();
	}
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	solve();
	return 0;
}
