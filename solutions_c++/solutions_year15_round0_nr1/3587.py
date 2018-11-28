#include <cstdio>

int main() {
    int cases;
    scanf("%d", &cases);
    for (int c = 1; c <= cases; c++) {
        int len;
        char str[1010];
        scanf("%d %s", &len, str);
        int sum = str[0] - '0',
            friends = 0;
        for (int i = 1; i <= len; i++) {
            if (sum + friends < i)
                friends += i - (sum + friends);
            sum += str[i] - '0';
        }

        printf("Case #%d: %d\n", c, friends);
    }
    return 0;
}
