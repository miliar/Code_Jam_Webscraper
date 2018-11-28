#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int n,m,K;
int map[6][6],b,c[6][6],d[6][6],f[100];
const int C[8]={1,1,1,0,0,-1,-1,-1};
const int D[8]={1,0,-1,1,-1,1,0,-1};

int find(int x){
	if (f[x]!=x) f[x]=find(f[x]);
	return f[x];
}

void can(){
	b=1;
	memcpy(c,d,sizeof(c));
}

void dfs(int x,int y,int k){
	if (b) return ;
	if (k>K) return ;
	if (x>n){
		if (k<K) return ;
		for (int i=1; i<=n; ++i)
			for (int j=1; j<=m; ++j)
				d[i][j]=map[i][j];
		if (n*m==k+1){
			for (int i=1; i<=n; ++i)
				for (int j=1; j<=m; ++j)
					if (d[i][j]==0) d[i][j]=3;
			can();
			return ;
		}
		for (int i=1; i<=n; ++i)
			for (int j=1; j<=m; ++j)
				if (d[i][j]==1)
					for (int l=0; l<8; ++l){
						int xx=i+C[l],yy=j+D[l];
						if (!xx || !yy || xx>n || yy>m)continue;
						if (d[xx][yy]==1) continue;
						d[xx][yy]=2;
					}
		for (int i=1; i<=n*m; ++i) f[i]=i;
		for (int i=1; i<=n; ++i)
			for (int j=1; j<=m; ++j){
				if (d[i][j]==1) continue;
				if (d[i][j]==2){
					int k=0;
					for (int l=0; l<8; ++l){
						int xx=i+C[l],yy=j+D[l];
						if (!xx || !yy || xx>n || yy>m) continue;
						if (d[xx][yy]==0) ++k;
					}
					if (!k) return ;
					continue;
				}
				for (int l=0; l<8; ++l){
					int xx=i+C[l],yy=j+D[l];
					if (!xx || !yy || xx>n || yy>m) continue;
					if (d[xx][yy]==0) f[find((i-1)*m+j)]=find((xx-1)*m+yy);
				}
			}
		int k=0;
		for (int i=1; i<=n; ++i)
			for (int j=1; j<=m; ++j)
				if (d[i][j]==0)
				if (find((i-1)*m+j)==(i-1)*m+j) {++k; d[i][j]=3;}
		if (k!=1) return ;
		can();
		return ;
	}
	int num=m-y+1;
	num+=(n-x)*m;
	if (k+num<K) return ;
	int xx=x,yy=y+1;
	if (yy>m) ++xx,yy=1;
	dfs(xx,yy,k);
	map[x][y]=1;
	dfs(xx,yy,k+1);
	map[x][y]=0;
}

int main(){
	freopen("1.txt","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int I=1; I<=T; ++I){
		scanf("%d%d%d",&n,&m,&K);
		b=0;
		memset(c,-1,sizeof(c));
		memset(map,0,sizeof(map));
		dfs(1,1,0);
		printf("Case #%d:\n",I);
		if (!b) puts("Impossible");
		else {
			for (int i=1; i<=n; ++i)
				for (int j=1; j<=m; ++j){
					if (c[i][j]==0 || c[i][j]==2) putchar('.');
					if (c[i][j]==1) putchar('*');
					if (c[i][j]==3) putchar('c');
					if (j==m) puts("");
				}
		}
	}
}
