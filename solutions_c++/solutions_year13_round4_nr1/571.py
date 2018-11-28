#include <cstdio>
#include <algorithm>
#include <cstring>
#define fill(a) memset(a, 0, sizeof a)
using namespace std;
int n, m, p, q, x, y, z, i, l[111], r[111], cur[111], ans;
int T,cas;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++){
		fill(l); fill(r); fill(cur);
		ans = 0;
		scanf("%d%d", &n, &m);
		for (i = 1; i <= m; i++){
			scanf("%d%d%d", &x, &y, &z);
			l[x] += z;  r[y] += z; q = y - x;
			ans += z * (21 - q) * q / 2;
		}
		for (i = 1; i <= n; i++){
			cur[i] += l[i]; x = r[i]; y = i;
			for (;x; y--){
				z = min(x, cur[y]);
				q = i - y;
				ans -= z * (21 - q) * q / 2;
				x -= z; cur[y] -= z;
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}
