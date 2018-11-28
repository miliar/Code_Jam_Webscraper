#include <iostream>
#include <string>

using namespace std;

const int MAXN = 1005;
bool pancakes[MAXN];

int main() {
	string input_string;
	
	int t, n, k, res;
	cin >> t;
	
	bool possible = true;
	
	for (int q = 0; q < t; q++) {
		cin >> input_string;
		cin >> k;
		
		n = input_string.size();
		
		
		for (int i = 0; i < n; i++) {
			if (input_string[i] == '+') {
				pancakes[i] = true;
			} else {
				pancakes[i] = false;
			}
		}
		
		res = 0;
		for (int i = 0; i <= n - k; i++) {
			if (!pancakes[i]) {
				++res;
				
				for (int j = i; j < i + k; j++) {
					pancakes[j] = !pancakes[j];
				}
			}
		}
		
		possible = true;
		
		for (int i = n - k + 1; i < n; i++) {
			if (!pancakes[i]) {
				possible = false;
			}
		}
		
		cout << "Case #" << q + 1 << ": ";
		(possible) ? cout << res << endl : cout << "IMPOSSIBLE" << endl;
	}
}