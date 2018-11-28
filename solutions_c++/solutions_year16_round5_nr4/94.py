#include<cstdio>
#include<cstring>
char st[111][111];
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		int n, l;
		scanf("%d%d", &n, &l);
		for(int i(0); i <= n; i++) {
			scanf("%s", st[i]);
		}
		bool flag(true);
		for(int i(0); i < n; i++) {
			if(strcmp(st[i], st[n]) == 0) {
				flag = false;
				break;
			}
		}
		if(flag == false) {
			printf("Case #%d: IMPOSSIBLE\n", qq);
			continue;
		}
		printf("Case #%d: ", qq);
		for(int i(0); i < l; i++) {
			printf("0?");
		}
		printf(" ");
		for(int i(0); i < l * 2 - 1; i++) {
			printf("%c", i % 2 == 1 ? '1' : '0');
		}
		printf("\n");
	}
}
