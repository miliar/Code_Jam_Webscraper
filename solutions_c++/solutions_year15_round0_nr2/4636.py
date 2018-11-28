#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <ctime>
#include <cstring>
#include <sstream>

//#include <unordered_map>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<pii, pii> ppii;
typedef vector<int> vi;


#define SI(n) scanf("%d", &n)
#define SII(x, y) scanf("%d%d", &x, &y)
#define SD(n) scanf("%lf", &n)
#define SPII(n) scanf("%d%d", &n.first, &n.second)
#define FI(n) for (int i=0; i<n; i++)
#define WS(n) while(SI(n) != EOF && n)
#define DB(n) cout<<#n<<" = "<<n<<" ";
#define DBN(n) cout<<#n<<" = "<<n<<"\n";
#define FIX(n) cout.precision(2), cout.setf(cout.fixed)
#define PI(n) printf("%d", n)
#define SPACE() putchar(' ')
#define ENDL() putchar('\n')

char s[1000001];
int a[1001];

int get_ans(int x, int lvl) {
	if (x <= lvl)
		return 0;
	return  x / lvl - (x%lvl == 0);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	

	int t;
	SI(t);
	for (int i = 1; i <= t; i++) {
		int n;
		SI(n);
		int mx = 0;
		map<int, int> mp;
		for (int i = 0; i < n; i++) {
			int x;
			SI(a[i]);
			mx = max(mx, a[i]);
		}

		int l = 1, r = mx;
		while (l != r) {
			int m = (l + r) >> 1;
			int m1 = (l + m) >> 1;
			int m2 = r - m1 + l;
			//for (int z = 1, end = mx; z <= end; z++) {
			int al = l;
			int ar = r;
			int am1 = m1;
			int am2 = m2;

			for (int j = 0; j < n; j++) {
				al += get_ans(a[j], l);
				am1 += get_ans(a[j], m1);
				am2 += get_ans(a[j], m2);
				ar += get_ans(a[j], r);
			}
			mx = min(al, mx);
			mx = min(am1, mx);
			mx = min(am2, mx);
			mx = min(ar, mx);


			if (al <= am1 && am1 <= am2) {
				r = m2 - 1;
			}
			else if (al >= am1 && am2 <= ar) {
				l = m1;
				r = m2 - 1;
			}
			else {
				l = m1;
			}
		//DB(l); DB(m1); DB(m2); DBN(r);
			//			DB(z); DBN(cr);
			//		}
		}

		printf("Case #%d: %d\n", i, mx);
	}

	return 0;
}