#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T,S,TT,TTT,n,m,x,y,x1,y1,x2,y2,mm;
int indx[110000],dep[110000],data[110000],now[110000],tot,i,j,k,ans;
bool f[110000],map[512][512];
const int bx[4]={1,-1,0,0};
const int by[4]={0,0,1,-1};
struct edge{
	int x,y,f,c,nxt;
}a[1100000];
int hash(int x,int y,int z){
	return 2*(x*m+y)+z;
}
void add(int x,int y,int z){
	a[++mm].x=x;a[mm].y=y;a[mm].c=z;a[mm].f=0;
	a[mm].nxt=indx[x];indx[x]=mm;
	a[++mm].x=y;a[mm].y=x;a[mm].c=0;a[mm].f=0;
	a[mm].nxt=indx[y];indx[y]=mm;
}
bool bfs(){
	int op,cl,k,j;
	memset(dep,0,sizeof(dep));memset(f,true,sizeof(f));
	data[1]=S;op=1;cl=2;f[S]=false;dep[S]=1;
	while(op<cl){
		k=data[op];op++;now[k]=indx[k];
		for(j=indx[k];j;j=a[j].nxt)
			if(a[j].c!=a[j].f&&f[a[j].y]){
				f[a[j].y]=false;data[cl]=a[j].y;cl++;dep[a[j].y]=dep[k]+1;
			}
	}
	return !f[T];
}
int dfs(int v,int flow){
	int c,increase,j,f;
	if(v==T)return flow;
	c=flow;f=0;
	for(j=now[v];j;j=a[j].nxt)
		if(a[j].c!=a[j].f&&dep[a[j].y]==dep[v]+1){
			increase=dfs(a[j].y,min(c,a[j].c-a[j].f));
			f+=increase;c-=increase;
			a[j].f+=increase;a[((j-1)^1)+1].f-=increase;
			if(c==0)break;
		}
	now[v]=j;
	return f;
}
bool out(int x,int y){
	if(x<=0||x>n||y<=0||y>m)return 1;
	return 0;
}
int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&TTT);
for(TT=1;TT<=TTT;TT++){
	printf("Case #%d: ",TT);
	scanf("%d%d%d",&m,&n,&tot);
	memset(map,0,sizeof(map));
	for(i=1;i<=tot;i++){
		scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
		x1++,y1++,x2++,y2++;
		if(x1>x2)swap(x1,x2);
		if(y1>y2)swap(y1,y2);
		for(x=x1;x<=x2;x++)
			for(y=y1;y<=y2;y++)map[x][y]=1;
	}
		S=0;
		mm=0;memset(indx,0,sizeof(indx));
		S=0;T=101000;
		for(i=1;i<=n;i++)for(j=1;j<=m;j++)if(map[i][j]==0){
			add(hash(i,j,1),hash(i,j,2),1);
			for(k=0;k<4;k++){
				x=i+bx[k];y=j+by[k];
				if(out(x,y)||map[x][y])continue;
				add(hash(i,j,2),hash(x,y,1),1);
			}
		}
		for(i=1;i<=m;i++){
			add(S,hash(1,i,1),1);
			add(hash(n,i,2),T,1);
		}
		ans=0;
		while(bfs())
			ans+=dfs(S,~0u>>1);
		printf("%d\n",ans);
	
}
}