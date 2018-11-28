/*
Date: 2016/05/28 22:55:17 Saturday
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

const int N=10,M=111111;
int l,m,n,t,C;
char s[N][N];
int a[N][N],b[N][N],p[N];
int check(){
	if(n==1)return a[1][1]==1;
	rep(i,1,n)p[i]=i;
	while(1){
		rep(_,1,n){
			int i=p[_];
			vector<int>cnt;
			rep(j,1,n)if(a[i][j])cnt.pb(j);
			if(_!=SZ(cnt)+1)continue;
			int bo=1;
			rep(j,1,_-1)if(!a[p[j]][cnt[j-1]])bo=0;
			if(bo)return 0;
		}
		if(!next_permutation(p+1,p+1+n))break;
	}return 1;
}
int main(){
	//ios::sync_with_stdio(false);
#ifdef LOCAL
	freopen("D.in","r",stdin);freopen("D.out","w",stdout);
#endif
	scanf("%d",&C);rep(_,1,C){
		scanf("%d",&n);rep(i,1,n){scanf("%s",s[i]+1);rep(j,1,n)b[i][j]=a[i][j]=s[i][j]-'0';}
		printf("Case #%d: ",_);
		int ans=inf;
		rep(msk,0,(1<<(n*n))-1){
			int bo=0,t=0,cnt=0;rep(i,1,n)rep(j,1,n)a[i][j]=b[i][j];
			rep(i,1,n)rep(j,1,n){
				if(msk>>t&1){
					if(a[i][j])bo=1;a[i][j]=1;++cnt;
				}++t;
			}if(bo)continue;
			if(check())MIN(ans,cnt);
		}printf("%d\n",ans);
	}
	return 0;
}
