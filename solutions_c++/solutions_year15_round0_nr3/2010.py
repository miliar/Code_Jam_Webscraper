#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <ctime>
#include <algorithm>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
string s, tmp;
int t, n, x;
int head[11111], tail[11111];
inline int mult(int &prod, int &sgn, char s, bool swp = 0) {
	if (prod == 1) {
		prod = s - 'i' + 2;
	} else
		if (prod == 2) {
			if (s == 'i') {
				prod = 1; sgn *= -1;
			} else
				if (s == 'j') {
					prod = 4; if (swp) sgn *= -1;
				} else {
					prod = 3; sgn *= -1; if (swp) sgn *= -1;
				}
		} else
			if (prod == 3) {
				if (s == 'i') {
					prod = 4; sgn *= -1; if (swp) sgn *= -1;
				} else
					if (s == 'j') {
						prod = 1; sgn *= -1;
					} else {
						prod = 2; if (swp) sgn *= -1;
					}
			} else {
				if (s == 'i') {
					prod = 3; if (swp) sgn *= -1;
				} else
					if (s == 'j') {
						prod = 2; sgn *= -1; if (swp) sgn *= -1;
					} else {
						prod = 1; sgn *= -1;
					}
			}
}
int main() {

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for(int tc = 1; tc <= t; ++tc)  {
		cerr << tc << endl;
		cin >> n >> x;
		cin >> tmp;
		s = "";
		for(int i = 0; i < x; ++i) {
			s += tmp;
		}
		n *= x;

		int prod = 1, sgn = 1;
		for(int i = 0; i < n; ++i) {
			mult(prod, sgn, s[i]);
			head[i] = prod * sgn;
		}


		prod = 1; sgn = 1;
		for(int i = n - 1; i >= 0; --i) {
			mult(prod, sgn, s[i], 1);
			tail[i] = prod * sgn;
		}

//		cerr << head[2] << endl;
//		cerr << tail[n - 6] << endl;
//		exit(0);

		bool ok = 0;
		for(int i = 1; i < n && !ok; ++i) {
			if (head[i - 1] != 2) continue;
			prod = 1; sgn = 1;
			for(int j = i; j < n - 1; ++j) {
				mult(prod, sgn, s[j]);
		//		if (i == 3) {
		//			cerr << s[j] << " " << prod << " " << sgn << endl;
		//		}
				if (prod * sgn == 3 && tail[j + 1] == 4) {
					ok = 1;
					break;
				}
			}
		}
		cout << "Case #" << tc << ": ";
		if (ok) cout << "YES\n"; else cout << "NO\n";
	}
}
