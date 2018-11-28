#include <cassert>
#include <iostream>
#include <vector>

#define FOR(it, seq) for(auto it : seq)
#define FORI(it, beg, end) for(auto it = beg; it != end; ++it)

#define DBG(x) cout << x
#define DBGV(v) {cout << "["; FOR(i_, v) {DBG(i_); cout << ", ";} cout << "]" << endl; }

using namespace std;

typedef long long lint;
typedef vector<int> VI;
typedef vector<lint> VL;

int T;

void solve() {
	int flips = 0;
	char prev = '?';
	char c = '?';
	while (c != '!') {
		cin >> c;

		switch (c) {
			case '+':
				/* unchanged flips */
				break;
			case '-':
				if (prev == '?') {
					flips = 1;
				} else if (prev == '-') {
					/* flips = flips */
				} else if (prev == '+') {
					flips += 2;
				} else {
					assert(false);
				}
				break;
			default:
				c = '!';
				break;
		}
		prev = c;
	}

	cout << flips;
}

int main(int argc, char *argv[])
{
	char c;
	cin >> T;
	cin >> noskipws >> c;

	FORI(t, 0, T) {
		cout << "Case #" << (t+1) << ": ";

		solve();

		cout << endl;
	}


	return 0;
}
