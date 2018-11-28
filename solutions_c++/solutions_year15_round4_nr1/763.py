#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;


const int MAXN=111;
char grid[MAXN][MAXN];
int zm[MAXN][MAXN];
int zle[MAXN][MAXN];

main(){
	int test;scanf("%d",&test);
	for(int tnu=1;tnu<=test;tnu++){
		int n,m;scanf("%d%d",&n,&m);
		for(int i=1;i<=n;i++){
			scanf("%s",grid[i]+1);
		}
		for(int i=1;i<=n;i++){
			for(int j=1;j<=m;j++){
				if(grid[i][j]!='.'){
					zle[i][j]++;
					if(grid[i][j]=='<') zm[i][j]++;
					break;
				}
			}
			for(int j=m;j>0;j--){
				if(grid[i][j]!='.'){
					zle[i][j]++;
					if(grid[i][j]=='>') zm[i][j]++;
					break;
				}
			}
		}
		for(int j=1;j<=m;j++){
			for(int i=1;i<=n;i++){
				if(grid[i][j]!='.'){
					zle[i][j]++;
					if(grid[i][j]=='^') zm[i][j]++;
					break;
				}
			}
			for(int i=n;i>0;i--){
				if(grid[i][j]!='.'){
					zle[i][j]++;
					if(grid[i][j]=='v') zm[i][j]++;
					break;
				}
			}
		}
		int wyn=0;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=m;j++){
				//printf("%d %d %c %d %d\n",i,j,grid[i][j],zle[i][j],zm[i][j]);
				if(zle[i][j]==4) wyn=-1000111;
				if(zm[i][j]>0) wyn++;
				zm[i][j]=zle[i][j]=0;
			}
		}
		printf("Case #%d: ",tnu);
		if(wyn<0) puts("IMPOSSIBLE");
		else printf("%d\n",wyn);
	}
}
		
		

