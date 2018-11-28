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
#define FOR(x, l, r) for(x = (l); x <= (r); x++)
#define FORD(x, r, l) for(x = (r); x >= (l); x --)
using namespace std;
map<int, int> mp;
int a[100000], b[100000];
int main()
{
	int tt, cas = 0, ans, l, r, i, j, n, tmp;
	freopen("input.txt", "r", stdin);
	freopen("output", "w", stdout);
	cin >> tt;
	while (tt --) {
		cin >> n;
		FOR(i, 1, n)  {
			scanf("%d", a + i);
			b[i] = a[i];
		}
		sort(b + 1, b + n + 1);
		mp.clear();
		FOR(i, 1, n) mp[b[i]] = i;
		FOR(i, 1, n) {
			a[i] = mp[a[i]];
			//cout << a[i] << " ";
		}
		l = 1; r = n; ans = 0;
		for (i = 1; i <= n; i ++) {
			for (j = 1; j <= n; j ++) if (a[j] == i) break;
			if (j - l < r - j) {
				ans += j - l;  tmp = a[j];
				for (j = j; j > l; j --) a[j] = a[j - 1];
				a[l] = tmp;
				l ++;
			}
			else {
				ans += r - j; tmp = a[j];
				for (j = j; j < r; j ++) a[j] = a[j + 1];
				a[r] = tmp; r --;
			}
			//cout << "yo " << ans << endl;
		}
		printf("Case #%d: ", ++cas);
		cout << ans << endl;
	}
	return 0;
}