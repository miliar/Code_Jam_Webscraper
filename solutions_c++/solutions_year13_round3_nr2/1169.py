#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

int main() {

	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	int T, X, Y;

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> X >> Y;

		vector<char> routing;
		int currentX = 0, currentY = 0;
		for (int move = 1; move <= 500 && (currentX != X || currentY != Y); move++) {
			if (abs(X - currentX) == move)
			{
				if (X >= 0) {
					currentX += move;
					routing.push_back('E');
				} else {
					currentX -= move;
					routing.push_back('W');
				}
				continue;
			}

			if (abs(Y - currentY) == move)
			{
				if (Y >= 0) {
					currentY += move;
					routing.push_back('N');
				} else {
					currentY -= move;
					routing.push_back('S');
				} continue;
			}

			if (currentX != X) {
				if (abs(X - currentX) > move) {
					if (X >= 0) {
						currentX += move;
						routing.push_back('E');
					} else {
						currentX -= move;
						routing.push_back('W');
					}
					continue;
				} else if (abs(X - currentX) < move) {
					if (X >= 0) {
						currentX -= move;
						routing.push_back('W');
					} else {
						currentX += move;
						routing.push_back('E');
					} 
					continue;
				}
			}

			if (currentY != Y) {
				if (abs(Y - currentY) > move) {
					if (Y >= 0) {
						currentY += move;
						routing.push_back('N');
					} else {
						currentY -= move;
						routing.push_back('S');
					}
					continue;
				} else if (abs(Y - currentY) < move) {
					if (Y >= 0) {
						currentY -= move;
						routing.push_back('S');
					} else {
						currentY += move;
						routing.push_back('N');
					}
					continue;
				}
			}
		}

		if (currentX == X && currentY == Y) {
			cout << "Case #" << i+1 << ": ";
			for (vector<char>::iterator it = routing.begin(); it != routing.end(); ++it) {			
				cout << *it;
			}
			cout << endl;
		} else
			cout << "Case #" << i+1 << ": ERROR" << endl;
	}

	return 0;
}