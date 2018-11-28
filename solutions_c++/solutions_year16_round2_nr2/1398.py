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


int main () {
//	freopen (filename".in", "r", stdin);
//	freopen (filename".out", "w", stdout);	
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++) {
		string s, t;
		cin >> s >> t;
		int ans = 1000;
		int pi = -1, pj = -1;
		int len = sz (s);
		int st = 1;
		for (int i = 0; i < len; i++) st *= 10;
		for (int i = 0; i < st; i++) {
			for (int j = 0; j < st; j++) {
				int l = i, c1 = 0, c2 = 0;
				for (int q = 0; q < len; q++) { if ((l % 10 == s[len - q - 1] - '0') || s[len - q - 1] == '?') c1++; l /= 10; }
				l = j;
				for (int q = 0; q < len; q++) { if ((l % 10 == t[len - q - 1] - '0') || t[len - q - 1] == '?') c2++; l /= 10; }
				if (c1 == len && c2 == len) {
					if (ans > abs (i - j)) {
						ans = abs (i - j);
						pi = i;
						pj = j;
					}
				}
			}
		}

		cout << "Case #" << tt << ": ";
		printf (("%0" + to_string(len) + "d %0" + to_string(len) + "d").c_str(), pi, pj);
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", tt, nt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / tt * nt) / CLOCKS_PER_SEC);
	}
    return 0;
}
