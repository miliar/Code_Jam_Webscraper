#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (auto i = begin(c); i != end(c); i++)
#define all(c) begin(c), end(c)
#define sz(c) int((c).size())
#define mp make_pair
#define pb push_back
#define DBG(...) ({ if(1) fprintf(stderr, __VA_ARGS__); })
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

template<class C, class I>
bool has(C con, I item) {
	return con.find(item) != con.end();
}

int main() {
	ios::sync_with_stdio(false);

	int TC;
	cin >> TC;
	FOR(tc, 1, TC+1) {
		ll N;
		cin >> N;
		cout << "Case #" << tc << ": ";

		if (N == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}

		set<char> digits;
		ll cur = 0;

		while (sz(digits) < 10) {
			cur += N;

			auto tmp = to_string(cur);
			for (char c : tmp) {
				digits.insert(c);
			}
		}

		cout << cur << endl;
	}
}
