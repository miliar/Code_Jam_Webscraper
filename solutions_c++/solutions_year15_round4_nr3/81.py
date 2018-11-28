#include<bits/stdc++.h>
#define int64 long long
#define sqr(x) (x)*(x)
#define mk make_pair
#define pb push_back
#define fi first
#define se second
#define rep(i,x,y) for(int i=(x);i<=(y);++i)
#define VI vector<int>
#define VI64 vector<int64>
#define VS vector<string>
#define PII pair<int,int>
#define PDD pair<double,double>
#define VPII vector< PII >
#define SZ(x) ((int)(x).size())
#define N 1320
using namespace std;
const double pi=acos(-1);
map<string,int> M;
const int inf=100000;
struct Flow{
	#define maxn 10200
	#define maxm 120000
	
	int Next[maxm],e[maxm],c[maxm],head[maxn],dis[maxn],bfs[maxn],len,s,t;
	
	#undef maxn
	#undef maxm
	Flow(){
		len=1;
	}
	void reset(int source,int sink){
		memset(head,0,sizeof(head));
		s=source; t=sink;
		len=1;
	}
	void addedge(int x,int y,int k){
		Next[++len]=head[x]; head[x]=len; e[len]=y; c[len]=k;
		Next[++len]=head[y]; head[y]=len; e[len]=x; c[len]=0;
	}
	bool build(){
		int l,r,i,x;
		memset(dis,0,sizeof(dis));
		bfs[l=r=1]=s;
		dis[s]=1;
		while(l<=r){
			x=bfs[l];
			for(i=head[x];i;i=Next[i]) if(c[i]&&!dis[e[i]]){
				dis[e[i]]=dis[x]+1;
				bfs[++r]=e[i];
			}
			l++;
		}
		return dis[t]!=0;
	}
	int dinic(int x,int v){
		int flow=0;
		if(x==t)return v;
		for(int i=head[x];i;i=Next[i])if(c[i] && dis[x]+1==dis[e[i]]){
			int ff=dinic(e[i],min(v-flow,c[i]));
			c[i]-=ff;
			c[i^1]+=ff;
			flow+=ff;
			if(flow==v)return flow;
		}
		dis[x]=-1;
		return flow;
	}
	int maxflow(){
		int ans=0;
		while(build())ans+=dinic(s,inf);
		return ans;
	}
}Flow;
int cnt,num[N];
int a[N][N],T,tim,n;
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	for(scanf("%d",&T);T--;){
		scanf("%d",&n);
		M.clear();
		cnt=0;
		rep(i,1,n){
			string s;
			num[i]=0;
			for(;;){
				cin>>s;
				if(!M[s])M[s]=++cnt;
				a[i][++num[i]]=M[s];
				char c=getchar();
				if(c=='\n' || c==EOF)break;
			}
		}
		int s=0,t=1;
		Flow.reset(s,t);
		Flow.addedge(s,2,inf);
		Flow.addedge(3,t,inf);
		rep(i,3,n)Flow.addedge(s,i+1,inf),Flow.addedge(i+1,t,inf);
		rep(i,1,cnt)
			Flow.addedge(i+n+1,i+n+1+cnt,1);
		rep(i,1,n)
			rep(j,1,num[i]){
				int u=a[i][j]+n+1,v=u+cnt;
				Flow.addedge(i+1,u,inf);
				Flow.addedge(v,i+1,inf);
			}
		printf("Case #%d: %d\n",++tim,Flow.maxflow()%inf);
	}
}

