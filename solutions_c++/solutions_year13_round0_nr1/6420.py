#include <stdio.h>
#include <iostream>

char board[20];

int check_row()
{
	int i,j;
	for(i=0; i<4; i++) {
		char c = board[i*4];
		if(c=='.') continue;
		if(c=='T') {
			c=board[i*4 + 1];
			if(c=='.') continue;
		}
		for(j=1; j<4; j++) {
			if(board[i*4 + j] != c && board[i*4 + j] != 'T')
				break;
		}
		if(j==4) {
			printf("%c won\n", c);
			return 1;
		}
	}
	return 0;
}

int check_col()
{
	int i,j;
	for(i=0; i<4; i++) {
		char c = board[i];
		if(c=='.') continue;
		if(c=='T') {
			c=board[4 + i];
			if(c=='.') continue;
		}
		if(c=='.') continue;
		for(j=1; j<4; j++) {
			if(board[j*4 + i] != c && board[j*4 + i] != 'T')
				break;
		}
		if(j==4) {
			printf("%c won\n", c);
			return 1;
		}
	}
	return 0;
}

int check_dia()
{
	int sum;
	if(board[0] != '.') {
		sum = 0;
		for(int i=0; i<4; i++) {
			sum += (int)board[i*4+i];
		}
		if(sum == 4*(int)board[0]) {
			printf("%c won\n", (char)(sum/4));
			return 1;
		}
		sum -= (int)'T';
		if(sum == 3*(int)'X' || sum == 3*(int)'O') {
			printf("%c won\n", (char)(sum/3));
			return 1;
		}
	}
	if(board[3] != '.') {
		sum = 0;
		for(int i=0; i<4; i++) {
			sum += (int)board[i*4+3-i];
		}
		if(sum == 4*(int)board[3]) {
			printf("%c won\n", (char)(sum/4));
			return 1;
		}
		sum -= (int)'T';
		if(sum == 3*(int)'X' || sum == 3*(int)'O') {
			printf("%c won\n", (char)(sum/3));
			return 1;
		}
	}
	return 0;
}

int main()
{
	int T;
	std::string str;
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		bool complete = true;
		getline(std::cin, str);
		for(int j=0; j<4; j++) {
			std::getline(std::cin, str);
			for(int k=0; k<4; k++) {
				board[j*4 + k] = str[k];
				if(str[k] == '.')
					complete = false;
			}
		}
		printf("Case #%d: ", i+1);
		if(check_row()) {
			continue;
		}
		if(check_col()) {
			continue;
		}
		if(check_dia()) {
			continue;
		}
		if(complete)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}
