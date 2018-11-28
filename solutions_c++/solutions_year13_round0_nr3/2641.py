#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz(v) (int)v.size()
#define clr(x, v) memset(x, v, sizeof(x))
#define rep(i, l, u) for(int i = (l); i < (u); i++)
#define repv(i, v) for(i = 0; i < (int)v.size(); i++)
#define repi(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)


int trans (int x) {
	int i, k = 0;
	while (x != 0) {
		k = k * 10 + (x % 10);
		x /= 10;
	}
	return k;
}

int main () {
	int i, j, k;
	int T, ca;
	int pool[1011], cnt = 0;

	freopen ("C-small-attempt0.in", "r", stdin);
	freopen ("C-small-attempt0.txt", "w", stdout);

	for (i = 1; i <= 1000; ++i) {
		int j = (int) sqrt(i);
		if (j * j == i && trans(j) == j && trans(i) == i) {
			//	printf ("%d\n", i);
			pool[++cnt] = i;
		}
	}

	for (scanf ("%d", &T), ca = 1; ca <= T; ++ca) {
		scanf ("%d%d", &i, &j);
		int ans = 0;
		for (k = 1; k <= cnt; ++k)
			if (pool[k] >= i && pool[k] <= j)
				ans ++;
		printf ("Case #%d: %d\n", ca, ans);
	}
	return 0;
}
	 
