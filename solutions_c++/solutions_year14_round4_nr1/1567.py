#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int cnt[750];

int main() {
	int T, t = 0;
	scanf(" %d", &T);
	while(T --) {
		t ++;
		int n, x;
		scanf(" %d %d", &n, &x);
		for(int i = 0; i < n; i ++) {
			int p;
			scanf(" %d", &p);
			cnt[p] ++;
		}
		int ans = 0;
		for(int i = x; i >= 1; i --) {
			while(cnt[i] != 0) {
				cnt[i] --;
				ans ++;
				for(int j = x - i; j >= 1; j --) {
					if(cnt[j]) {
						cnt[j] --;
						break;
					}
				}
			}
		}
		memset(cnt, 0, sizeof(cnt));
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
