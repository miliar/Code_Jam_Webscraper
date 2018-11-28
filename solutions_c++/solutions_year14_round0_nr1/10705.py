#include <stdio.h>

int main(){

	int tc;
	int p[4][4];
	int r;
	int v1[4];
	scanf("%d",&tc);
	int dmy;
	int tcc = 1;
	while(tc--){

		scanf("%d",&r);
		for(int i = 0 ; i<4 ; i++)
			for(int j = 0 ; j<4 ; j++)
				scanf("%d",&p[i][j]);
		for(int i = 0 ; i<4 ; i++)
			v1[i] = p[r-1][i];
		scanf("%d",&r);
		for(int i = 0 ; i<4 ; i++)
			for(int j = 0 ; j<4 ; j++)
				scanf("%d",&p[i][j]);
		int count = 0;
		int y;
		for(int i = 0 ; i<4 ; i++){
			for(int j = 0 ; j<4 ; j++){
				if(p[r-1][i] == v1[j]){
					count++;
					y = v1[j];
				}
			}
		}
		if(count==1){
			printf("Case #%d: %d\n",tcc++,y);
		}
		else if(count > 1){
			printf("Case #%d: Bad magician!\n",tcc++);	
		}
		else{
			printf("Case #%d: Volunteer cheated!\n",tcc++);	
		}

	}
	return 0;
}