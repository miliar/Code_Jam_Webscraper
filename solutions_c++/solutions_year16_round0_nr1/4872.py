#include <iostream>
#include <bitset>

using namespace std;

bitset<10> full_bs("1111111111");

int main() {
#ifdef MAXTEST
	for (int N = 0; N <= 1000000; N++) {
#else
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		int N;
		cin >> N;
#endif

		if (N == 0) {
			cout << "INSOMNIA" << endl;
		} else {
			bitset<10> bs;
			
			long long n = 0;
			while (true) {
				n += N;
				long long x = n;
				while (x) {
					bs[x % 10] = 1;
					x /= 10;
				}
				if (bs == full_bs) {
					cout << n << endl;
					break;
				}
			}
		}
	}
}
