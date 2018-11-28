#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORVEC(it,v) for (auto it=(v).begin(); it != (v).end(); ++it)
#define NUL(arr) memset(arr, 0, sizeof(arr));
#define SORT(x) sort((x).begin(), (x).end());

/* Liefert alle Möglichkeiten k Zahlen aus [lo,hi] zu ziehen
 * wobei die Reihenfolge nicht beachtet wird
 * v ist ein Array der Größe k und enthält die gezogenen Zahlen
 * int v[k];
 * choose_init(v, k, lo);
 * do { ... } while (choose_next(v, k, lo, hi));
 */
 
void choose_init(int* v, int k, int lo) {
	while (k--) v[k] = lo+k;
}
 
bool choose_next(int* v, int k, int lo, int hi) {
	if (--k<0) return false;
	if (++v[k] <= hi) return true;
	if (!choose_next(v, k, lo, hi-1)) { v[k] = lo+k; return false; }
	v[k] = v[k-1]+1;
	return true;
}

void solve()
{
	int n, k;
	cin >> n >> k;
	vector<ld> p(n);
	FOR(i,n) cin >> p[i];
	int v[n], w[n];
	choose_init(v, k, 0);
	ld yesbest = 0.0;
	do {
		ld yesall = 0.0;
		choose_init(w, k/2, 0);
		w[k/2] = 10000;
		do {
			ld yes = 1.0;
			int j = 0;
			FOR(i,k) {
				if (i == w[j]) {
					yes *= p[v[i]];
					++j;
				} else {
					yes *= (1 - p[v[i]]);
				}
			}
			yesall += yes;
		} while (choose_next(w, k/2, 0, k-1));
		yesbest = max(yesbest, yesall);
	} while (choose_next(v, k, 0, n-1));
	cout << fixed << setprecision(6) << yesbest;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}
