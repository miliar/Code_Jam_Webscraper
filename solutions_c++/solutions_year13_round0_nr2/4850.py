#include<cstdio>
#include<algorithm>
using namespace std;

int col[150], row[150], grid[150][150];

int main(){
	int Z;
	scanf("%d",&Z);
	for(int Q = 1; Q<=Z; ++Q){
		int n,m;
		bool res = true;
		scanf("%d %d",&n, &m);
		for(int i = 1; i <= n; ++i){
			for(int j = 1; j <=m; ++j){
				col[j]=0;
				scanf("%d",&grid[i][j]);
			}
		}
		for(int i=1; i<=n; ++i){
			row[i]=0;
			for(int j=1; j<=m; ++j){
				col[j]=max(col[j],grid[i][j]);
				row[i]=max(row[i],grid[i][j]);
			}
		}
		for(int i = 1; i<=n; ++i)
			for(int j = 1; j<=m; ++j)
				if(grid[i][j]!=col[j] && grid[i][j]!=row[i])res = false;
		printf("Case #%d: %s\n",Q,(res)?"YES":"NO");
	}
	return 0;
}
