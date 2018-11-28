#include <stdio.h>

using namespace std;

void game();

int main(){
	int cases;

	scanf("%d", &cases);
	for(int i=0; i<cases; i++){
		printf("Case #%d: ", (i+1));
		game();
	}

	return 0;
}

void game(){
	char board[4][5], curr[2] = {'X', 'O'};
	bool free = false, t = false;
	int x, y;

	for(int i=0; i<4; i++){
		scanf("%s", board[i]);
		for(int j=0; j<4; j++){
			if(board[i][j]=='T'){
				t = true;
				x = i; 
				y = j;
			}
			if(board[i][j]=='.'){
				free = true;
			}
		}
	}

	for(int k=0; k<2; k++){
		if(t)
			board[x][y] = curr[k];
		
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(board[i][j]!=curr[k])
					break;
				if(j==3 && board[i][j]==curr[k]){
					printf("%c won\n", curr[k]);
					return;
				}
			}

			for(int j=0; j<4; j++){
				if(board[j][i]!=curr[k])
					break;
				if(j==3 && board[j][i]==curr[k]){
					printf("%c won\n", curr[k]);
					return;
				}
			}
		}

		for(int i=0; i<4; i++){
			if(board[i][i]!=curr[k])
				break;
			if(i==3 && board[i][i]==curr[k]){
				printf("%c won\n", curr[k]);
				return;
			}
		}

		for(int i=0; i<4; i++){
			if(board[i][3-i]!=curr[k])
				break;
			if(i==3 && board[i][3-i]==curr[k]){
				printf("%c won\n", curr[k]);
				return;
			}
		}
	}

	if(free){
		printf("Game has not completed\n");
	}else
		printf("Draw\n");
}
