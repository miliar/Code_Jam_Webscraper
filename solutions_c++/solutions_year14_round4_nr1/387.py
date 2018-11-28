#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define ll long long
#define pb push_back 
#define mp make_pair
#define FOR(x, l, r) for(x = (l); x <= (r); x++)
#define FORD(x, r, l) for(x = (r); x >= (l); x --)
using namespace std;
int a[100000];
int main()
{
	int tt, cas = 0, ans, i, m, t, w, n;
	freopen("input.txt", "r", stdin);
	freopen("output", "w", stdout);
	cin >> tt;
	while (tt --) {
		cin >> n >> m;
		FOR(i, 1, n) scanf("%d", a + i);
		sort(a + 1, a + n + 1);
		t = 1; w = n; ans = 0;
		while (t <= w) {
			if (a[t] + a[w] <= m) w--, t ++;
				else w --;
			ans ++;
		}
		printf("Case #%d: ", ++cas);
		cout << ans << endl;
	}
	return 0;
}