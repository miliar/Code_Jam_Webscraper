#include<stdio.h>

int main(){
	int testCases;
	scanf("%d",&testCases);
	for(int t=1;t<=testCases;t++){
		int N,M;
		scanf("%d%d",&N,&M);
		int arr[N][M];
		int maxRow[N];
		int maxCol[M];

		for(int i=0;i<N;i++)
			maxRow[i] = -1;
		for(int j=0;j<M;j++){
			maxCol[j] = -1;
		}

		for(int i=0;i<N;i++){

			for(int j=0;j<M;j++){
				scanf("%d",&arr[i][j]);
				if(maxRow[i] < arr[i][j]){
					maxRow[i] = arr[i][j];
				}			
				if(maxCol[j] < arr[i][j]){
					maxCol[j] = arr[i][j];
				}
			}
		}
		int pos = 1;


		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				
				if(arr[i][j] != maxRow[i] && arr[i][j] != maxCol[j]){
					pos = 0;
					break;
				}

			}
			if(!pos)break;
		}

		if(pos){
			printf("Case #%d: YES\n",t);
		}
		else{
			printf("Case #%d: NO\n",t);
		}

	}
}
