#include <cstdio>

void work() {
	int d, t, a[4], b[4];
	scanf("%d", &d);
	for(int i = 1; i <= 4; i ++)
		if(i == d) {
			for(int j = 0; j < 4; j ++)
				scanf("%d", a + j);
		}
		else for(int j = 0; j < 4; j ++) scanf("%d", &t);
	scanf("%d", &d);
	for(int i = 1; i <= 4; i ++)
		if(i == d) {
			for(int j = 0; j < 4; j ++)
				scanf("%d", b + j);
		}
		else for(int j = 0; j < 4; j ++) scanf("%d", &t);
	int ans = 0, cnt = 0;
	for(int i = 0; i < 4; i ++)
		for(int j = 0; j < 4; j ++)
			if(a[i] == b[j]) cnt ++, ans = a[i];
	if(cnt == 0) printf("Volunteer cheated!\n");
	else if(cnt == 1) printf("%d\n", ans);
	else printf("Bad magician!\n");
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int i  = 1; i <= T; i ++)
		printf("Case #%d: ", i), work();
	return 0;
}
