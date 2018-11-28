#include<iostream>
#include<cstdio>

using namespace std;

int grid[101][101];
int rowMax[101];
int colMax[101];

int main(){
	int t,kase=1,n,m,i,j,rMax,cMax;
	bool possible=true;
	scanf("%d",&t);
	while(t--){
		possible = true;
		rMax = 0;
		cMax = 0;
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&grid[i][j]);
		for(i=0;i<n;i++){
			rMax=0;
			for(j=0;j<m;j++){
				rMax = max(rMax, grid[i][j]);
			}
			rowMax[i]=rMax;
		}
		for(i=0;i<m;i++){
			cMax=0;
			for(j=0;j<n;j++){
				cMax = max(cMax, grid[j][i]);
			}
			colMax[i]=cMax;
		}
		for(i=0;i<n && possible;i++)
			for(j=0;j<m && possible;j++){
				if(!(grid[i][j]==rowMax[i] || grid[i][j]==colMax[j])){
					possible = false;
				}
			}
		printf("Case #%d: %s\n",kase++, possible?"YES":"NO");
	}
	return 0;
}
