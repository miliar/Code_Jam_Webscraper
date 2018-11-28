#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int S; cin >> S;
		int count = 0;
		int sol = 0;
		
		for (int i = 0; i < S+1; i++) {
			char x; cin >> x;
			if (count < i) {
				sol += i-count;
				count = i;
			}
			count += x-'0';
		}
		
		cout << "Case #" << t << ": " << sol << endl;
	}
}
