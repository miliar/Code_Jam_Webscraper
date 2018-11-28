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

string s;
int n, cs, js;

void run(int tc)
{
	cin >> s;
//	n = s.size() / 2;
	vector<char> rem;

	int sum = 0;
	for (char c : s) {

		// cerr << c << " ";

		if (rem.empty()) {
			rem.push_back(c);
			continue;
		}

		if (c == rem.back()) {

			// cerr << c << " vs " << rem.back()

			rem.pop_back();
			sum += 10;
		} else {
			rem.push_back(c);
		}
	}

	cerr << sum << " " << rem.size() << endl;

	int answer = sum + 5 * (rem.size() / 2);

	/*
	cs = js = 0;
	for (char c : s) {
		if (c == 'C') cs++;
		else js++;
	}

	for (int c = 0; c < n; c++) {
		int sum = 0;
		stack<char> s;
		int cleft = c, jleft = n - c;

		for (char c : s) {
			if (s.empty()) {
				s.push(c);


				if (c == 'C') cleft--;
				else jleft--;
			}
			if (c == 'C') {
				if (s.top())
			}
		}
	}
	*/

	cout << "Case #" << tc << ": " << answer << endl;
}

int main()
{
#ifdef LOCAL
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
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
