#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second

typedef unsigned long long ull;
typedef unsigned int ui;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);
const double E = exp(1);

int n, p, r, s;
char c[3] = {'S', 'R', 'P'};
vector <int> v;

bool vai () {
	if (v.size() == 1) return true;

	vector <int> ve;
	for (int i = 0; i < (int)v.size(); i+=2) {
		if (v[i] == v[i+1]) return false;
		if (v[i] == 0)
			if (v[i + 1] == 1)	ve.pb(v[i + 1]);
			else 			ve.pb(v[i]);
		else if (v[i] == 1)
			if (v[i + 1] == 2)	ve.pb(v[i + 1]);
			else			ve.pb(v[i]);
		else
			if (v[i + 1] == 0)	ve.pb(v[i + 1]);
			else 			ve.pb(v[i]);
	}
	v.clear();
	for (int i = 0; i < (int)ve.size(); i++)
		v.pb(ve[i]);
	return vai();
}

void go () {
	int m = 1;

	int N = n;
	n = 1;
	for (int i = 0; i < N; i++)
		n *= 2;

	for (int i = 0; i < n; i++)
		m *= 3;

	for (int i = 0; i < m; i++) {
		int val = i;
		int P = 0, R = 0, S = 0;
		v.clear();
		for (int j = 0; j < n; j++) {
			if ((val%3) == 0) S++;
			else if ((val%3) == 1) R++;
			else P++;
//			cout << (val%3) << " ";
			v.pb((val%3));
			val /= 3;
			if (R == r and P == p and S == s and vai()) {
				int val = i;
				for (int j = 0; j < n; j++) {
					cout << c[(val%3)];
					val /= 3;
				}
				cout << endl;
				return;
			}
		}
//		cout << endl;
	}

	cout << "IMPOSSIBLE" << endl;
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int t;	cin >> t;
	for (int T = 1; T <= t; T++) {
		cout << "Case #" << T << ": ";
		cin >> n >> r >> p >> s;
		go();
	}
	return 0;
}
