#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; q++) {
		string pancakes;
		int flipper_size;
		cin.ignore();
		// Read input 
		cin >> pancakes;
		cin >> flipper_size;
		// Minimum number of flips required if possible
		int flip_count = 0;
		for (int i = 0; i < pancakes.size() - flipper_size + 1; i++) {
			if (pancakes[i] == '-') {
				for (int j = 0; j < flipper_size; j++) {
					pancakes[i + j] = pancakes[i + j] == '+' ? '-' : '+';
				}
				flip_count++;
			}
		}
		string ans = to_string(flip_count);
		for (int i = 0; i < pancakes.size(); i++) {
			if (pancakes[i] == '-') {
				ans = "IMPOSSIBLE";
				break;
			}
		}
		cout << "Case #" << q << ": " << ans << endl;
	}
	return 0;
}
				

