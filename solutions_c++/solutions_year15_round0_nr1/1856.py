#include <iostream>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		
		int n;
		cin >> n;
		string audience;
		cin >> audience;
		int current_amount = 0;
		int friends = 0;
		int length = audience.length();
		for (int c = 0; c < length; c++) {
			if (current_amount < c) {
				friends += c - current_amount;
				current_amount = c;
			}
			current_amount += audience[c] - '0';
		}
		cout << "Case #" << i << ": " << friends << endl;
	}
	return 0;
}