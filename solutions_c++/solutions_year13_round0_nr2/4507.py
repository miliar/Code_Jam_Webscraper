#include<stdio.h>
#include<stdlib.h>
int board[121][121];
int N, M;
int check(int x,int y){
	int flag = 1;
	for(int i=0;i < N ; i++){
		if(board[i][y] > board[x][y]){
			flag = 0;
			break;
		}
	}
	if(flag == 1)return 1;
	flag = 1;
	for(int j=0;j<M;j++){
		if(board[x][j] > board[x][y]){
			flag = 0;
			break;
		}
	}
	if(flag == 1)return 1;
	return 0;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int ca = 0; ca < T; ca++){
		printf("Case #%d: ", ca+1);
		scanf("%d %d",&N, &M);
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				int a = scanf("%d",&board[i][j]);
				if(a != 1){
					fprintf(stderr, "Warning: empty![a = %d]\n", a);
				}
			}
		}

		int result = 1;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				if(check(i,j) == 0){
					result = 0;
					break;
				}
			}
			if(result == 0)break;
		}
		if(result == 1){
			printf("YES\n");
		}else{
			printf("NO\n");
		}
	}
	return 0;
}
