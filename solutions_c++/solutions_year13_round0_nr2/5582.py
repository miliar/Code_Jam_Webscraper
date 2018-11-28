#include<iostream>
using namespace std;

class lawnMower {
private:
	int m, n;
	char row[10];
	char col[10];
	int input[10][10];
public:
	lawnMower(int x, int y) {
		this->m = x;
		this->n = y;
	}
	void getInput();
	bool solve();

};
bool lawnMower::solve() {
	bool hasTwo = false;
	bool hasOne = false;

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (input[i][j] == 2) {
				hasTwo = true;
			} else {
				hasOne = true;
			}
		}
		if (hasTwo && hasOne)
			row[i] = 'N';
		else
			row[i] = 'Y';

		hasTwo = false;
		hasOne = false;
	}
	hasTwo = false;
	hasOne = false;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (input[j][i] == 2) {
				hasTwo = true;
			} else {
				hasOne = true;
			}
		}
		if (hasTwo && hasOne)
			col[i] = 'N';
		else
			col[i] = 'Y';

		hasTwo = false;
		hasOne = false;
	}

	for (int i = 0; i < m; i++) {
		int k = 0;
		if (row[i] == 'Y')
			continue;
		for (int j = 0; j < n; j++) {
			if (input[i][j] != 1)
				continue;
			if (col[j] == 'Y') {
				row[i] = 'Y';
			} else {
				row[i] = 'N';
				return false;
			}
		}
	}
	return true;

}

void lawnMower::getInput() {
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			cin >> input[i][j];
		}
	}
}

int main() {

	int noOfTestCases = 0;
	cin >> noOfTestCases;
	int m = 0, n = 0;	//m rows n col

	for (int i = 1; i < noOfTestCases + 1; i++) {
		cin >> m;
		cin >> n;
		lawnMower obj(m, n);
		obj.getInput();
		if (obj.solve()) {
			cout << "Case #" << i << ": " << "YES" << endl;
		} else {
			cout << "Case #" << i << ": " << "NO" << endl;
		}

	}

	return 0;

}
