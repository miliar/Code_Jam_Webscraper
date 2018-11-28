#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int i = 0 ; i < T ; ++i) {
		int X, R, C;
		cin >> X >> R >> C;

		int ans; // 0 = GABRIEL, 1 = RICHARD.
		if (X == 1) {
			ans = 0;
		} else if (X == 2) {
			ans = (R%2 && C%2)?1:0;
		} else if (X == 3) {
			ans = (R%3==0 || C%3==0)&&(R+C)>=5 ? 0:1;
		} else {	
			ans = ((R%2==0 && C%2==0) || (R%4==0&&C%2==1) || (C%4==0&&R%2==1)) && (R+C) >= 7 ? 0 : 1;
		}

		cout << "Case #" << i+1 << ": " << (ans?"RICHARD":"GABRIEL") << endl;
	}
}