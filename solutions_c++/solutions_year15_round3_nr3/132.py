#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 105;
const int MOD = 10000007;
int a[N];
int main () {
	freopen ("input.txt" , "r" , stdin);
	freopen ("output.txt" , "w" , stdout);
	int t , cas = 0;scanf ("%d" , &t);
	while (t --) {
		int c , d , v;
		scanf ("%d %d %d" , &c , &d , &v);
		for (int i = 0 ; i < d ; i ++)
			scanf ("%d" , a + i);
		sort (a , a + d);
		int ans = 0;
		LL now = 0;
		for (int i = 0 ; i < d ; i ++) {
			while (now + 1 < a[i] && now < v) {
				ans ++;
				now += (now + 1) * 1LL * c;
			}
			if (now < v) now += a[i] * 1LL * c;
		}
		while (now < v) {
			now += (now + 1) * 1LL * c;
			ans ++;
		}
		printf ("Case #%d: %d\n" , ++ cas , ans);
	}
	return 0;
}