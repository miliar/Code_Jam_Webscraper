#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int inf=1000000000;
struct edge{
	int t,next,v,rev;
}g[1000001];
FILE *of;
bool b[511][511];
int flow,i,j,k,n,m,tot,tb,h[110001],dis[110001],s,t,x1,x2,y1,y2,tests,cc,p[511][511],q[110001],l[110001];
void addedge(int x,int y,int z){
	//printf("%d %d %d\n",x,y,z);
	g[++tot].t=y;g[tot].next=h[x];h[x]=tot;g[tot].v=z;g[tot].rev=tot+1;
	g[++tot].t=x;g[tot].next=h[y];h[y]=tot;g[tot].v=0;g[tot].rev=tot-1;
}
bool bfs(){
	int i,j,l,r;
	for (i=1;i<=t;i++) dis[i]=-1;
	dis[s]=1;q[1]=s;l=0;r=1;
	while (l<r){
		j=q[++l];
		for (i=h[j];i;i=g[i].next)
		 if (g[i].v&&dis[g[i].t]==-1){
		 	dis[g[i].t]=dis[j]+1;q[++r]=g[i].t;
		 	if (g[i].t==t) return 1;
		 }
	}
	return 0;
}
int work(int x,int low){
	if (x==t) return low;
	int i,res=0,k;
	//printf("%d %d\n",x,dis[x]);
	for (i=l[x];i&&low;i=g[i].next)
	 if (g[i].v&&dis[g[i].t]==dis[x]+1&&l[g[i].t]){
	 	k=work(g[i].t,min(low,g[i].v));
	 	res+=k;low-=k;g[i].v-=k;g[g[i].rev].v+=k;
	 	if (low) l[x]=i;
	 }
	return res;
}
int main(){
	scanf("%d",&tests);of=fopen("CS0bf.out","w");
	for (cc=1;cc<=tests;cc++){
		scanf("%d%d%d",&m,&n,&tb);s=2*n*m+1;t=s+1;tot=0;memset(h,0,sizeof(h));
		memset(b,0,sizeof(b));
		for (i=1;i<=n;i++)
		 for (j=1;j<=m;j++) p[i][j]=(i-1)*m+j;
		for (i=1;i<=tb;i++){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);x1++;x2++;y1++;y2++;
			for (j=x1;j<=x2;j++)
			 for (k=y1;k<=y2;k++) b[k][j]=1;
		}
		for (i=1;i<=m;i++){
			if (!b[1][i]) addedge(s,2*p[1][i]-1,1);
			if (!b[n][i]) addedge(2*p[n][i],t,1);
		}
		for (i=1;i<=n;i++)
		 for (j=1;j<=m;j++){
		 	if (!b[i][j]) addedge(2*p[i][j]-1,2*p[i][j],1);
		 	if (i<n&&!b[i][j]&&!b[i+1][j]) addedge(2*p[i][j],2*p[i+1][j]-1,1),addedge(2*p[i+1][j],2*p[i][j]-1,1);
		 	if (j<m&&!b[i][j]&&!b[i][j+1]) addedge(2*p[i][j],2*p[i][j+1]-1,1),addedge(2*p[i][j+1],2*p[i][j]-1,1);
		 }
		for (flow=0;bfs();){
			//printf("%d\n",flow);
			for (i=1;i<=t;i++) l[i]=h[i];
			flow+=work(s,inf);
		}
		fprintf(of,"Case #%d: %d\n",cc,flow);
		printf("%d\n",cc);
	}
	return 0;
}
