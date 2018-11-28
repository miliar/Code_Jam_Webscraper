#include <stdio.h>
#include <stdlib.h>

using namespace std;

int cnt = 0;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);	
	while(t--){
		printf("Case #%d: ", ++cnt);	
		int row1, row2;
		int g1[5][5], g2[5][5];
		scanf("%d", &row1);
		for(int i=1; i<=4; ++i){
			for(int j=1; j<=4; ++j){
				scanf("%d", &g1[i][j]);	
			}
		}
		scanf("%d", &row2);
		for(int i=1; i<=4; ++i){
			for(int j=1; j<=4; ++j){
				scanf("%d", &g2[i][j]);	
			}
		}

		int res = 0;
		int val = 0;
		for(int i=1; i<=4; ++i){
			for(int j=1; j<=4; ++j){
				//printf("--- %d %d\n", g1[row1][i], g2[row2][j]); 
				if(g1[row1][i] == g2[row2][j]){
					++res;
					val = g1[row1][i];
				}	
			}	
		}
		if(res == 0){
			printf("Volunteer cheated!\n");	
		}else if(res == 1){
			printf("%d\n", val);	
		}else{
			printf("Bad magician!\n");	
		}
	}
	return 0;
}
