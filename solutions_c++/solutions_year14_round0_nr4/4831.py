#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int T,TT,n;
double t1[1001],t2[1001];
int g[2010][2010],m;
int chk[2010];
int a,b;

bool dfs(int v){
	if(v==m)return 1;
	chk[v]=1;
	for(int i=0;i<=m;i++)
		if(g[v][i]&&!chk[i]&&dfs(i)){
			g[v][i]=0;
			g[i][v]=1;
			chk[v]=0;
			return 1;
		}
	chk[v]=0;
	return 0;
}

int main(){
	int i,j;
	scanf("%d",&TT);
	while(TT--){
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%lf",&t1[i]);
		for(i=0;i<n;i++)scanf("%lf",&t2[i]);
		sort(t1,t1+n);
		sort(t2,t2+n);
		m=2*n+1;
		
		memset(g,0,sizeof(g));
		for(i=0;i<n;i++)g[0][1+i]=1;
		for(i=0;i<n;i++)g[1+n+i][m]=1;
		for(i=0;i<n;i++)for(j=0;j<n;j++)
			g[1+i][1+n+j]=(t1[i]>t2[j]?1:0);
		for(a=0;dfs(0);a++);
		
		b=0;
		for(i=j=n-1;i>=0;i--){
			if(t1[i]>t2[j]){
				b++;
			}else{
				j--;
			}
		}
		
		printf("Case #%d: %d %d\n",++T,a,b);
	}
	return 0;
}