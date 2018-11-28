#include <iostream>
#include <cstdio>
using namespace std;

#define BOARD_SIZE 4

char board[BOARD_SIZE + 5][BOARD_SIZE + 5];
int numTests;

char checkSequence(int incr1, int incr2, int start1, int start2) {
	int i = start1, j = start2; 
	char ret = board[i][j];
	if (ret == '.') return 'D'; 
	for (int k = 1; k < BOARD_SIZE; k++) {
		i += incr1, j += incr2;
		char cur = board[i][j];
		if (ret == 'T') ret = cur;
		if (cur == '.') return 'D';
		if (cur != ret && cur != 'T') return 'D'; 		
	}	
	//printf("%d,%d %d,%d winner %c\n",incr1,incr2,start1,start2,ret);
	return ret;
}

int main() {
	scanf("%d",&numTests);
	for (int tc = 1; tc <= numTests; tc++) {
		for (int i = 0; i < BOARD_SIZE; i++) scanf("%s",board[i]);
		bool gameEnded = true;
		for (int i = 0; i < BOARD_SIZE; i++)
			for (int j = 0; j < BOARD_SIZE; j++) {
				if (board[i][j] == '.') gameEnded = false;
			}
		char winner = 'D';	
		for (int i = 0; i < BOARD_SIZE; i++) {
			char ret = checkSequence(0,1,i,0);
			if (ret != 'D') {
				winner = ret;
			}
			ret = checkSequence(1,0,0,i);
			if (ret != 'D') {
				winner = ret;
			}
		}
		char ret = checkSequence(1,1,0,0);
		if (ret != 'D') {
			winner = ret;
		}
		ret = checkSequence(1,-1,0,BOARD_SIZE-1);
		if (ret != 'D') {
			winner = ret;
		}
		printf("Case #%d: ",tc);
		if (winner != 'D') {
			printf("%c won",winner);
		} else if (gameEnded) {
			printf("Draw");
		} else printf("Game has not completed");
		printf("\n");
	}
}