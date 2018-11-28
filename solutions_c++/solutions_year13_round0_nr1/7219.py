#include <cstdio>

char data[5][5];

bool isWon(char target) {

	for(int i=0; i<4; ++i) {

		bool allX=true;
		for(int j=0; j<4; ++j)
			if(data[i][j]!=target && data[i][j]!='T') {
				allX=false;
				break;
			}
		if(allX) return true;

		allX=true;
		for(int j=0; j<4; ++j)
			if(data[j][i]!=target && data[j][i]!='T') {
				allX=false;
				break;
			}
		if(allX) return true;

	}

	bool diagonalX=true;
	for(int i=0; i<4; ++i)
		if(data[i][i]!=target && data[i][i]!='T') {
			diagonalX=false;
			break;
		}
	if(diagonalX) return true;

	diagonalX=true;
	for(int i=0; i<4; ++i)
		if(data[i][3-i]!=target && data[i][3-i]!='T') {
			diagonalX=false;
			break;
		}
	if(diagonalX) return true;

	return false;

}

bool isCompleted() {

	for(int i=0; i<4; ++i) for(int j=0; j<4; ++j)
		if(data[i][j]=='.') return false;
	return true;

}

int main() {

	int T;

	scanf("%d", &T);
	for(int i=1; i<=T; ++i) {

		for(int j=0; j<4; ++j) scanf("%s", data[j]);
		
		printf("Case #%d: ", i);
		if(isWon('X')) printf("X won");
		else if(isWon('O')) printf("O won");
		else if(isCompleted()) printf("Draw");
		else printf("Game has not completed");
		printf("\n");

	}

	return 0;

}