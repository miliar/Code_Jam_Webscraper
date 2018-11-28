#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	int numCases;
	cin >> numCases;
	
	for(int x = 1; x <= numCases; x++) {
		int X, R, C;
		cin >> X >> R >> C;
		
		//Adding some consistency to dimension ordering, for my own convenience:
		if(R < C) {
			int temp = R;
			R = C;
			C = temp;
		}
		
		if(X > R * C || (R * C) % X != 0) {//auto-win for Richard
			cout << "Case #" << x << ": RICHARD\n";
		} else if(C > 1 && X >= 2 * C) {//Richard can choose a shape that doesn't fit
			cout << "Case #" << x << ": RICHARD\n";
		} else if(C == 1 && X > 2) {//Richard can choose a shape that doesn't fit
			cout << "Case #" << x << ": RICHARD\n";
		} else if(X >= 7) {//Richard can make a shape with a 1x1 hole
			cout << "Case #" << x << ": RICHARD\n";
		} else if(X > R) {//Richard can choose a line-shape that doesn't fit
			cout << "Case #" << x << ": RICHARD\n";
		} else if(X <= R) {//Richard can't win unless he can force an unfavourable board split
			if(C < 3) {//cannot force a board split
				cout << "Case #" << x << ": GABRIEL\n";
			} else if(X < ((2 * C) - 1)) {//cannot force a board split
				cout << "Case #" << x << ": GABRIEL\n";
			} else if(R % C == 0) {//cannot force an unfavourable board split
				cout << "Case #" << x << ": GABRIEL\n";
			} else {
				bool canForceBad = false;
				for(int blah = 1; blah < (C+1)/2; blah++) {
					bool tempForceBad = true;
					int leftover = blah * (C - 1);
					for(int blah2 = 0; blah2 < C; blah2++) {
						if((leftover + (C * blah2)) % X == 0) {
							if(leftover + (C * blah2) + X < (R * C)) {
								tempForceBad = false;
							}
						}
					}
					canForceBad = canForceBad || tempForceBad;
				}
				if(canForceBad) {
					cout << "Case #" << x << ": RICHARD\n";
				} else {
					cout << "Case #" << x << ": GABRIEL\n";
				}
			}
		} else {
			cerr << "SANITY CHECK ERROR\n";
		}
	}
}
