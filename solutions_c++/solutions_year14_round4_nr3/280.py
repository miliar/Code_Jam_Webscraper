#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
#include <complex>
using namespace std;
#define rep(i,a,n) for (int i=a;i<(int)n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
#define ACCU accumulate
#define TWO(x) (1<<(x))
#define TWOL(x) (1ll<<(x))
#define clr(a) memset(a,0,sizeof(a))
#define POSIN(x,y) (0<=(x)&&(x)<n&&0<=(y)&&(y)<m)
#define PRINTC(x) cout<<"Case #"<<++__<<": "<<x<<endl 
#define POP(x) (__builtin_popcount(x))
#define POPL(x) (__builtin_popcountll(x))
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long ll;
typedef long double LD;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef vector<ll> VL;
typedef vector<PII> VPII;
typedef complex<double> CD;
const int inf=0x20202020;
const ll mod=1000000007;
const double eps=1e-9;
const double pi=3.1415926535897932384626;
const int DX[]={1,0,-1,0},DY[]={0,1,0,-1};
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll powmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}
// head

const int N=200,M=600;
int _,n,m,k,ans,__;
int col[N][M],vis[N][M],dis[N][M];
PII q[N*M*2];
int main() {
	for (scanf("%d",&_);_;_--) {
		scanf("%d%d%d",&n,&m,&k);
		rep(i,0,n) rep(j,0,m) col[i][j]=vis[i][j]=0;
		rep(i,0,k) {
			int x_0,x_1,y_0,y_1;
			scanf("%d%d%d%d",&x_0,&y_0,&x_1,&y_1);
			rep(x,x_0,x_1+1) rep(y,y_0,y_1+1) col[x][y]=1; 
		}
		int h=n*m,t=n*m;
		rep(i,0,m) if (col[0][i]) q[--h]=mp(0,i),dis[0][i]=0;
		else q[t++]=mp(0,i),dis[0][i]=1;
		rep(i,0,m) vis[0][i]=1;
		while (h<t) {
			int x=q[h].fi,y=q[h].se;
			++h;
			rep(dx,-1,2) rep(dy,-1,2) if (dx||dy) {
				int cx=x+dx,cy=y+dy;
				if (POSIN(cx,cy)&&!vis[cx][cy]) {
					vis[cx][cy]=1;
					if (col[cx][cy]) {
						dis[cx][cy]=dis[x][y];
						q[--h]=mp(cx,cy);
					} else {
						dis[cx][cy]=dis[x][y]+1;
						q[t++]=mp(cx,cy);
					}
				}
			}
		}
		ans=inf;
		rep(i,0,m) ans=min(ans,dis[n-1][i]);
		PRINTC(ans);
	}
}
