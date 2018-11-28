#include <iostream>

using namespace std;

int main() {
	int T, C = 1, ans1, ans2;
	int matriz1[5][5], matriz2[5][5], encuentra[17];
	cin >> T;
	while (T--) {
		for (int i = 1; i <= 16; i++) encuentra[i] = 0;
		cout << "Case #" << C++ << ": ";
		cin >> ans1;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				cin >> matriz1[i][j];
		
		cin >> ans2;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				cin >> matriz2[i][j];
		

		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) 
				if ( matriz1[ans1][i] == matriz2[ans2][j] ) 
					encuentra[matriz1[ans1][i]]++;
					
		int c = 0;
		for (int i = 1; i <= 4; i++)
			if (encuentra[matriz1[ans1][i]])
				c++;
		if (c == 0) {
			cout << "Volunteer cheated!" << endl;
		} else if (c == 1) {
			for (int i = 1; i <= 4; i++) {
				if (encuentra[matriz1[ans1][i]]) {
					cout << matriz1[ans1][i] << endl;
				}
			}
		} else {
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}
