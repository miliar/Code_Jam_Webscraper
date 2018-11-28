#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);
	for (int tn = 1; tn <= T; tn++) {
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", tn);
        for (int i = 1; i <= s; i++)
            printf(" %d", i);
        puts("");
	}
}