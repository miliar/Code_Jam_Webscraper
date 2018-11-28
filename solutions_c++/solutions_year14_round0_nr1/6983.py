#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main() {
	int cases,card,answer[2],posible_cards[2][4];
	vector<int> v;

	cin >> cases;
	cin.ignore();
	for (int i=0; i<cases; i++) {
		// Answers
		for (int j=0; j<2; j++) {
			cin >> answer[j];
			// Rows
			for (int row=0; row<4; row++) {
				// Columns
				for (int col=0; col<4; col++) {
					cin >> card;
					if (row==answer[j]-1) {
						posible_cards[j][col] = card;
					}
				}
			}
		}
		v.clear();
		for (int j=0; j<4; j++) {
			for (int k=0; k<4; k++) {
				if (posible_cards[0][j]==posible_cards[1][k]) {
					v.push_back(posible_cards[0][j]);
				}
			}
		}
		// Out
		cout << "Case #" << i+1 << ": ";
		switch (v.size()) {
			case 0: cout << "Volunteer cheated!";
			break;
			case 1: cout << v[0];
			break;
			default: cout << "Bad magician!";
			break;
		}
		cout << endl;
	}
	return 0;
}

