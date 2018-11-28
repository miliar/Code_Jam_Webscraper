#include <iostream>
using namespace std;
#define G "GABRIEL"
#define R "RICHARD"

string ans(int x, int r, int c) {
	if (x == 1) return G;
	if ((r*c)%x != 0) return R;	
	if (x == 2) return G;
	if (x == 3) {
		if (r == 1 || c == 1) return R;
		else return G;
	}
	if (x == 4) {
		if ((r*c)/x <= 2) return R;
		else return G;
	}
	
}


int main() {
	int x, r, c;
	int t; cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> x >> r >> c;
		cout << "Case #" << i << ": " << ans(x, r, c) << endl;
	} 


	return 0;
}
