#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <utility>
#include <cstdlib>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <memory.h>
#include <ctime>
#include <cctype>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define mp make_pair
#define fs first
#define sc second
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long double ld;
typedef long long ll;
typedef unsigned char uc;
typedef unsigned int ui;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;

const ld pi = 3.141592653589793238462643l;

int a[105][105];

void solve () {
	int n, m;
	cin >> n >> m;
	forn (i, n) {
		forn (j, m) {
			cin >> a[i][j];
		}
	}
	while (n && m) {
		int mn = 1000;
		forn (i, n) {
			forn (j, m) {
				if (mn > a[i][j]) {
					mn = a[i][j];
				}
			}
		}
		bool done = 0;
		forn (i, n) {
			bool ok = 1;
			forn (j, m) {
				ok &= a[i][j] == mn;
			}
			if (ok) {
				done = 1;
				forn (j, m) {
					a[i][j] = a[n - 1][j];
				}
				n--;
				i--;
			}
		}
		forn (j, m) {
			bool ok = 1;
			forn (i, n) {
				ok &= a[i][j] == mn;
			}
			if (ok) {
				done = 1;
				forn (i, n) {
					a[i][j] = a[i][m - 1];
				}
				m--;
				j--;
			}
		}
		if (!done) {
			puts("NO");
			return;
		}
	}
	puts("YES");
}

int main () {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);	
	int t;
	cin >> t;
	forn (i, t) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}

