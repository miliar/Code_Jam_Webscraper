#include <cstdio>

bool draw  = true;

int fromCharToInt(char a){
	switch(a)
	{
		case 'T':
			return 0;
		case 'O':
			return -1;
		case 'X':
			return 1;
		case '.':
			draw = false;
			return -50;
	}
	return 0;
}


int main(){
	char board[5][5];
	int kolumny[4];
	int wiersze[4];
	int TAB[2];
	int z;
	scanf("%d",&z);
	for (int k=1;k<=z;k++){
		draw = true;
		TAB[0] = 0;
		TAB[1] = 0;
		for (int i=0;i<4;i++){
			kolumny[i] = 0;
			wiersze[i] = 0;
			scanf("%s", board[i]);
		}
		
		for (int i=0;i<4;i++){
			for (int j=0;j<4;j++){
				int r = fromCharToInt(board[i][j]);
				kolumny[j] += r;
				wiersze[i] += r;
			}
		}
		
		
		for (int i=0;i<4;i++){
			if (kolumny[i]==4 || kolumny[i]==3) TAB[0] = 1;
			if (wiersze[i]==4 || wiersze[i]==3) TAB[0] = 1;
			if (kolumny[i]==-4 || kolumny[i]==-3) TAB[1] = 1;
			if (wiersze[i]==-4 || wiersze[i]==-3) TAB[1] = 1;
		}
		
		if (TAB[0]==0 && TAB[1]==0){
			if ((board[0][0]=='X' || board[0][0]=='T') &&
			(board[1][1]=='X' || board[1][1]=='T') &&
			(board[2][2]=='X' || board[2][2]=='T') &&
			(board[3][3]=='X' || board[3][3]=='T')) TAB[0] = 1;
			if ((board[0][0]=='O' || board[0][0]=='T') &&
			(board[1][1]=='O' || board[1][1]=='T') &&
			(board[2][2]=='O' || board[2][2]=='T') &&
			(board[3][3]=='O' || board[3][3]=='T')) TAB[1] = 1;
			if ((board[0][3]=='X' || board[0][3]=='T') &&
			(board[1][2]=='X' || board[1][2]=='T') &&
			(board[2][1]=='X' || board[2][1]=='T') &&
			(board[3][0]=='X' || board[3][0]=='T')) TAB[0] = 1;
			if ((board[0][3]=='O' || board[0][3]=='T') &&
			(board[1][2]=='O' || board[1][2]=='T') &&
			(board[2][1]=='O' || board[2][1]=='T') &&
			(board[3][0]=='O' || board[3][0]=='T')) TAB[1] = 1;
		}
		
		printf("Case #%d: ",k);
		if (TAB[0]==TAB[1]){
			if (draw) printf("Draw\n");
			else printf("Game has not completed\n");
		}
		else if (TAB[0]==1) printf("X won\n");
		else printf("O won\n");
	}
	return 0;
}
