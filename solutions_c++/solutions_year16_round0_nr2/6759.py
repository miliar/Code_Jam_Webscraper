#include <cstdio>
using namespace std;
int main()
{
    int t, i, len;
    char s[105];
    scanf("%d", &t);
    for (int k = 1; k <= t; k++) {
        scanf("%s", s);
        printf("Case #%d: ", k);
        len = -1;
        while (s[++len] != '\0');
        int count = 0;
        while (len > 0) {
            for (i = len - 1; i >= 0; i--)
                if (s[i] != '+')
                    break;
            len = i + 1;
            if (len > 0) {
                for (i = len - 1; i >= 0; i--) {
                    if (s[i] == '+')
                        s[i] = '-';
                    else
                        s[i] = '+';
                }
                count++;
            }
        }
        printf("%d\n", count);
    }
    return 0;
}
