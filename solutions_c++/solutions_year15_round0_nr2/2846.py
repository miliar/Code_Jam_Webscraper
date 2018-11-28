#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <memory>
#include <queue>

using namespace std;

priority_queue<int> qq;

int a[10000];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test = 0;
	scanf("%d", &test);
	for (int now = 1; now <= test; now++) {
		int n = 0;
		int ans = 0;
		scanf("%d", &n);
		int v = 0;
		// while (!qq.empty()) qq.pop();
		for (int i = 1; i <= n; i++) {
			// int j;
			// scanf("%d", &j);
			// qq.push(j);
			scanf("%d", &a[i]);
			// printf("%d %d", i, a[i]);
			// if (int(log(a[i])/log(2)) > v) v = int(log(a[i])/log(2));
			if (a[i] > ans) ans = a[i];
		}	
		// v = v + 1;
		sort(a + 1, a + 1 + n);
		// for (int i = 1; i <= n; i++) printf("%d", a[i]);
		int ll = 0, rr = ans;
		while (ll + 1 < rr) {

			int mid = (ll + rr) / 2;
			// cout << mid << ' ' << endl;
			int p = 0;
			int qgll = 0, qgrr = mid;
			bool uu = false;
			for (int qgMid = 0; qgMid <= mid - 1; qgMid++) {
				bool u = true;
				int p = 0;
				for (int i = n; i >= 1; i--) {
					if (a[i] > mid - qgMid) {
						p += (a[i] - 1) / (mid - qgMid) ;
						if (p > qgMid) { u = false; break;}
						// s = s - (mid - qgMid);
						// cout << s << ' ' << p << endl;
					} else break;
				}
				if (u) {uu = true;break;}
			}
			if (!uu) ll = mid; else rr = mid;
		}
		// int p = 0;
		// int ans = qq.top();
		// for (int i = 1; i <= qq.top(); i++) {
		// 	int w = qq.top();
		// 	qq.pop();
		// 	qq.push((w+1)/2); qq.push(w/2);
		// 	w = qq.top();
		// 	if (w + i < ans) ans = w + i;
		// }
		printf("Case #%d: %d\n", now, rr);
	}
	return 0;
}