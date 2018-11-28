#include <iostream>

using namespace std;

long sleep(int n) {
	bool seen[10] = {false};
	long cur = n;
	while (true) {
		long tmp = cur;
		do {
			int digit = tmp % 10;
			seen[digit] = true;
			tmp /= 10;
		} while (tmp > 0);
		if (seen[0] && seen[1] && seen[2] && seen[3] && seen[4] && seen[5] && seen[6] && seen[7] && seen[8] && seen[9]) {
			return cur;
		}
		cur += n;
	}
}

int main() {
	int t,n;
	cin >> t;
	for (int i=0;i<t;++i) {
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		} else {
			cout << "Case #" << i+1 << ": " << sleep(n) << endl;
		}
	}
	return 0;
}
