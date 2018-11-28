#include <cstdio>

char grid[10][10];

int check(int pos, char symbol, int line){
	int res=1;
	if(symbol=='.') return 0;
	switch(line){
		case 0:
			for(int i=0; res &&  i<4; i++){
				if(grid[pos][i] != 'T' && grid[pos][i] != symbol){
					res = 0;
				}
			}
		break;
		case 1:
			for(int i=0; res &&  i<4; i++){
				if(grid[i][pos] != 'T' && grid[i][pos] != symbol){
					res = 0;
				}
			}
		break;
		case 2:
			for(int i=0; res &&  i<4; i++){
				if(grid[i][i] != symbol && grid[i][i] != 'T'){
			//		printf("%c != %c\n",grid[i][i], symbol);
					res = 0;
				}
			}
		break;
		case 3:
			for(int i=0; res && i<4; i++){
				if(grid[3-i][i] != 'T' && grid[3-i][i] != symbol){
					res = 0;
				}
			}
		break;
		
	}
	return res;
}

int main(int argc, char *argv[]){
	int T;
	scanf("%d\n",&T);
	
	for(int cases=0; cases<T; cases++){
		for(int i=0; i<4; i++){
			scanf("%s\n",grid[i]);
		}
		int result=0;
			//printf("Checking diagonal %c\n",grid[0][0]);
		if(grid[0][0]=='T'){
			if(check(0, 'X', 2)){
				result = 'X';
			}else if(check(0, 'O', 2)){
				result = 'O';
			}
		}else if(check(0, grid[0][0], 2)){
			result = grid[0][0];
		}
		//printf("@@@%c@@@\n", result);
		if(!result && grid[3][0]=='T'){
			if(check(3, 'X', 3)){
				result = 'X';
			}else if(check(3, 'O', 3)){
				result = 'O';
			}
		}else if(!result && check(0, grid[3][0], 3)){
			result = grid[3][0];
		}
		
		for(int i=0; !result && i<4; i++){
			if(grid[i][0] == 'T'){
				if(check(i, 'X', 0)){
					result = 'X';
				}else if(check(i, 'O', 0)){
					result = 'O';
				}
			}else if(check(i, grid[i][0], 0)){
				result = grid[i][0];
				break;
			}
		}
		
		for(int i=0; !result && i<4; i++){
			if(grid[0][i] == 'T'){
				if(check(i, 'X', 1)){
					result = 'X';
				}else if(check(i, 'O', 1)){
					result = 'O';
				}
			}else if(check(i, grid[0][i], 1)){
				result = grid[0][i];
				break;
			}
		}
		int space=0;
		for(int i=0; !space && !result && i<4; i++){
			for(int j=0; !space && j<4; j++){
				if(grid[i][j]=='.'){
					space=1;
					result = ' ';
				}
			}
		}
		printf("Case #%d: ", cases+1);
		if(!result){
			printf("Draw\n");
		}else if(result == ' '){
			printf("Game has not completed\n");
		}else{
			printf("%c won\n",result);
		}
	}
	
}

