#include <bits/stdc++.h>

using namespace std;

int T;
int k, c, s;

void load () {
	cin >> k >> c >> s;
}

void solve () {
	for (int i = 0; i < s; i++) {
		cout << ' ' << i + 1; 	
	}
	cout << endl;
}

int main () {
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		load ();
		cout << "Case #" << tc << ":";
		solve ();
	}	
}