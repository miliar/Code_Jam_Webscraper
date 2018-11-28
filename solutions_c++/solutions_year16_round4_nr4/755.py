//batch scheduling 2002
#include <bits/stdc++.h>
#include <vector>
#include <cstdio>
#include <deque>
#include <iostream>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < n; i++)
#define re return
#define sz(a) (int)a.size()
#define fi first
#define se second
#define mp(a, b) make_pair(a, b)
typedef long long ll;
typedef double ld;
typedef pair<ld, ld> pld;
typedef vector<ll> vi;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
const ll cnn = 800, sz_g = 200000, inf = 1000000000LL, mod2 = 5000000, /*mod = inf + 7, */ma = 128 * 1024;
int t, n, r, p, s, a[4][4], use[4], b[4][4], ans = 0;

void my_assert(bool ok) {
	if (!ok) while(true);	
}
vector<int> kk;

bool ok(int nu) {
	if (nu == n) re true;
	int kp = 0; 
	forn (i, n)
		if (use[i] == 0 && b[kk[nu]][i] == 1) {
			use[i] = 1;
			kp++;
			if (!ok(nu + 1)) re false;
			use[i] = 0;
		}
	if (kp == 0) re false;
	re true;
}

bool okk() {
	kk.resize(0);
	forn (i, n) kk.push_back(i);
	do {
		forn (i, 4) use[i] = 0;
		if (!ok(0)) {
			re false;
		}
	} while (next_permutation(kk.begin(), kk.end()));
	re true;
}


void fc(int i, int j, int kk) {
	if (kk >= ans) re;
	if (i == n) {
		/*cout << kk << endl;
		forn (i, n) {
			forn (j, n)
				cout << b[i][j] << " ";
			cout << endl;
		}		
		cout << endl;*/
		if (okk()) ans = min(ans, kk);
		re;
	}
	if (a[i][j] == 1) {
		b[i][j] = 1;
		fc(i + (j + 1) / n, (j + 1) % n, kk);
		b[i][j] = 0;
		re;
	}
	b[i][j] = 0;
	fc(i + (j + 1) / n, (j + 1) % n, kk);
	b[i][j] = 1;
	fc(i + (j + 1) / n, (j + 1) % n, kk + 1);
	b[i][j] = 0;
}

int main() {
	//iostream::sync_with_stdio(0), cin.tie(0);
	freopen("sum.in", "r", stdin);
	freopen("sum.out", "w", stdout);
	int t;
	cin >> t;
	forn (i, t) {
		cin >> n;
		ans = n * n;
		forn (i, n) {
			string s;
			cin >> s;
			forn (j, n)
				a[i][j] = s[j] - '0';
		}
		fc(0, 0, 0);
		cout << "Case #" << i + 1 << ": " << ans << "\n";
	}	
	re 0;
}  