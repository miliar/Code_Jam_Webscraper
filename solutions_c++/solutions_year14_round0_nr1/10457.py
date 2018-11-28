//============================================================================
// Name        : CodeJamA.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int N = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int a1, a2, a3, a4;
		int T = 0;
		cin >> T;
		for (int j = 1; j < 5; j++) {
			int tmp;
			if (j == T) {
				cin >> a1;
				cin >> a2;
				cin >> a3;
				cin >> a4;
			} else {
				cin >> tmp;
				cin >> tmp;
				cin >> tmp;
				cin >> tmp;
			}
		}
		int D = 0;
		cin >> D;
		int result = -1;
		for (int j = 1; j < 5; j++) {
			for (int b = 0; b < 4; b++) {
				int tmp;
				if (j == D) {
					cin >> tmp;
					if (tmp == a1) {
						if (result == -1)
							result = a1;
						else {
							result = -2;
						}
					}
					if (tmp == a2) {
						if (result == -1)
							result = a2;
						else {
							result = -2;
						}
					}
					if (tmp == a3) {
						if (result == -1)
							result = a3;
						else {
							result = -2;
						}
					}
					if (tmp == a4) {
						if (result == -1)
							result = a4;
						else {
							result = -2;
						}
					}
				} else {
					cin >> tmp;
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		switch (result) {
		case -1:
			cout << "Volunteer cheated!";
			break;
		case -2:
			cout << "Bad magician!";
			break;
		default:
			cout << result;
			break;
		}
		cout << "\n";
	}
	return 0;
}
