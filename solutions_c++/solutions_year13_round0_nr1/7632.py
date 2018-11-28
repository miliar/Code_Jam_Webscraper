#include <stdio.h>

void main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int result = 0;
	int board[4][4];
	char s[10];
	int bit = 0;
	int ntest = 0;
	scanf("%d", &ntest); gets(s);
	for(int test = 0; test < ntest; test++) {
		for(int j = 0; j < 4; j++) {
			gets(s);
			for(int k = 0; s[k]; k++) {
				if(s[k] == 'T')
					board[j][k] = 0;
				else if(s[k] == 'X')
					board[j][k] = 1;
				else if(s[k] == 'O')
					board[j][k] = 2;
				else {
					bit = 1;
					board[j][k] = 4;
				}	
			}
		}

		for(int i = 0; i < 4; i++) {
			result = board[i][0]|board[i][1]|board[i][2]|board[i][3];
			if(result == 1 || result == 2)
				goto end;
		}
		for(int i = 0; i < 4; i++) {
			result = board[0][i]|board[1][i]|board[2][i]|board[3][i];
			if(result == 1 || result == 2)
				goto end;
		}
		result = board[0][0]|board[1][1]|board[2][2]|board[3][3];
		if(result == 1 || result == 2)
				goto end;

		result = board[0][3]|board[1][2]|board[2][1]|board[3][0];
		if(result == 1 || result == 2)
				goto end;
end:
		if(result == 1)
			printf("Case #%d: X won\n", test + 1);
		else if(result == 2)
			printf("Case #%d: O won\n", test + 1);
		else {
			if(bit == 0)
				printf("Case #%d: Draw\n", test + 1);
			else
				printf("Case #%d: Game has not completed\n", test + 1);
		}
		bit = 0; 
			
		gets(s);
	}
}
