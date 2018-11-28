#include <iostream>

using namespace std;
int main() {
	long long t, test, n;
	cin >> t;
	for (test=1;test<=t;test++) {
		cin >> n;
		bool digit[10] = {0};
		long long count = 0;
		long long m = n;

		while (count < 10 && n>0) {
			long long copy = m;
			while (copy>0) {
				if (!digit[copy%10]) {
					digit[copy%10] = true;
					count ++;
				}
				copy /= 10;
			}
			m += n;
		}

		m -= n;
		if (m)
			cout << "Case #" << test << ": " << m << endl;
		else
			cout << "Case #" << test << ": " << "INSOMNIA" << endl;

	}
	return 0;
}
