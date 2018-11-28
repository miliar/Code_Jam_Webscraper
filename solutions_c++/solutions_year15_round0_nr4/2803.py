#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int count = 1; count <= t; count++) {
		int x, r, c;
		cin >> x >> r >> c;
		bool res = false;
		if(r > c) swap(r, c);
		if(x == 1) res = true;
		if(x == 2 && r*c % 2 == 0) res = true;
		if(x == 3 && r*c % 3 == 0 && r > 1) res = true;
		if(x == 4 && r*c % 4 == 0 && r > 2) res = true;
		cout << "Case #" << count << ": ";
		if(res) cout << "GABRIEL";
		else cout << "RICHARD";
		cout << endl;
	}
	return 0;
}
