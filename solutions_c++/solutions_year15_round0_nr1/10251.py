#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t, s, res, count = 0;
	char c;
	cin >> t;
	while (t > 0) {
		res = 0;
		cin >> s;
		int temp, sum = 0;
		for (int i = 0; i < s + 1; i++) {
			cin >> c;
			temp = c - 48;
			//cout << "i: " << i << endl << "sum: " << sum << endl;
			if (temp != 0 && i > sum) {
				res += i - sum;
				sum += res;
			}
			sum += temp;
		}
		count++;
		cout << "Case #" << count << ": " << res << endl;
		t--;
	}
	return 0;
}