#include <iostream>

using namespace std;

int main() {

	int T;
	cin >> T;

	for(int t = 0; t < T; t++) {
		int ans;
		cin >> ans;
		ans = ans - 1;

		int boarda[4][4];
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				int c;
				cin >> c;
				boarda[i][j] = c;
				// cout << boarda[i][j] << " " ;
			}
			// cout << endl;
		}

		int ans_after;
		cin >> ans_after;
		ans_after = ans_after-1;
		int boardb[4][4];
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				int c;
				cin >> c;
				boardb[i][j] = c;
				// cout << boardb[i][j] << " " ;
			}
			// cout << endl;
		}
		// cout << endl;

		//logic heres



		int count = 0;
		int index = 0;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(boarda[ans][i] == boardb[ans_after][j]) {
					count++;
					index = boarda[ans][i];
				}
			}
		}

		cout << "Case #" << t+1 << ": ";

		if(count > 1) {
			cout << "Bad magician!" << endl;
		} else if(count == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << index << endl;
		}
	}
}