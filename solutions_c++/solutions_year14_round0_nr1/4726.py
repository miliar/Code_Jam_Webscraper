#include <iostream>

using namespace std;

void solve() {
	int i, j;
	int a1, a2;
	int field1[4][4], field2[4][4];
	
	cin >> a1;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			cin >> field1[i][j];
		}
	}
	cin >> a2;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			cin >> field2[i][j];
		}
	}
	
	a1--;
	a2--;
	int answer;
	int counter = 0;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (field1[a1][i] == field2[a2][j]) {
				answer = field1[a1][i];
				counter++;
				break;
			}
		}
	}
	
	//cout << counter;
	
	if (counter == 0) {
		cout << "Volunteer cheated!";
	} else if (counter == 1) {
		cout << answer;
	} else {
		cout << "Bad magician!";
	}
}

int main() {
	int cases;
	int i = 1;
	
	cin >> cases;
	while (cases--) {
		cout << "Case #" << i << ": ";
		solve();
		i++;
		cout << endl;
	}
	
	return 0;
}