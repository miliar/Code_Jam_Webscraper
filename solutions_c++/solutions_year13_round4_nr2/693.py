#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
using namespace std;
typedef long long ll;
int const maxn = 10010;
int mi[maxn], mx[maxn];
int main() {
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-ans1.txt", "w", stdout);
	freopen("B-large.in", "r", stdin);  freopen("B-large-ans.txt", "w", stdout);
	int T, ca = 1;
	int n;
	ll p;
	for (scanf("%d", &T); T--; ) {
		scanf("%d%lld", &n, &p);
		ll m = 1LL << n;
		//mi[0] = 0, mx[m - 1] = m - 1;
		//int cc = 1, dd = m - 1, now = 1, len = (1 << n) >> 1;
		//for (int i = 0; i < n; ++i) {
			//for (int j = 0; j < len; ++j) {
				//mi[cc++] = now;
				//mx[--dd] = m - 1 - now;
			//}
			//len >>= 1;
			//now = now * 2 + 1;
		//}
		
		ll y = 0, z = 0;
		bool flag = false;
		if (m - 1 < p) {
			flag = true;
			y = m - 1;
		}
		ll cc = 1, dd = m - 1, now = 1, len = (1LL << n) >> 1;
		for (int i = 0; i < n; ++i) {
			if (now < p) z = cc + len - 1;
			if (!flag && m - 1 - now < p) {
				flag = true;
				y = dd - 1;
			}
			cc += len;
			dd -= len;
			len >>= 1;
			now = now * 2LL + 1;
		}
		
		//for (int i = 0; i < m; ++i) {
			//cout << mi[i] << " " << mx[i] << endl;
		//}
		//for (int i = 0; i < m; ++i) {
			//if (mx[i] < p) y = i;
			//if (mi[i] < p) z = i;	
		//}
		//for (int i = 0; i < m; ++i) cout << mi[i] << " " << mx[i] << endl;
		printf("Case #%d: %lld %lld\n", ca++, y, z);	
	}
	return 0;
}


