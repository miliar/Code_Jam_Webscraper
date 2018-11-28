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

int n;

int a[2010], b[2010];
int c[2010];

void solve () {
	cin >> n;
	forn (i, n) {
		cin >> a[i];
	}
	forn (i, n) {
		cin >> b[i];
	}
	memset(c, 0, sizeof c);
	forn (t, n) {
		while (1) {
			bool q = 0;
			forn (i, n) {
				int mn = 1000000;
				forn (j, i) {
					if (a[j] + 1 == a[i]) {
						mn = min(mn, c[j] + 1);
					}
					if (b[j] <= b[i]) {
						if (c[i] < c[j] + 1) {
							q = 1;
							c[i] = c[j] + 1;
						}
					}
				}
				if (a[i] > 1) {
					if (c[i] < mn) {
						q = 1;
						c[i] = mn;
					}
				}
				mn = 1000000;
				for (int j = i + 1; j < n; ++j) {
					if (b[j] + 1 == b[i]) {
						mn = min(mn, c[j] + 1);
					}
					if (a[j] <= a[i]) {
						if (c[i] < c[j] + 1) {
							q = 1;
							c[i] = c[j] + 1;
						}
					}
				}
				if (b[i] > 1) {
					if (c[i] < mn) {
						q = 1;
						c[i] = mn;
					}
				}
			}
			if (!q) {
				break;
			}
		}
		int cnt = 0;
		forn (i, n) {
			if (c[i] == t) {
				c[i] += cnt;
				cnt++;
			}
		}
	}
	forn (i, n) {
		if (i) {
			cout << ' ';
		}
		cout << c[i] + 1;
	}
	cout << endl;
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
