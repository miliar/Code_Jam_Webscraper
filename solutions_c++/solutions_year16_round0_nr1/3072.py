#include <stdio.h>
#include <string.h>

int T;
int n;
int flag[10];

int check(int x)
{
    while (x > 0) {
        flag[x % 10] = 1;
        x /= 10;
    }
    for (int i = 0; i < 10 ; i++) {
        if (!flag[i]) {
            return 0;
        }
    }
    return 1;
}

int main()
{
    scanf("%d", &T);
    for (int z = 1; z <= T; z++) {
        scanf("%d", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", z);
            continue;
        }
        memset(flag, 0, sizeof(flag));
        for (int i = 1; ; i++) {
            if (check(i * n)) {
                printf("Case #%d: %d\n", z, i * n);
                break;
            }
        }
    }
	return 0;
}

