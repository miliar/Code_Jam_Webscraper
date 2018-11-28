#include <iostream>
using namespace std;

int main() {
	int currentgame = 0, games, res, maybe_not_completed, done = 0;
	char x;
	int v[4][4];
	int verticalres[4], diagres[2];
	
	cin >> games;
	
	while (currentgame++ < games) {
		maybe_not_completed = done = 0;
		
		for (int i = 0; i < 4; i++) {
			verticalres[i] = 1;
		}
		
		for (int i = 0; i < 2; i++) {
			diagres[i] = 1;
		}
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> x;
				switch (x) {
					case 'X':
						v[i][j] = 2;
						break;
					case 'O':
						v[i][j] = 3;
						break;
					case '.':
						v[i][j] = 0;
						maybe_not_completed = 1;
						break;
					case 'T':
						v[i][j] = 5;
						break;
				} 
			}
		}
		
		for (int i = 0; i < 4 && !done; i++) {
			res = 1;
			for (int j = 0; j < 4; j++) {
				res *= v[i][j];
				verticalres[j] *= v[i][j];
				
				if (i == j)
					diagres[0] *= v[i][j];
				else if (i+j == 3) {
					//cout << "at " << i << j << endl;
					diagres[1] *= v[i][j];
					//cout << diagres[1] << endl;
				}
			}
			//res = v[i][0] * v[i][1] * v[i][2] * v[i][3];
			//cout << res << endl;

			if ((res == 40) || (res == 16)) {
				cout << "Case #" << currentgame << ": X won" << endl;
				done = 1;
			} else if ((res == 81) || (res == 135)) {
				cout << "Case #" << currentgame << ": O won" << endl;
				done = 1;
			}
		}
		
		if (!done) {
			for (int i = 0; i < 4; i++) {
				if ((verticalres[i] == 40) || (verticalres[i] == 16)) {
					cout << "Case #" << currentgame << ": X won" << endl;
					done = 1;
				} else if ((verticalres[i] == 81) || (verticalres[i] == 135)) {
					cout << "Case #" << currentgame << ": O won" << endl;
					done = 1;
				}
			}
		}
		
		if (!done) {
			for (int i = 0; i < 2; i++) {
				if ((diagres[i] == 40) || (diagres[i] == 16)) {
					cout << "Case #" << currentgame << ": X won" << endl;
					done = 1;
				} else if ((diagres[i] == 81) || (diagres[i] == 135)) {
					cout << "Case #" << currentgame << ": O won" << endl;
					done = 1;
				}
			}
		}
		
		
		if (!done) { 
			if (maybe_not_completed)
				cout << "Case #" << currentgame << ": Game has not completed" << endl;
			else 
				cout << "Case #" << currentgame << ": Draw" << endl;
		}
	}
	return 0;
}

