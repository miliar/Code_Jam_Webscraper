#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << i << ":";
		for (int x = 0; x < s; x++) cout << " " << (x+1);
		cout << endl;
	}
}
