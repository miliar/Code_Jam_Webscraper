#include <stdio.h>
#include <string.h>

int T;
char str[1100];
int k;


int main()
{
    scanf("%d", &T);
    for (int z = 1; z <= T; z++) {
        scanf("%s%d", str, &k);

        int ans = 0;
        int len = strlen(str);

        for (int i = 0; str[i] != '\0'; i++) {
            if (str[i] == '-') {
                if (i + k > len) {
                    ans = -1;
                    break;
                }

                for (int j = 0; j < k; j++) {
                    str[i + j] = (str[i + j] == '-' ? '+' : '-');
                }
                ans ++;
            }
        }

        if (ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", z);
        } else {
            printf("Case #%d: %d\n", z, ans);
        }
    }
    
	return 0;
}

