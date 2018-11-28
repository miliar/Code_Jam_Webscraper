#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define fi first
#define se second
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PII;
const ll mod=1000000007;
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// head

const int inf=0x20202020;
typedef int flowt;
namespace flow {
	const int M=1000000,N=10000;
	int y[M],nxt[M],gap[N],fst[N],c[N],pre[N],q[N],dis[N];
	flowt f[M];
	int S,T,tot,Tn;
	void init(int s,int t,int tn) {
		tot=1; assert(tn<N);
		rep(i,0,tn) fst[i]=0;
		S=s;T=t;Tn=tn;
	}
	void add(int u,int v,flowt c1,flowt c2=0) {
//		printf("%d %d %d\n",u,v,c1);
		tot++;y[tot]=v;f[tot]=c1;nxt[tot]=fst[u];fst[u]=tot;
		tot++;y[tot]=u;f[tot]=c2;nxt[tot]=fst[v];fst[v]=tot;
	}
	flowt sap() {
		int u=S,t=1;flowt flow=0;
		rep(i,0,Tn) c[i]=fst[i],dis[i]=Tn,gap[i]=0;
		q[0]=T;dis[T]=0;pre[S]=0;
		rep(i,0,t) {
			int u=q[i];
			for (int j=fst[u];j;j=nxt[j]) if (dis[y[j]]>dis[u]+1&&f[j^1]) 
				q[t++]=y[j],dis[y[j]]=dis[u]+1;
		}
		rep(i,0,Tn) gap[dis[i]]++;
		while (dis[S]<=Tn) {
			while (c[u]&&(!f[c[u]]||dis[y[c[u]]]+1!=dis[u])) c[u]=nxt[c[u]];
			if (c[u]) {
				pre[y[c[u]]]=c[u]^1;
				u=y[c[u]];
				if (u==T) {
					flowt minf=inf;
					for (int p=pre[T];p;p=pre[y[p]]) minf=min(minf,f[p^1]);
					for (int p=pre[T];p;p=pre[y[p]]) f[p^1]-=minf,f[p]+=minf;
					flow+=minf;u=S;
				}
			} else {
				if (!(--gap[dis[u]])) break;
				int mind=Tn;
				c[u]=fst[u];
				for (int j=fst[u];j;j=nxt[j]) if (f[j]&&dis[y[j]]<mind) 
					mind=dis[y[j]],c[u]=j;
				dis[u]=mind+1;
				gap[dis[u]]++;
				if (u!=S) u=y[pre[u]];
			}
		}
		return flow;
	}
};

char s[101000];
vector<string> seq[1010],eng,fra;
map<string,int> dict;
int _,n,cnt,__;
vector<string> readline() {
	gets(s);
	stringstream os; os<<s;
	string x;
	vector<string> p;
	while (os>>x) p.pb(x);
	for (auto s:p) if (!dict.count(s)) dict[s]=cnt++;
	return p;
}
int main() {
//	freopen("C.in","r",stdin);
	for (scanf("%d",&_);_;_--) {
		scanf("%d ",&n);
		dict.clear(); cnt=0;
		eng=readline();
		fra=readline();
		rep(i,2,n) seq[i-2]=readline();
		flow::init(2*cnt,2*cnt+1,2*cnt+2);
		rep(i,0,cnt) flow::add(i,i+cnt,1);
		for (auto s:eng) flow::add(2*cnt,dict[s],inf);
		for (auto s:fra) flow::add(dict[s]+cnt,2*cnt+1,inf);
		rep(i,0,n-2) rep(p,0,SZ(seq[i])) rep(q,p+1,SZ(seq[i])) {
			flow::add(dict[seq[i][p]]+cnt,dict[seq[i][q]],inf);			
			flow::add(dict[seq[i][q]]+cnt,dict[seq[i][p]],inf);			
		}
		printf("Case #%d: %d\n",++__,flow::sap());
	}
}
