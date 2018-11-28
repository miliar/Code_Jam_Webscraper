#include <fstream>
using namespace std;

int main() {
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	int T;
	cin >> T;
	for(int X = 0; X < T; X++) {
		int row[2], *options, cards[2][4][4], y = -1, i, j;
		cin >> row[0];
		row[0]--;
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				cin >> cards[0][i][j];
			}
		}
		cin >> row[1];
		row[1]--;
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				cin >> cards[1][i][j];
			}
		}
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				if(cards[0][row[0]][i] == cards[1][row[1]][j]) {
					y = (y == -1) ? cards[0][row[0]][i] : -2;
					break;
				}
			}
		}
		cout << "Case #" << (X + 1) << ": ";
		if(y > 0) {
			cout << y;
		} else if(y == -1) {
			cout << "Volunteer cheated!";
		} else {
			cout << "Bad magician!";
		}
		cout << "\n";
	}
	system("PAUSE");
	return 0;
}