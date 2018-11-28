#include <stdio.h>

const int size = 16;
const int side = 4;

char finished(char *b, int i, int r) {
	int ini = r == 0 ? i : (r == 1? i*side : (r == 2 ? 3 : 0));
	int inc = r == 0 ? side : (r == 1? 1 : (r == 2 ? 3 : 5));
	
	char to, tx, tt;
	to = tx = tt = 0;
	for(int k=ini, j=0; j<side; ++j, k+=inc) {
		to += b[k] == 'O';
		tx += b[k] == 'X';
		tt += b[k] == 'T';
	}
	
	if(to+tt == 4 || tx+tt == 4) {
		return to ? 'O' : 'X';
	} else {
		return 0;
	}
}

int main() {
	int t; 
	
	char completed;
	char board[size+1];
	char res;	
	
	scanf("%d\n", &t);
	
	// iterate over number of cases
	for(int tt=1; tt<=t; ++tt) {
		completed = 1;
		res = 0;
		
		// read the board
		for(int n=0; n<size; ++n) {
			scanf("%c", &board[n]);			
			if(board[n] == '.') completed = 0;			
			if(n % 4 == 0 && n != 0) scanf("%c");
		}
		board[size] = 0;
		
		//printf("'%s'\n", board);
		printf("Case #%d: ", tt);
		
		// check the board 
		for(int k=0; k<=3; ++k) {
			for(int i=0; i<side; ++i) {
				res = finished(board, i, k);
				if(res) {
					printf("%c won\n", res);
					break;
				}
			}
			
			if(res) break;
		}
			
		if(!res) printf("%s\n", completed? "Draw" : "Game has not completed");
		scanf("\n");
	}
	
	return 0;
}