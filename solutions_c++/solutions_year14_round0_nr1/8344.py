#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	int T; int playerAnswer;
	int cardMap[4][4];
	int cardArray[4]; int answer = 0; int counter = 1; int multi = 0;
	cin >> T;

	while (counter != T+1) {
		cin >> playerAnswer;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> cardMap[i][j];
			}
		}
		for (int i = 0; i < 4; i++) {
			cardArray[i] = cardMap[playerAnswer-1][i];
		}
		cin >> playerAnswer;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> cardMap[i][j];
			}
		}
		// answer = 0, volunteer cheated!, answer = 1~16, Bad magician!
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (cardArray[i] == cardMap[playerAnswer-1][j]) {
					answer= cardMap[playerAnswer-1][j];
					multi++;
				}
			}
		}
		if (answer == 0)
			cout << "Case #" << counter << ": " << "Volunteer cheated!"<< endl;
		else if (multi == 1)
			cout << "Case #" << counter << ": " << answer << endl;
		else if (multi > 1)
			cout << "Case #" << counter << ": " << "Bad magician!" << endl;
		answer = 0;
		multi = 0;
		counter++;
	}
	return 0;
}