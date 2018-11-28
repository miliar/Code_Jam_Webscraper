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

using namespace std;

__int64 a[1005];

vector<pair<__int64, int> > p;
int main() {
	int i, j, k, n;
	__int64 m, up, down, mid;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%I64d", &n, &m);
		for (i = 0; i < n; ++i)
			scanf("%I64d", &a[i]);
		up = 200000LL * 1000000000LL;
		down = 0;
		while (up - down > 0) {
			mid = (up + down) / 2;
			__int64 cnt = 0;
			for (i = 0; i < n; ++i) {
				cnt += (mid + a[i]) / a[i];
			}
			if (cnt >= m)
				up = mid;
			else
				down = mid + 1;
		}
		//cout << up << " " << down << endl;
		__int64 cnt = m - 1;
		for (i = 0; i < n; ++i) {
			cnt -= up / a[i];
		}
		//cout << cnt << endl;
		p.clear();
		for (i = 0; i < n; ++i) {
			p.push_back(make_pair(-(up % a[i]), i));
		}
		sort(p.begin(), p.end());
		printf("Case #%d: %d\n", cas, p[cnt].second + 1);
	}
}
/*
 #include <iostream>
 #include <cmath>
 #include <string>
 #include <algorithm>
 #include <cstdio>
 #include <vector>
 #include <queue>
 #include <cstring>
 using namespace std;
 typedef long long LL;
 const int N = 1005;
 const int MOD = 100007;
 int n , a[N] , m;

 bool check (LL t) {
 LL cut = 0;
 for (int i = 0 ; i < n ; i ++) {
 cut += (t + a[i] - 1) / a[i];
 }
 return cut >= m;
 }
 vector <pair <int , int> > v;
 int gao (LL t) {
 v.clear ();
 int cut = m;
 for (int i = 0 ; i < n ; i ++) {
 cut -= (t - 1) / a[i];
 v.push_back (make_pair ((t - 1) / a[i] * a[i] , i + 1));
 }
 sort (v.begin () , v.end ());
 for (int i = 0 ; i < n ; i ++) {
 cut --;
 if (cut == 0) {
 return v[i].second;
 }
 }
 }
 int main () {
 // freopen ("input.txt" , "r" , stdin);
 // freopen ("output.txt" , "w" , stdout);
 int t , cas = 0;scanf ("%d" , &t);
 while (t --) {
 scanf ("%d %d" , &n , &m);
 for (int i = 0 ; i < n ; i ++)
 scanf ("%d" , a + i);
 LL low = 0 , high = (LL)1e14 , mid , ans;
 while (low <= high) {
 mid = (low + high) >> 1;
 if (check (mid)) {
 ans = mid;
 high = mid - 1;
 }
 else low = mid + 1;
 }
 printf ("Case #%d: %d\n" , ++ cas , gao (ans));
 }
 return 0;
 }

 */
