#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <string>

#define FOR(i, s, e) for (int i=(s);i<(e);i++)
#define FOE(i, s, e) for (int i=(s);i<=(e);i++)
#define FOD(i, s, e) for (int i=(s)-1;i>=(e);i--)
#define CLR(x, a) memset(x, a, sizeof(x))
#define LL long long int
using namespace std;
#define N 1005

int n, TC, p[N], a[N];

void solve(int tc) {
	scanf("%d", &n);
	int mx = 0, ret = 2000 * 2000;
	FOR(i, 0, n){
		scanf("%d", &p[i]);
		mx = max(mx, p[i]);
	}
	
	if (mx == 0) ret = 0;
	else {
		FOE(i, 1, mx) {
			int cnt = 0;
			FOR(j, 0, n) a[j] = p[j];
			FOR(j, 0, n) cnt += (p[j] - 1) / i;
			ret = min(ret, cnt + i);
		}
	}
	printf("Case #%d: %d\n", tc, ret);
}

int main(){
	scanf("%d", &TC);
	FOE(i, 1, TC) solve(i);
	return 0;
}

