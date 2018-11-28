#include <cstdio>
#include <algorithm>
using namespace std;

const int INF = 200000000;
const int N = 105;

int a, n, v[N], f[N][N];

int gao(int cas) {
	scanf("%d%d", &a, &n);
	for(int i=1; i<=n; ++i) scanf("%d", v+i);
	sort(v+1, v+n+1);
	f[0][0] = a;
	for(int i=1; i<=n; ++i) {
		f[0][i] = min(INF, f[0][i-1]*2-1);
	}
	for(int i=1; i<=n; ++i) {
		for(int j=0; j<=n; ++j) {
			if(f[i-1][j] > v[i]) {
				f[i][j] = min(INF, f[i-1][j]+v[i]);
			} else {
				f[i][j] = j ? f[i-1][j-1] : 0;
			}
			if(j) f[i][j] = max(f[i][j], min(INF,f[i][j-1]*2-1));
		}
	}
	for(int i=0; i<=n; ++i) {
		if(f[n][i]) return i;
	}
	return n;
}

int main() {
	int T; scanf("%d", &T);
	for(int cas=1; cas<=T; ++cas) {
		printf("Case #%d: %d\n", cas, gao(cas));
	}
}
