#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

ostream& operator<<(ostream &out, const pii &a) { return out << '(' << a.first << ", " << a.second << ')'; }
istream& operator>>(istream &in, pii &a) { return in >> a.first >> a.second; }

const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

// lambda-expression: [] (args) -> retType { body }

int n, l;
string g[1000], b;

void run(int tc)
{
	cin >> n >> l;
	for (int i = 0; i < n; i++) {
		cin >> g[i];
	}
	cin >> b;

	cerr << "Case #" << tc << ": " << n << " " << l << endl;
	for (int i = 0; i < n; i++) {
		cerr << g[i] << endl;
	}
	cerr << b << endl;

//	for (char c : b) {
//		if (c != '1') {
//			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
//			return;
//		}
//	}
	for (int i = 0; i < n; i++) {
		if (g[i] == b) {
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
			return;
		}
	}

	string aa = "?", ab = "";
	for (int i = 1; i < l; i++) {
		if (i & 1) ab += "10?";
		else aa += "10?";
	}
	if (l & 1) aa += "1";
	else ab += "1";

	if (ab == "") ab = "0";

//	cerr << tc << ": " << n << " " << l << endl;
	assert(aa.size() + ab.size() <= 200);
	cout << "Case #" << tc << ": " << aa << " " << ab << endl;
}

int main()
{
#ifdef LOCAL
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
    assert(freopen("debug.txt", "w", stderr));
#endif // LOCAL
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	// cerr << boolalpha;
	(cout << fixed).precision(10);

	int ntc;
	cin >> ntc;
	for (int tc = 1; tc <= ntc; tc++) {
		run(tc);
	}

	return 0;
}
