#include <cstdio>
#include <iostream>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	int X, R, C;
	bool gridCanBeFilled;
	for (int t=1; t<=T; t++) {
		cin >> X >> R >> C;
		if (C > R) swap(R, C);
		
		// C <= R
		
		// C 1 1 1 1 2 2 2 3 3 4
		// R 1 2 3 4 2 3 4 3 4 4
		
		// C 1 1 2 1 2 3 1 2 3 4
		// R 1 2 2 3 3 3 4 4 4 4
		
		if (X == 1) {	//1x1 block
			gridCanBeFilled = true;
		}
		if (X == 2) {	//1x2 block
			if (R==1) gridCanBeFilled = false;
			if (R==2) gridCanBeFilled = true;
			if (R==3) gridCanBeFilled = (C==2);
			if (R==4) gridCanBeFilled = true;
		}
		if (X == 3) {
			if (C==1) gridCanBeFilled = false;	//choose L-shaped block
			if (C==2) gridCanBeFilled = (R==3);
			if (C==3) gridCanBeFilled = true;
			if (C==4) gridCanBeFilled = false;
		}
		if (X == 4) {
			if (C==1) gridCanBeFilled = false;	//choose 2x2 block
			if (C==2) gridCanBeFilled = false;	//R==2 or R==3 -> choose 1x4 block, R==4 choose lightning bolt shaped block
			if (C==3) gridCanBeFilled = (R==4);
			if (C==4) gridCanBeFilled = true;
		}
		
		printf("Case #%d: %s\n", t, (gridCanBeFilled) ? "GABRIEL" : "RICHARD");
	}
	return 0;
}