#include <iostream>
#include <unordered_map>
using namespace std;
int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int r;
		int x;
		unordered_map<int, bool> h_table;

		cin >> r;

		for (int j = 1; j <= 4; j++) {
			for (int k = 0; k < 4; k++) {
				cin >> x;
				if (j == r) {
					h_table[x] = true;
				}
			}
		}

		cin >> r;
		int count = 0;
		int result;
		for (int j = 1; j <= 4; j++) {
			for (int k = 0; k < 4; k++) {
				cin >> x;
				if (j == r && h_table.find(x) != h_table.end()) {
					count++;
					result = x;
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		if (count == 1) {
			cout << result << endl;
		} else if (count >= 2) {
			cout << "Bad magician!" << endl;
		} else 
			cout << "Volunteer cheated!" << endl;
	}
	return 0;
}