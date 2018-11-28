#include <cstdio>

char pancakes[105];

int main() {
    int t;
    scanf("%d\n", &t);
    for (int c = 1; c <= t; c++) {
        fgets(pancakes, sizeof(pancakes), stdin);
        int prev = 0;
        int cur = 0;
        int flips = 0;
        while (pancakes[cur] != '\n') {
            for (cur = prev; pancakes[cur] == pancakes[prev]; cur++);
            flips++;
            prev = cur;
        }

        if (pancakes[cur - 1] == '-') {
            flips++;
        }
        printf("Case #%d: %d\n", c, flips - 1);
    }
}

