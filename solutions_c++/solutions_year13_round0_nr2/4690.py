#include<stdio.h>
#include<cstring>
using namespace std;
int g[100][100];
int f[100][100];
int T,n,m;
int main(){
	int i,j,k;
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	scanf("%d",&T);
	for(int p=1;p<=T;p++){
		printf("Case #%d: ",p);
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&f[i][j]),g[i][j]=100;
		int maxx;
		for(i=0;i<n;i++){
			maxx=0;
			for(j=0;j<m;j++)
				maxx=f[i][j]>maxx?f[i][j]:maxx;
			for(j=0;j<m;j++)
				g[i][j]=g[i][j]<maxx?g[i][j]:maxx;
		}
		for(i=0;i<m;i++){
			maxx=0;
			for(j=0;j<n;j++)
				maxx=f[j][i]>maxx?f[j][i]:maxx;
			for(j=0;j<n;j++)
				g[j][i]=g[j][i]<maxx?g[j][i]:maxx;
		}
		//
		bool flag=true;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(f[i][j]!=g[i][j]) flag=false;
		if(flag)
			puts("YES");
		else
			puts("NO");
	}
	scanf("%d",&n);
}
