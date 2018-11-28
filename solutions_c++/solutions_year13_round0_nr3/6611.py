#include <cstdio>
#include <cstdlib>

using namespace std;

char grid[4][5];

void print(char c) {
	switch(c) {
		case 'X': printf("X won\n"); break;
		case 'O': printf("O won\n"); break;
		case 'D': printf("Draw\n"); break;
		case 'G': printf("Game has not completed\n"); break;
	}
}

char result() {
	char t;
	int c;
	bool empty=false;
	for(int i=0; i<4; i++) {
		// Horizontal solution
		t = grid[i][0] != 'T' ? grid[i][0] : grid[i][1]; c=0;
		for(int j=0; j<4; j++) {
			if(grid[i][j] == '.')
				empty=true;
			if(grid[i][j] == t || grid[i][j] == 'T')
				c++;
		}
		if(c == 4 && t != '.')
			return t;
		// Vertical solution
		t = grid[0][i] != 'T' ? grid[0][i] : grid[0][i]; c=0;
		for(int j=0; j<4; j++) {
			if(grid[j][i] == t || grid[j][i] == 'T')
				c++;
		}
		if(c == 4 && t != '.')
			return t;
	}
	// Left diagonal
	t = grid[0][0] != 'T' ? grid[0][0] : grid[1][1]; c=0;
	for(int i=0; i<4; i++) {
		if(grid[i][i] == t || grid[i][i] == 'T')
			c++;
	}
	if(c == 4 && t != '.')
		return t;
	// Right diagonal
	t = grid[0][3] != 'T' ? grid[0][3] : grid[1][2]; c=0;
	for(int i=0; i<4; i++) {
		if(grid[i][3-i] == t || grid[i][3-i] == 'T')
			c++;
	}
	if(c == 4 && t != '.')
		return t;
	if(empty)
		return 'G';
	else
		return 'D';
}

int input() {
	for(int i=0; i<4; i++) {
		scanf("%s", grid[i]);
	}
}

int main() {
	int t; 
	scanf("%d", &t);
	for(int i=1; i<=t; i++) {
		printf("Case #%d: ", i);
		input();
		print(result());
	}

	return 0;
}
