#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int n, m;
int b[1000], e[1000], p[1000];

void input() {
	scanf("%d%d", &n, &m);
	for(int i = 0;i < m;i ++) scanf("%d%d%d", &b[i], &e[i], &p[i]);
}

void solve() {
	char vis[1000];
	memset(vis, 0, sizeof(vis));
	long long res = 0;
	while(1) {
		int id = -1;
		for(int i = 0;i < m;i ++) if(vis[i] == 0) {
			if(id == -1||e[i] < e[id]||e[i] == e[id]&&b[i] < b[id]) id = i;
		}
		if(id == -1) break;

		int id2 = -1;
		for(int i = 0;i < m;i ++) if(vis[i] == 0&&b[i] <= e[id]&&b[i] > b[id]&&e[i] > e[id]) {
			if(id2 == -1||b[i] > b[id2]) id2 = i;
		}

		if(id2 == -1) vis[id] = 1;
		else {
			int tp = p[id];
			if(p[id2] < tp) tp = p[id2];
			res += (((((long long)(b[id2]-b[id]))*((long long)(e[id2]-e[id])))%1000002013)*((long long)tp))%1000002013;
			res %= 1000002013;

			if(p[id] == tp) {
				e[id] = e[id2];
				p[id2] -= tp;
			}
			else {
				b[id2] = b[id];
				p[id] -= tp;
			}

			if(p[id] == 0) vis[id] = 1;
			if(p[id2] == 0) vis[id2] = 1;
		}
	}

	printf("%lld\n", res);
}

int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t = 1;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}