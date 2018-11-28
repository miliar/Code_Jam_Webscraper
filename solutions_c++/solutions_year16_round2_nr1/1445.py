#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define makeunique(x) sort(all(x)), (x).resize(unique(x) - (x).begin())
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define j0 j5743892
#define j1 j542893
                         
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { re x > 0 ? x : -x; }
template<class T> T gcd(T a, T b) { re a ? gcd (b % a, a) : b; }
template<class T> T sqr(T a) { re a * a; }
template<class T> T sgn(T a) { re a > 0 ? 1 : (a < 0 ? -1 : 0); }

#define filename ""

int n;
int m;
string w[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
// "ONE", "NINE"

int main () {
//	freopen (filename".in", "r", stdin);
//	freopen (filename".out", "w", stdout);	
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++) {
		string s;
		cin >> s;
		vi c(256, 0);
		vi res(10, 0);
		for (int i = 0; i < sz (s); i++) c[s[i]] ++;
		while (c['Z'] > 0) { res[0] ++; for (int j = 0; j < sz (w[0]); j++) c[w[0][j]]--; }
		while (c['W'] > 0) { res[2] ++; for (int j = 0; j < sz (w[2]); j++) c[w[2][j]]--; }
		while (c['U'] > 0) { res[4] ++; for (int j = 0; j < sz (w[4]); j++) c[w[4][j]]--; }
		while (c['F'] > 0) { res[5] ++; for (int j = 0; j < sz (w[5]); j++) c[w[5][j]]--; }
		while (c['X'] > 0) { res[6] ++; for (int j = 0; j < sz (w[6]); j++) c[w[6][j]]--; }
		while (c['S'] > 0) { res[7] ++; for (int j = 0; j < sz (w[7]); j++) c[w[7][j]]--; }
		while (c['S'] > 0) { res[7] ++; for (int j = 0; j < sz (w[7]); j++) c[w[7][j]]--; }
		while (c['G'] > 0) { res[8] ++; for (int j = 0; j < sz (w[8]); j++) c[w[8][j]]--; }
		while (c['H'] > 0) { res[3] ++; for (int j = 0; j < sz (w[3]); j++) c[w[3][j]]--; }
		while (c['I'] > 0) { res[9] ++; for (int j = 0; j < sz (w[9]); j++) c[w[9][j]]--; }
		while (c['O'] > 0) { res[1] ++; for (int j = 0; j < sz (w[1]); j++) c[w[1][j]]--; }
		cout << "Case #" << tt << ": ";
		for (int j = 0; j < 10; j++) while (res[j] > 0) { printf ("%d", j); res[j]--; }
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", tt, nt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / tt * nt) / CLOCKS_PER_SEC);
	}
    return 0;
}
