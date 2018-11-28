#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <climits>
#include <complex>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <bitset>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <cmath>

using namespace std;

int n;
bool vis[11];

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int _ = 1; _ <= T; _++) {
		printf("Case #%d: ", _);
		memset(vis, 0, sizeof(vis));
		scanf("%d", &n);
		if(n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		int cnt = 0, ans = 0;
		int nn = n;
		int k = 2, p, pre = n;
		while(1) {
			int t = n;
			if(cnt == 10) {
				ans = pre;
				break;
			}
			while(t) {
				p = t % 10;
				// printf("%d\n", p);
				if(!vis[p]) {
					vis[p] = 1;
					cnt++;
				}
				t /= 10;
			}
			n = k * nn;
			pre = (k - 1) * nn;
			k++;
		}
		printf("%d\n", ans);
	}
	return 0;
}