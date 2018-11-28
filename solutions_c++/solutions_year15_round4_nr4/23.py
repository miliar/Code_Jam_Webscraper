/*
Date: 2015/05/30 23:37:20 Saturday
Author: xllend3
*/
#include<bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define mp make_pair
#define ph push
#define pb push_back
#define REP(i,a,n) for(int _tmp=n,i=a;i<=_tmp;++i)
#define DEP(i,a,n) for(int _tmp=n,i=a;i>=_tmp;--i)
#define rep(i,a,n) for(int i=(a);i<=(n);++i)
#define dep(i,a,n) for(int i=(a);i>=(n);--i)
#define ALL(x,S) for(__typeof((S).end()) x=S.begin();x!=S.end();x++)
#define eps 1e-8
#define pi 3.1415926535897
#define sqr(x) ((x)*(x))
#define MAX(a,b) a=max(a,b)
#define MIN(a,b) a=min(a,b)
#define SZ(x) ((int)(x).size())
#define CPY(a,b) memcpy(a,b,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define POSIN(x,y) (1<=(x)&&(x)<=n&&1<=(y)&&(y)<=m)
#define all(x) (x).begin(),(x).end()
#define COUT(S,x) cout<<fixed<<setprecision(x)<<S<<endl
typedef long long ll;
typedef double lf;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<lf,lf> pff;
typedef complex<double> CD;
const int inf=0x20202020;
const int mod=1000000007;
template<class T> inline void read(T&x){bool fu=0;char c;for(c=getchar();c<=32;c=getchar());if(c=='-')fu=1,c=getchar();for(x=0;c>32;c=getchar())x=x*10+c-'0';if(fu)x=-x;};
template<class T> inline void read(T&x,T&y){read(x);read(y);}
template<class T> inline void read(T&x,T&y,T&z){read(x);read(y);read(z);}
template<class T> inline void read(T&x,T&y,T&z,T&q){read(x);read(y);read(z);read(q);}
const int DX[]={1,0,-1,0},DY[]={0,1,0,-1};
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll powmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}
//*******************************************

const int N=111,M=111111;
int l,m,n,t,C,cnt;
int a[N][N];
int comp(int x,int y){
	rep(i,1,n)rep(j,0,m-1)if(a[i][(x+j)%m+1]<a[i][(y+j)%m+1])return 1;
	else if(a[i][(x+j)%m+1]>a[i][(y+j)%m+1])return 0;return 0;
}
void dfs(int x,int y){
	if(x>n){
		rep(i,1,m)if((a[n][i]==a[n][i-1])+(a[n][i]==a[n][i+1])+(a[n][i]==a[n-1][i])!=a[n][i])return;
		rep(i,0,m-1)if(comp(i,0))return;
		//rep(i,1,n){rep(j,1,m)printf("%d",a[i][j]);puts("");}puts("");
		cnt++;return;
	}
	if(y>m){a[x][0]=a[x][m];a[x][m+1]=a[x][1];dfs(x+1,1);return;}
	rep(i,1,3){
		a[x][y]=i;
		if(x>1&&(a[x-1][y]==a[x-1][y+1])+(a[x-1][y]==a[x-1][y-1])+(a[x-1][y]==a[x][y])+(a[x-1][y]==a[x-2][y])
			!=a[x-1][y])continue;
		dfs(x,y+1);
	}
}
int main(){
	//ios::sync_with_stdio(false);
#ifdef LOCAL
	freopen("D.in","r",stdin);freopen("D.out","w",stdout);
#endif
	scanf("%d",&C);rep(_,1,C){
		printf("Case #%d: ",_);
		scanf("%d%d",&n,&m);
		cnt=0;
		dfs(1,1);
		printf("%d\n",cnt);
	}
	return 0;
}
