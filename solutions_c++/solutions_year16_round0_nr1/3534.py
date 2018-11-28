#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<vii> vvii;
typedef set<int> si;
typedef vector<si> vsi;
typedef pair<double, double> dd;

const int inf = 1e9;

void what_digits(si& d, int n) {
	do {
		d.insert(n % 10);
		n /= 10;
	} while (n);
}

int main() {
	ios::sync_with_stdio(false);

	int ts; cin >> ts;
	for (int t = 1; t <= ts; t++) {
		int n; cin >> n;
		si s, digits;
		bool insomnia = true;
		int tmp = n;
		while (s.find(tmp) == s.end()) {
			s.insert(tmp);
			what_digits(digits, tmp);
			// for (si::iterator i = s.begin(); i != s.end(); i++)
			// 	cerr << *i << ' ';
			// cerr << endl;
			if (digits.size() == 10) {
				insomnia = false;
				break;
			}
			tmp += n;
		}
		cout << "Case #" << t << ": ";
		if (insomnia)
			cout << "INSOMNIA" << endl;
		else
			cout << tmp << endl;
	}

	return 0;
}
