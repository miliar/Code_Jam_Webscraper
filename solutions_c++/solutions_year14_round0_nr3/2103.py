#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <deque>
#include <bitset>

#define sqr(x) ((x) * (x))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define y0 ywuerosdfhgjkls
#define y1 hdsfjkhgjlsdfhgsdf
#define j1 j924
#define j0 j2834
#define sqrt(x) (sqrt(abs(x)))
#define re return
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = ((n) - 1); i >= 0; i--)
#define fill(a, x) memset(a, x, sizeof(a))

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <int> vi;
typedef vector <ii> vii;
typedef vector <vi> vvi;
typedef double D;
typedef vector <string> vs;

template <class T> inline T abs(T a) {
		return a > 0 ? a : -a;
}

int n;
int m;

const int nmax = 50;

int main() {
	int T;
	cin >> T;
	rep(I, T) {
		cout << "Case #" << I + 1 << ":" << endl;
		int n, m, k;
		cin >> n >> m >> k;
		k = n * m - k;
		string s[n];
		if (k == 1) {
			cout << "c";
			rep(j, m - 1)
				cout << "*";
			cout << endl;
			rep(i, n - 1) {
				rep(j, m)
					cout << "*";
				cout << endl;
			}
		} else if (min(n, m) == 1) {
			if (n == 1) {
				cout << "c";
				rep(i, k - 1)
					cout << ".";
				rep(i, m - k)
					cout << "*";
				cout << endl;
			} else {
				cout << "c" << endl;
				rep(i, k - 1)
					cout << "." << endl;
				rep(i, n - k)
					cout << "*" << endl;
			}
		} else {
			rep(i, n) {
				s[i] = "";
				rep(j, m)
					s[i] += "*";
			}
				
			bool kpyto = false;
			for (int i = 2; i <= n; i++) {
				for (int j = 2; j <= m; j++) {
					if (i * j >= k && i * j - (i - 2) * (j - 2) <= k) {
						rep(x, i)
							rep(y, j)
								s[x][y] = '.';
						kpyto = true;
						k = i * j - k;
						int x = i - 1;
						int y = j - 1;
						while (k > 0) {
							while (y > 1 && k-- > 0)
								s[x][y--] = '*';
							x--;
							y = j - 1;
						}
						s[0][0] = 'c';
						rep(q, n)
							cout << s[q] << endl;
						break;
					}
					if (kpyto)
						break;
				}
				if (kpyto)
					break;
			}
			if (!kpyto)
				cout << "Impossible" << endl;
		}
	}
	return 0;
}
