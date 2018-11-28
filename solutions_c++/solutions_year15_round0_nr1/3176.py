#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;
char s[1010];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int _;
	scanf("%d", &_);
	for(int ca = 1; ca <= _; ++ca) {
		int d, ans = 0, pre = 0;
		scanf("%d", &d);
		scanf("%s", s);
		for(int i = 0; i <= d; ++i) {
			int u = s[i] - '0';
			if(!u) continue;
			if(i > pre) {
				ans += i - pre;
				pre = i + u;
			}
			else {
				pre += u;
			}
		}
		printf("Case #%d: %d\n", ca, ans);
	}
	return 0;
}