#include <stdio.h>
#include <string.h>

int T;
int n;
int c;
long long ans[150];


int main()
{
    scanf("%d", &T);
    for (int z = 1; z <= T; z++) {
        scanf("%d%d%*d", &n, &c);
        c--;
        for (int i = 1 ; i <= n ; i++) {
            ans[i] = i;
        }
        while(c--) {
            for (int i = 1 ; i <= n ; i++) {
                ans[i] = (ans[i]-1) * n + i;
            }
        }
        printf("Case #%d:", z);
        for (int i = 1 ; i <= n ; i++) {
            printf(" %lld", ans[i]);
        }
        puts("");
    }
	return 0;
}

