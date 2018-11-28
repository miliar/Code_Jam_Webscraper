#define DEBUG 0
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cerr << fixed << setprecision(0);

	if (!DEBUG) {
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	}

	int _c, _start = static_cast<int>(clock());
	cin >> _c;

	for(int _cc = 1; _cc <= _c; ++_cc) {
		int _t = static_cast<int>(clock());
		cout << "Case #" << _cc << ": ";

		string s;
		cin >> s;

		char matchC = '+';
		int nFlips = 0;

		for (int i = s.size() - 1; i >= 0; --i) {
			if (s[i] != matchC) {
				++nFlips;
				matchC = s[i];
			}
		}
		cout << nFlips << '\n';

		cerr << "[Case #" << _cc << " complete, " << static_cast<int>(clock() - _t) << " ms, " << 100. * _cc / _c << "%]" << endl;
	}

	cerr << "Total time: " << static_cast<int>(clock() - _start) << " ms" << endl;

	return 0;
}

