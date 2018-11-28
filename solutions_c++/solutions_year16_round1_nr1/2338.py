#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
struct _ans {
	int x, y;
} ans[1010];
bool cmp(_ans a, _ans b) {
	return a.x < b.x;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, i;
	char s[1010];
	scanf("%d", &t);
	gets(s);
	for(int x = 1;x<=t;++x) {
		gets(s);
		printf("Case #%d: ", x);
		char c = 'A' - 1;
		int right = 0, left = 0;
		for(i = 0;i<strlen(s);++i) {
			ans[i].y = i;
			if(s[i] >= c) {
				c = s[i];
				ans[i].x = left-1;
				--left;
			}
			else {
				ans[i].x = right;
				++right;
			}
		}
		sort(ans, ans + strlen(s), cmp);
		for(i=0;i<strlen(s);++i)
			printf("%c", s[ans[i].y]);
		printf("\n");
	}
	return 0;
}
