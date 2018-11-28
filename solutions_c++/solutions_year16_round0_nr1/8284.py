#include <bits/stdc++.h>
using namespace std;
int main(long long argc, char **argv) {
	long long tc, n;
	cin >> tc;
	long long myCase = 1;
	while (tc--) {
		cin >> n;
		if (n == 0) {
			cout << "Case #" << myCase << ": INSOMNIA\n";
		} else {
			bitset<10> m(0);
			long long ind = 1;
			while (m.to_ullong() != ((1 << 10) - 1)) {
				long long x = n * ind;
				string s = to_string(x);
				for (long long j = 0; j < (long long) s.length(); j++)
					m[s[j] - '0'] = 1;
				ind++;
			}
			cout << "Case #" << myCase << ": " << n * (ind - 1) << endl;
		}
		myCase++;
	}
	return 0;
}
