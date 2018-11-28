#include <cstdio>
#include <algorithm>
using namespace std;

int main (){
	int t,n,m;
	int lawn[10][10];
	int row_max[10], col_max[10];
	scanf("%d",&t);
	for(int i=0; i<t; ++i){
		for(int j=0; j<10; ++j){
			row_max[j] = col_max[j] = -1;
		}
		scanf("%d %d",&n,&m);
		for(int j=0; j<n; ++j){
			for(int k=0; k<m; ++k){
				scanf("%d",lawn[j]+k);
				row_max[j] = max(row_max[j], lawn[j][k]);
				col_max[k] = max(col_max[k], lawn[j][k]);
			}
		}
		bool possible = true;
		for(int j=0; j<n; ++j){
			for(int k=0; k<m; ++k){
				if(lawn[j][k] < min(row_max[j] , col_max[k]) ){
					//printf("failure at pos (%d,%d)\n" , j+1, k+1);
					possible = false;
					break;
				}
			}
			if(!possible)
				break;
		}
		if(possible)
			printf("Case #%d: YES\n",i+1);
		else
			printf("Case #%d: NO\n",i+1);
	}
	return 0;
}
