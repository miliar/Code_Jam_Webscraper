/*
Date: 2015/05/30 22:33:38 Saturday
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

const int N=111111,M=1111111;
int l,m,n,t,C,tt;
char ss[N];
string s[N];
map<string,int>S;
vector<int>v[N];
int di[N],his[N],pre[N],b[N],dis[N],vh[N],tot;
struct zcc{int nxt,flw,v;}a[M];
int sap(){
    int u=1,now,aug=inf,flow=0;rep(i,1,n)di[i]=b[i],vh[i]=dis[i]=0;vh[0]=n;
    while(dis[1]<n){
        for(now=di[u];now;now=a[now].nxt)if(a[now].flw&&dis[u]==dis[a[now].v]+1)break;
        di[u]=now;his[u]=aug;
        if(now){
            MIN(aug,a[now].flw);pre[u=a[now].v]=now;
            if(u==n){
                do{a[pre[u]].flw-=aug;a[pre[u]^1].flw+=aug;u=a[pre[u]^1].v;}while(u-1);
                flow+=aug;aug=inf;
            }
        }else{
            if(--vh[dis[u]]==0)break;dis[u]=n+1;
            for(now=b[u];now;now=a[now].nxt)if(a[now].flw)MIN(dis[u],dis[a[now].v]+1);di[u]=b[u];
            ++vh[dis[u]];if(u-1){u=a[pre[u]^1].v;aug=his[u];}
        }
    }return flow;
}
void add(int x,int y,int z){
	a[++tot].v=y;a[tot].nxt=b[x];b[x]=tot;a[tot].flw=z;
	a[++tot].v=x;a[tot].nxt=b[y];b[y]=tot;a[tot].flw=0;
	//printf("%d %d %d\n",x,y,z);
}
string getstr(string &s){
	while(s[0]==' ')s.erase(0,1);
	string tmp="";while(s.size()&&s[0]!=' ')tmp.pb(s[0]),s.erase(0,1);return tmp;
}
int main(){
	//ios::sync_with_stdio(false);
#ifdef LOCAL
	freopen("C.in","r",stdin);freopen("C.out","w",stdout);
#endif
	scanf("%d",&C);rep(_,1,C){
		printf("Case #%d: ",_);
		rep(i,1,n)v[i].clear(),b[i]=0;
		tt=0;tot=1;S.clear();
		scanf("%d\n",&n);rep(i,1,n)gets(ss),s[i]=string(ss);
		//rep(i,1,n)printf("%d:%s\n",i,s[i].c_str());
		rep(i,1,n){
			string pt=s[i];while(SZ(pt)){
				string tmp=getstr(pt);if(!S[tmp])S[tmp]=++tt;v[i].pb(S[tmp]);
				//printf("%s_%s\n",pt.c_str(),tmp.c_str());
			}
		}
		/*
		rep(i,1,n){
			sort(v[i].begin(),v[i].end());
			int pt=0;
			rep(j,1,SZ(v[i])-1)if(v[i][j]!=v[i][pt])v[i][++pt]=v[i][j];
			while(SZ(v[i])>pt+1)v[i].pop_back();
			//rep(j,0,SZ(v[i])-1)printf("%d ",v[i][j]);puts("");
		}
		*/
		add(1,2,1000);add(3,n+tt+tt+2,1000);
		rep(i,3,n)add(1,i+1,1000),add(i+1,n+tt+tt+2,1000);
		rep(i,1,tt){
			add(n+i+1,n+i+tt+1,1);
			rep(j,1,n){
				int bo=0;rep(J,0,SZ(v[j])-1)if(v[j][J]==i){bo=1;break;}
				if(bo)add(j+1,n+i+1,inf),add(n+i+tt+1,j+1,inf);
			}
		}
		int sum=-1000*(n-2);
		n=n+tt+tt+2;
		printf("%d\n",sap()+sum);
	}
	return 0;
}
