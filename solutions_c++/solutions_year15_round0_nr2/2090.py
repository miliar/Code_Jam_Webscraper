#include<cstdio>
#include<algorithm>
#include<cmath>

#define N 1005
using namespace std;

int main(){
	int tcc;
	scanf("%d", &tcc);
	int table[N], data[N];
	for (int tc = 1; tc<=tcc; tc++) {
		int n;
		scanf("%d", &n);
		int maxx = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &data[i]);
			maxx = max(maxx, data[i]);
		}
		int ans = maxx;
		for (int i = 1; i < maxx; i++) {
			int cnt = 0;
			for (int j = 0; j < n; j++) {
				if (data[j] > i) {
					cnt += ceil((double)data[j]/i)-1;
				}
			}
			//printf("ans:%d i:%d cnt: %d cnt+i: %d\n", ans, i, cnt, cnt + i);
			ans = min(ans, cnt + i);
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
