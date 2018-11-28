#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
const int N(222);
int a[N][N], f[N], b[N][N];
char st[N];
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		int n;
		scanf("%d", &n);
		for(int i(0); i < n; i++) {
			scanf("%s", st);
			for(int j(0); j < n; j++) {
				a[i][j] = st[j] == '1';
			}
		}
		int ans(1e9);

		for(int msk(0); msk < (1 << n * n); msk++) {
			int x(msk);
			bool flag(true);
			int cost(0);
			for(int i(0); i < n && flag; i++) {
				for(int j(0); j < n && flag; j++) {
					int y(x % 2);
					x /= 2;
					if(y == 0 && a[i][j] == 1) {
						flag = false;
						break;
					}
					b[i][j] = a[i][j] | y;
					if(y == 1 && a[i][j] == 0) {
						cost++;
					}
				}
			}
			if(!flag) {
				continue;
			}
			flag = true;
			for(int i(0); i < n; i++) {
				int cnt(0);
				for(int j(0); j < n; j++) {
					f[j] = 0;
				}
				for(int j(0); j < n; j++) {
					if(b[i][j] == 1) {
						cnt++;
						for(int k(0); k < n; k++) {
							f[k] += b[k][j];
						}
					}
				}
				bool ok(true);
				int cnt1(0);
				for(int j(0); j < n; j++) {
					if(f[j] != 0 && f[j] != cnt) {
						ok = false;
						break;
					}else {
						if(f[j] == cnt) {
							cnt1++;
						}
					}
				}
				if(cnt1 != cnt) {
					ok = false;
				}
				if(!ok) {
					flag = false;
					break;
				}
			}
			if(flag && ans > cost) {
				ans = cost;
			}
		}
		printf("Case #%d: %d\n", qq, ans);
	}
}
