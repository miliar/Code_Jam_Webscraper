/*
Date: 2015/05/30 21:59:22 Saturday
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

const int N=1111,M=111111;
int l,m,n,t,C;
int a[N][N],dir[N];
int getc(){char c;for(c=getchar();c!='.'&&c!='v'&&c!='^'&&c!='>'&&c!='<';c=getchar());return c;}
int check(int x,int y,int z){
	while(1<=x&&x<=m&&1<=y&&y<=n){
		x+=DX[z];y+=DY[z];
		if(1<=x&&x<=m&&1<=y&&y<=n&&a[x][y]!='.')return 1;
	}return 0;
}
int main(){
	//ios::sync_with_stdio(false);
#ifdef LOCAL
	freopen("A.in","r",stdin);freopen("A.out","w",stdout);
#endif
	dir['^']=2;dir['v']=0;
	dir['<']=3;dir['>']=1;
	scanf("%d",&C);rep(_,1,C){
		printf("Case #%d: ",_);
		scanf("%d%d",&m,&n);rep(i,1,m)rep(j,1,n)a[i][j]=getc();
		int imp=0,res=0;
		//rep(i,1,m)rep(j,1,n)rep(k,0,3)printf("%d %d %d %d\n",i,j,k,check(i,j,k));
		rep(i,1,m)rep(j,1,n)if(a[i][j]!='.'){
			if(!check(i,j,dir[a[i][j]])){
				++res;if(!check(i,j,0)&&!check(i,j,1)&&!check(i,j,2)&&!check(i,j,3))imp=1;
			}
		}
		if(imp)puts("IMPOSSIBLE");
		else printf("%d\n",res);
	}
	return 0;
}
