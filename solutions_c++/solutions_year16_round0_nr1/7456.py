#include <bits/stdc++.h>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("inp.txt", "r", stdin);
	freopen("outp.txt", "w", stdout);
#endif
    int cases;
    cin >> cases;
    for (int c = 1; c <= cases; ++c) {
		cout << "Case #" << c << ": ";
		int n;
		cin >> n;
		if (!n) cout << "INSOMNIA" << endl;
		else {
			int msk = (1 << 10) - 1, cur = 0;
			do {
				cur += n;
				int tmp = cur;
				while (tmp)
					msk &= ~(1 << (tmp % 10)), tmp /= 10;
			} while (msk);
			cout << cur << endl;
		}
    }
	return 0;
}