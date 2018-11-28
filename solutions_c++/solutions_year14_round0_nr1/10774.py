#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

string verdict;
int answer;

void solve() {
	int row;
	cin >> row; row--;
	bool can[20];
	int x;
	for (int i = 1; i <= 16; ++i) can[i] = false;
	for (int i = 0; i < 4; ++i)
		for (int j=0;j < 4; ++j) {
			cin >> x;
			if (i == row) {
				can[x] = true;
			} else {
				can[x] = false;
			}
		}
	cin >> row; row--;
	for (int i = 0; i < 4; ++i)
		for (int j=0;j < 4; ++j) {
			cin >> x;
			if (i == row) {
				//
			} else {
				can[x] = false;
			}
		}
	int count = 0;
	int ans;
	for (int i = 1; i <= 16; ++i) {
		if (can[i]) {
			count++;
			ans = i;
		}
	}
	if (count == 0) {
		verdict = " Volunteer cheated!";
	} else if (count == 1) {
		verdict = "";
		answer = ans;
	} else {
		verdict = " Bad magician!";
	}
}

void print(int testNum) {
	cout << "Case #" << testNum + 1<< ":";
	if  (verdict.size() == 0) {
		cout << " " << answer << endl;
	} else {
		cout << verdict << endl;
	}

}
int main() {
	int tests;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> tests;
	//cout << "Yesy";
	for (int test = 0; test< tests; ++test) {
		//cout << "test " << test << endl;
		solve();
		print(test);
	}
	return 0;
}