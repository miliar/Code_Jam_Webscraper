#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < (n); i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define fill(x,y) memset(x,y,sizeof(x))
                         
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { re x > 0 ? x : -x; }

const int MAX = 10000000;

int n;
int m;
ll l, r;
int f[MAX + 1];

int pal (ll x) {
	int n = 0;
	int y[20];
	while (x) {
		y[n++] = x % 10;
		x /= 10;
	}
	for (int i = 0, j = n - 1; i < j; i++, j--)
		if (y[i] != y[j])
			re 0;
	re 1;
}

ll q[100];

int main () {
	int k = 0;
	for (int i = 1; i <= MAX; i++)
		if (pal (i) && pal ((ll)i * i)) {
			f[i] = 1;
			q[k++] = (ll)i * i;
//			cout << (ll)i << endl;
		}	
	int tt;
	cin >> tt;
	for (int it = 1; it <= tt; it++) {
		cin >> l >> r;
		int ans = 0;
		for (int i = 0; i < k; i++)
			if (q[i] >= l && q[i] <= r)
				ans++;
		cout << "Case #" << it << ": " << ans;

		cout << endl;
		if (it % 100 == 0)
			cerr << it << " / " << tt << " " << clock () << endl;
	}
	return 0;
}