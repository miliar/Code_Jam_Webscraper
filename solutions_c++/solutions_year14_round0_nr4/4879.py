#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int cases,test_cases,blocks;
int grid[2010][2010],meta,check[2010],dwar,war;
double naomi[1001],ken[1001];

bool search(int varble){
	if(varble==meta)return 1;
	check[varble]=1;
	for(int i=0;i<=meta;i++)
		if(grid[varble][i]&&!check[i]&&search(i)){
			grid[varble][i]=0;
			grid[i][varble]=1;
			check[varble]=0;
			return 1;
		}
	check[varble]=0;
	return 0;
}

int main(){
	int i,j;
	scanf("%d",&test_cases);
	while(test_cases--){
		scanf("%d",&blocks);
		for(i=0;i<blocks;i++)scanf("%lf",&naomi[i]);
		for(i=0;i<blocks;i++)scanf("%lf",&ken[i]);
		sort(naomi,naomi+blocks);
		sort(ken,ken+blocks);
		meta=2*blocks+1;

		memset(grid,0,sizeof(grid));
		for(i=0;i<blocks;i++)grid[0][1+i]=1;
		for(i=0;i<blocks;i++)grid[1+blocks+i][meta]=1;
		for(i=0;i<blocks;i++)for(j=0;j<blocks;j++)
			grid[1+i][1+blocks+j]=(naomi[i]>ken[j]?1:0);
		for(dwar=0;search(0);dwar++);

		war=0;
		for(i=j=blocks-1;i>=0;i--){
			if(naomi[i]>ken[j]){
				war++;
			}else{
				j--;
			}
		}

		printf("Case #%d: %d %d\n",++cases,dwar,war);
	}
	return 0;
}
