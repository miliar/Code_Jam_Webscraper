#include "bits/stdc++.h"
 
using namespace std;
 
#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define mp make_pair
#define pb push_back
#define PATH "C:\\Users\\ValenKof\\Desktop\\"
 
template<typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template<typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template<typename T> inline int sz(const T& x) { return x.size(); }
 
typedef unsigned char uchar;
 
// SOLUTIONS BEGINS HERE

const int N = 100;

int r, c;

int a[N][N];

unordered_set<string> total;

bool ok(int i, int j) {
	int need = a[i][j];
	int count = 0;
	if (i - 1 >= 0 && a[i - 1][j] == need) count++;
	if (i + 1 < r && a[i + 1][j] == need) count++;
	if (a[i][(c + j - 1) % c] == need) count++;
	if (a[i][(c + j + 1) % c] == need) count++;
	
	return need == count;
}

bool validate() {
	// forn (i, r) {
		// forn (j, c) {
			// cout << a[i][j];
		// }
		// cout << endl;
	// }
	// cout << "=============" << endl;
	
	forn (i, r) {
		forn (j, c) {
			if (!ok(i, j)) {
				return false;
			}
		}
	}
	return true;
} 


void add() {
	vector<string> ss(r);
	forn (i, r) {
		string s = "";
		forn (j, c) {
			s += (char) (a[i][j] + '0');
		}
		ss[i] = s + s;
	}
	vector<string> shifts;
	forn (shift, c) {
		string s = "";
		forn (i, r) {
			s += ss[i].substr(shift, c);
		}
		shifts.pb(s);		
	}
	total.insert(*min_element(all(shifts)));
}

void gen(int i, int j)
{
	if (j == c) {
		i = i + 1;
		j = 0;
	}
	if (i == r) {
		if (validate()) {
			add();
		}
		return;
	}
	for (int place = 1; place <= 3; ++place) {
		a[i][j] = place;
		if (i > 0) {
			if (!ok(i - 1, j)) {
				continue;
			}
		}
		if (j > 0) {
			if (a[i][j - 1] == 3) {
				if (place != 3) {
					continue;
				}
			}
		}
		
		gen(i, j + 1);
	}
	a[i][j] = -1;
}


void solve() {
	cin >> r >> c;
	total.clear();
	forn (i, r) forn (j, c) a[i][j] = -1;
	gen(0, 0);
	cout << sz(total);
	// debug(total);
}
 
int main() {
	// freopen(PATH"in.txt", "r", stdin);
	freopen(PATH"D-small-attempt0.in", "r", stdin);
	freopen(PATH"out.txt", "w", stdout);
	int nTests;
	cin >> nTests;
	forn (i, nTests) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
		cout << endl;
	}	
	return 0;
}