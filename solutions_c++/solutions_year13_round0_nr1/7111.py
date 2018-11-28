#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int T, status, countX, countO, countT;
	char arr[5][5], player;
	scanf("%d", &T);

	for(int z=1; z<=T; z++) {
		status = 0;

		for(int i=0; i<4; i++) {
			scanf("%s", arr[i]);
		}

		for(int i=0; i<4; i++) {
			int j;
			for(j=0; j<4; j++) {
				if(arr[i][j] == '.') {
					status = 3;
					break;
				}
				status = 4;
			}
			if(arr[i][j] == '.') {
				status = 3;
				break;
			}
		}


		/* checking the diagonals */
			/* main diagonal */
		countX = countO = countT = 0;
		for(int i=0; i<4; i++) {
			switch(arr[i][i]) {
				case 'X': countX++; break;
				case 'O': countO++; break;
				case 'T': countT++; break;
				default: break;
			}
		}
		if(countX == 4 || (countX == 3 && countT == 1))
			status = 1;
		else if(countO == 4 || (countO == 3 && countT == 1))
			status = 2;

		/* slave diagonal */
		countX = countO = countT = 0;
		for(int i=0; i<4; i++) {
			switch(arr[i][3-i]) {
				case 'X': countX++; break;
				case 'O': countO++; break;
				case 'T': countT++; break;
				default: break;
			}
		}
		if(countX == 4 || (countX == 3 && countT == 1))
			status = 1;
		else if(countO == 4 || (countO == 3 && countT == 1))
			status = 2;

		/* other rows and columns */
		for(int i=0; i<4; i++) {
			/* rows */
			countX = countO = countT = 0;
			for(int j=0; j<4; j++) {
				switch(arr[i][j]) {
					case 'X': countX++; break;
					case 'O': countO++; break;
					case 'T': countT++; break;
					default: break;
				}
			}
			if(countX == 4 || (countX == 3 && countT == 1)) {
				status = 1;
				break;
			}
			else if(countO == 4 || (countO == 3 && countT == 1)) {
				status = 2;
				break;
			}

			/* columns */
			countX = countO = countT = 0;
			for(int j=0; j<4; j++) {
				switch(arr[j][i]) {
					case 'X': countX++; break;
					case 'O': countO++; break;
					case 'T': countT++; break;
					default: break;
				}
			}
			if(countX == 4 || (countX == 3 && countT == 1)) {
				status = 1;
				break;
			}
			else if(countO == 4 || (countO == 3 && countT == 1)) {
				status = 2;
				break;
			}
		}

		switch(status) {
			case 1:
				printf("Case #%d: X won\n", z);
				break;
			case 2:
				printf("Case #%d: O won\n", z);
				break;
			case 3:
				printf("Case #%d: Game has not completed\n", z);
				break;
			case 4:
				printf("Case #%d: Draw\n", z);
				break;
		}
	}
}