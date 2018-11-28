#include<cstdio>

int main(){
	int T;
	int cases=1;
	int row[2];
	int grid[2][10][10];
	int set[2][20];
	
	int row1, row2;
	
	scanf("%d\n",&T);
	
	while(T--){
		for(int k=0; k<2; k++){
			for(int i=0; i<20; i++){
				set[k][i] = 0;
			}
			scanf("%d\n", &row[k]);
			for(int i=0; i<4; i++){
				for(int j=0; j<4; j++){
					scanf("%d\n",&grid[k][i][j]);
					if(row[k]-1==i){
						set[k][grid[k][i][j]]=1;
					}
				}
			}
		}
		int c=0;
		int ans=-1;
		for(int i=0; i<=16; i++){
			if(set[0][i]+set[1][i]==2){
				c++;
				ans=i;
			}
		}
		printf("Case #%d: ",cases++);
		if(!c){
			printf("Volunteer cheated!\n");
		}else if(c==1){
			printf("%d\n",ans);
		}else{
			printf("Bad magician!\n");
		}
	}
	
	
	return 0;
}

