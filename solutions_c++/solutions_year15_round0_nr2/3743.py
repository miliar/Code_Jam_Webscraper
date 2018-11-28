#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <list>
#include <queue>
using namespace std;

#define LL long long
#define V vector
#define VD V<double>
#define VI V<int>
#define VII V<VI>
#define FOR(t,l,r) for (int t=l; t<(int)r; t++)
#define FORL(t,l,r) for (LL t=l; t<(LL)r; t++)
#define max(x,y) ((x>y)?x:y)
#define min(x,y) ((x<y)?x:y)
#define abs(x) (((x)<0)?-(x):(x))
const double mth_pi=2*acos(0.);
#define pi mth_pi
#define inf (1<<23)
#define eps 1e-10
#define pb push_back
#define mp make_pair
#define sz size()
#define all(a) a.begin(),a.end()
#define mii map<int,int>
#define pii pair<int,int>
#define x first
#define y second
#define VL V<LL>
#define si set<int>
#define endl '\n'

//const int N=1000010;
//int lp[N+1]; VI pr;
//void resh () {
//	FOR(i,2,N+1) {
//		if (!lp[i]) lp[i]=i, pr.pb(i);
//		for (int j=0; j<pr.sz && pr[j]<=lp[i] && i*pr[j]<=N; ++j)
//			lp[i*pr[j]]=pr[j];
//	}
//}

//const int MN = 202;
//int z[MN], c[MN];
//V<VI> g;
//
//void dfs (int v, int k) {
//	z[v]=1, c[v]=k;
//	for (VI::iterator it=g[v].begin(); it!=g[v].end(); ++it)
//		if (!z[*it]) dfs (*it,k+1);
//}

int a[2002];

int main () {
	freopen("B-large.in","r",stdin);
	freopen("blarge.out","w",stdout);
	int T; cin >>T;
	FOR(tt,1,T+1) {
		int x, i, j, mx, mn, sum;
		cin >>x;
		FOR(i,0,x) cin >>a[i], mx=max(mx,a[i]);
		mn=mx;
		FOR(i,1,mx+1) {
			sum=i;
			FOR(j,0,x)
				if (a[j]>i) {
					sum+=a[j]/i;
					if (a[j]%i==0) sum--;
				}
			mn=min(mn,sum);
		}
		cout<<"Case #"<<tt<<": "<<mn<<endl;
	}
return 0;
}














