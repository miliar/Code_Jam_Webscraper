#include <cstdio>

bool seen[10];
int numSeen;

void count(int n) {
    for (; n > 0; n /= 10) {
        int digit = n % 10;
        if (!seen[digit]) {
            numSeen++;
            seen[digit] = true;
        }
    }
}

int main() {
    int t;
    scanf("%d", &t);
    for (int c = 1; c <= t; c++) {
        for (int i = 0; i < 10; i++) {
            seen[i] = false;
        }
        numSeen = 0;

        int n;
        scanf("%d", &n);

        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", c);
        } else {
            for (int i = 1; ; i++) {
                count(n * i);
                if (numSeen == 10) {
                    printf("Case #%d: %d\n", c, n * i);
                    break;
                }
            }
        }
    }
}
