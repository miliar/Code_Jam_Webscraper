#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<map>
#include<vector>
#include<set>
#include<assert.h>
using namespace std;
#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RI64(x) scanf("%I64d",&(x))
#define RII64(x,y) scanf("%I64d%I64d",&(x),&(y))
#define RILL(x) scanf("%lld",&(x))
#define RIILL(x,y) scanf("%lld%lld",&(x),&(y))
#define FZ(i,n) for(int i=0;i<(n);i++)
#define PA(a,n) FZ(_1,n)printf("%d%c",(a)[_1],_1==(n)-1?10:32)
#define ePA(a,n) FZ(_2,n)fprintf(stderr,"%d%c",(a)[_2],_2==(n)-1?10:32)
#define SZ(x) ((int)x.size())
#define ALL(x) (x).begin(),(x).end()
#define pritnf printf
#define N 3000514
using namespace std;
typedef long long int lnt;
typedef double dou;
int n;
lnt D;
lnt As,Cs,Rs;
lnt Am,Cm,Rm;
lnt S[N],M[N];

int ord[N];
int cmp(int a,int b){
	return S[a]<S[b];
}
lnt up;
vector<int>e[N];
int inq[N];
int vis[N],vt;
void dfs1(int w){
	vis[w]=1;vt++;
	for(auto t:e[w]){
		if(vis[t]==0){
			if(up-D<=S[t]&&S[t]<=up){
				dfs1(t);
			}
			else if(S[t]>up){
				inq[t]=1;
			}
		}
	}
}
int vis2[N];
void dfs2(int w){
	vis2[w]=1;
	if(vis[w])vt--;
	for(auto t:e[w]){
		if(vis2[t]==0)dfs2(t);
	}
}
void sol(int uuu){
	RI(n);RI64(D);
	RII64(S[0],As);RII64(Cs,Rs);
	RII64(M[0],Am);RII64(Cm,Rm);
	FZ(i,n)if(i)S[i]=(S[i-1]*As+Cs)%Rs;
	FZ(i,n)if(i)M[i]=(M[i-1]*Am+Cm)%Rm;
	FZ(i,n)if(i)M[i]%=i;
	FZ(i,n)e[i].clear();
	FZ(i,n)if(i){
		e[M[i]].push_back(i);
	}
	FZ(i,n)ord[i]=i;
	sort(ord,ord+n,cmp);
	///
	FZ(i,n)inq[i]=vis[i]=vis2[i]=0;vt=0;
	up=S[0];
	dfs1(0);
	int ans=vt;
	int st=0,ed=0;
	for(;ed<n&&S[ord[ed]]<=up;ed++);
	for(up++;up<=min(1000514ll,S[0]+D);up++){
		for(;st<n&&S[ord[st]]<up-D;st++){
			if(vis2[ord[st]]==0)dfs2(ord[st]);
		}
		for(;ed<n&&S[ord[ed]]==up;ed++){
			int t=ord[ed];
			if(vis[t]==0&&vis2[t]==0&&inq[t])dfs1(ord[ed]);
		}
		ans=max(ans,vt);
	}
	pritnf("Case #%d: %d\n",uuu,ans);
}
int main(){
	//while(RI(n)!=EOF)sol(0);
	freopen("A-large.in","r",stdin);
	freopen("Al.txt","w",stdout);
	int t;
	if(RI(t)!=EOF){
		for(int ti=1;ti<=t;ti++)sol(ti);
	}
	return 0;
}

