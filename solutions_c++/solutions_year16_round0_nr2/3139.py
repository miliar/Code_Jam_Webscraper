#include <stdio.h>
#include <string.h>

int T;
char str[1000];
int n;
int ans;

void flip (int x)
{
    for (int i = 0; i*2 < x; i++) {
        char t = str[i];
        str[i] = str[x-i] == '+' ? '-' : '+';
        str[x-i] = t == '+' ? '-' : '+';
    }
    if (x % 2 == 0) {
        str[x/2] = str[x/2] == '+' ? '-' : '+';
    }
    ans++;
}

int main()
{
    scanf("%d", &T);
    for (int z = 1; z <= T; z++) {
        scanf("%s", str);
        n = strlen(str);
        ans = 0;

        while(n--) {
            if (str[n] == '+') {
                continue;
            } else {
                if (str[0] == '+') {
                    for (int i = 0; i < n ; i++) {
                        if (str[i + 1] == '-') {
                            flip(i);
                            break;
                        }
                    }
                }
                flip(n);
            }
        }

        printf("Case #%d: %d\n", z, ans);
    }
	return 0;
}

