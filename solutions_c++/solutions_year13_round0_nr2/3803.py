#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define rep(i,st,ed) for (int i=st; i<ed; i++)
#define foreach(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)

const int MAXN=128;
const int INF=0x3f3f3f3f;
const double eps=1e-8;

int n,m,ca;
int a[MAXN][MAXN];

void init(){
	cin>>n>>m;
	rep(i,0,n) rep(j,0,m) cin>>a[i][j];
}

bool ok(int x, int y){
	int retx=0,rety=0;
	rep(i,0,m) retx=max(retx,a[x][i]);
	rep(i,0,n) rety=max(rety,a[i][y]);
	return retx==a[x][y] || rety==a[x][y];
}

void solve(){
	rep(i,1,n-1) rep(j,1,m-1) if (!ok(i,j)){
		cout<<"NO"<<endl;
		return;
	}
	cout<<"YES"<<endl;
}

int main(){
	freopen("B.out","w",stdout);
	cin>>ca;
	rep(i,0,ca){
		cout<<"Case #"<<i+1<<": ";
		init();
		solve();
	}
	return 0;
}
