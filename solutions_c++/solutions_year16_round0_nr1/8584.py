#include <iostream>  
#include <vector>
using namespace std;
int main() {
	int t, n;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
			continue;
		}
		int last = 0;
		vector<int> digits(10, 0);
		int numdigit;
		do {
			last += n;
			for (int tmp = last; tmp; tmp /= 10) {
				digits[tmp % 10] = 1;
			}
			numdigit = 0;
			for (int& d : digits)
				numdigit += d;
		} while (numdigit < 10);
		cout << "Case #" << i << ": " << last << endl;
	}
	return 0;
}
