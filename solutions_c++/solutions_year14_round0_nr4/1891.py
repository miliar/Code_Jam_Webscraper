//made by kuailezhish
//gl && hf
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <stack>
#include <sstream>
#include <complex>
#include <cstring>
#include <ctime>
#define mem(a,b) memset(a,b,sizeof(a))
#define INF 0x3f3f3f3f
#define lINF 0x3f3f3f3f3f3f3f3fll
#define dINF 1e30
#define eps 1e-8
#define lld long long
#define sqr(x) ((x)*(x))
#define ab(x) (((x)>0) ? (x) : -(x))
#define PI 3.14159265358979323846
#define psl pair<sting,lld>
#define pll pair<lld,lld>
#define pii pair<int,int>
#define mp make_pair
#define er(i) (1ll<<(i))
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define cp complex<double>
#define here printf("!!!!!!!!\n");
#define foreach(it,v) for (__typeof((v).begin()) it = (v).begin(); it != (v).end(); it++)
#define upmin(a,b) {if ((a)>(b)) (a)=(b);}
#define upmax(a,b) {if ((a)<(b)) (a)=(b);}
#define upmod(a,b) (a)=((a)%(b)+(b))%(b)
#define equ(a,b) (fabs(a-b)<eps)
#define rin freopen("in.txt","r",stdin)
#define pout freopen("out.txt","w",stdout)
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;

#define maxn 2100

double a[maxn],b[maxn];
int ans1,ans2;
int n;

struct node{
	int ver,flow,next;
}edge[maxn*1000];
int adj[maxn],tot;
int dis[maxn],src,des;
int que[maxn];

void addedge(int u,int v,int flow){
	edge[tot].ver=v; edge[tot].flow=flow; edge[tot].next=adj[u]; adj[u]=tot++;
    edge[tot].ver=u; edge[tot].flow=0;	edge[tot].next=adj[v]; adj[v]=tot++;
}

int bfs(){                  //对距离进行标号
	int i,j,tem,y,head,tail,now;
	mem(dis,-1); que[head=1]=src; dis[src]=0;
	for (tail=head+1; head<tail; ){
		now=que[head++];
		for (j=adj[now]; j!=-1; j=edge[j].next){
			y=edge[j].ver;
			if (dis[y]==-1 && edge[j].flow>0){
				dis[y]=dis[now]+1; que[tail++]=y;
				if (dis[des]>=0) return 1;
			}
		}
	}
	return 0;
}

int dfs(int s,int exp){
	int i,j,tem,y,minf,tmpf=0;
	if (s==des) return exp;
	for (j=adj[s]; j!=-1; j=edge[j].next){
		y=edge[j].ver;
		if (dis[y]==dis[s]+1 && edge[j].flow>0 &&
			tmpf<exp && (minf=dfs(y,min(edge[j].flow,exp-tmpf)))){
				edge[j].flow-=minf; edge[j^1].flow+=minf;
				tmpf+=minf;
		}
	}
	if (tmpf==0) dis[s]=-1;
	return tmpf;
}

int dinic(){
	int ans=0,tem;
	while (bfs())
		while (tem=dfs(src,INF))
			ans+=tem;
	return ans;
}


int judge(int num){
    int i,j,tem;
    for (i=1; i<=num; i++)
        if (a[i+n-num]<=b[i]) return 0;
    return 1;
}

int main(){
    int i,j,tem,T,cas=0;
    rin; pout;
    scanf("%d",&T);
    while (T--){
        scanf("%d",&n);
        for (i=1; i<=n; i++) scanf("%lf",&a[i]);
        for (i=1; i<=n; i++) scanf("%lf",&b[i]);
        sort(a+1,a+1+n);
        sort(b+1,b+1+n);
        int low,high,mid;
        low=0; high=n;
        while (low<=high){
            mid=(low+high)/2;
            if (judge(mid)){
                ans1=mid;
                low=mid+1;
            }else high=mid-1;
        }

        mem(adj,-1); tot=0;
        src=0; des=2*n+1;
        for (i=1; i<=n; i++){
            addedge(src,i,1);
            addedge(n+i,des,1);
            for (j=1; j<=n; j++)
                if (a[i]<b[j]) addedge(i,n+j,1);
        }
        ans2=n-dinic();
        printf("Case #%d: %d %d\n",++cas,ans1,ans2);
    }
    return 0;
} 















