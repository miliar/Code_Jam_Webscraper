#include <iostream>

using namespace std;

bool find(int A[], int x) {
	for (int i = 0; i < 4; i++) {
		if (A[i] == x)
			return true;
	}
	return false;
}

int main() {
	int T, n, i, j, tmp, ctr, result;
	int row[4];
	cin >> T;
	for (i = 0; i < T; i++) {
		ctr = 0;
		cin >> n;
		for (j = 0; j < 4*(n-1); j++)
			cin >> tmp;
		for (j = 0; j < 4; j++)
			cin >> row[j];
		for (j = 0; j < 4*(4-n); j++)
			cin >> tmp;
		cin >> n;
		for (j = 0; j < 4*(n-1); j++)
			cin >> tmp;
		for (j = 0; j < 4; j++) {
			cin >> tmp;
			if (find(row, tmp)) {
				ctr++;
				result = tmp;	
			}
		}
		for (j = 0; j < 4*(4-n); j++)
			cin >> tmp;
		if (ctr >= 2)
			cout << "Case #" << i+1 << ": Bad magician!" << endl;
		else if (ctr == 1)
			cout << "Case #" << i+1 << ": " << result << endl;
		else 
			cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
	}
	return 0;
}
