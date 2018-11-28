#include <stdio.h>

int main(){
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; t++){
		char board[4][5];
		for(int i=0; i<4; i++)
			scanf(" %s", board[i]);
		int i, j, over = 0;
		for(i=0; i<4; i++){
			j = 0;
			while(j < 4 && board[i][j] == 'O' || board[i][j] == 'T'){
				j++;
			}
			if(j == 4){
				printf("Case #%d: O won\n", t+1);
				over = 1;
			}
			j = 0;
			while(j < 4 && board[i][j] == 'X' || board[i][j] == 'T'){
				j++;
			}
			if(j == 4){
				printf("Case #%d: X won\n", t+1);
				over = 1;
			}
		}
		for(j=0; j<4; j++){
			i = 0;
			while(i < 4 && board[i][j] == 'O' || board[i][j] == 'T'){
				i++;
			}
			if(i == 4){
				printf("Case #%d: O won\n", t+1);
				over = 1;
			}
			i = 0;
			while(i < 4 && board[i][j] == 'X' || board[i][j] == 'T'){
				i++;
			}
			if(i == 4){
				printf("Case #%d: X won\n", t+1);
				over = 1;
			}
		}
		i = 0;
		while(i < 4 && board[i][i] == 'O' || board[i][i] == 'T'){
			i++;
		}
		if(i == 4){
			printf("Case #%d: O won\n", t+1);
			over = 1;
		}
		i = 0;
		while(i < 4 && board[i][i] == 'X' || board[i][i] == 'T'){
			i++;
		}
		if(i == 4){
			printf("Case #%d: X won\n", t+1);
			over = 1;
		}
		i = 0;
		while(i < 4 && board[i][3-i] == 'O' || board[i][3-i] == 'T'){
			i++;
		}
		if(i == 4){
			printf("Case #%d: O won\n", t+1);
			over = 1;
		}
		i = 0;
		while(i < 4 && board[i][3-i] == 'X' || board[i][3-i] == 'T'){
			i++;
		}
		if(i == 4){
			printf("Case #%d: X won\n", t+1);
			over = 1;
		}
		if(over == 0){
			for(i=0; i<4; i++){
				for(j=0; j<4; j++)
					if(board[i][j] == '.'){
						printf("Case #%d: Game has not completed\n", t+1);
						over = 1;
						break;
					}
				if(over == 1)
					break;
			}
			if(over == 0)
				printf("Case #%d: Draw\n", t+1);
		}
	}
	return 0;
}
