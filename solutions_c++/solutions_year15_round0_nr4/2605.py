#include <iostream>
#include <cmath>
using namespace std;

// Can Richard choose an X to win?
string winningPlayer(int x, int r, int c) {
	/*if (x == 1) return "GABRIEL";
	if (x == 2) {
		if (r==1 && c==1 || r==3 && c==1 || r==1 && c==3 || r==3 && c==3) return "RICHARD";
		return "GABRIEL";
	}
	if (x==3) {
		if (r==2 && c==3 || r==3 && c==2 || r==3 && c==3 ||
			r==4 && c==4 || r==3 && c==4 || r==4 && c==3) return "GABRIEL";
		return "RICHARD";
	}
	if (x==4) {
		if (r==3 && c==4 || r==4 && c==3 || r==4 && c==4) return "GABRIEL";
		return "RICHARD";
	}*/
	
	int maxWidth = (int)ceil((double)x/2);
	if (r*c%x || r*c < x || r < maxWidth || c < maxWidth ||
		r < x-1 || c < x-1) return "RICHARD";
	return "GABRIEL";
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int X, R, C;
		cin >> X >> R >> C;
		cout << "Case #" << i+1 << ": " << winningPlayer(X, R, C) << endl;
	}
}