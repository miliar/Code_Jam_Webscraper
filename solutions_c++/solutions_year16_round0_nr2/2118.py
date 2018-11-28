#include <cstdio>

const int LARGE_S = 100;

int main(int argc, char *argv[]) {
    int T;
    std::scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        char cake_str[LARGE_S + 1];
        std::scanf("%s", cake_str);

        char specials[] = {'-', '+', '\0'};
        char last = cake_str[0];
        int i = 1, r = 1;
        while (cake_str[i] != specials[2]) {
            if (cake_str[i] != last) {
                ++r;
                last = cake_str[i];
            }
            ++i;
        }

        if (cake_str[i - 1] == specials[1]) {
            std::printf("Case #%d: %d\n", t, r - 1);
        } else {
            std::printf("Case #%d: %d\n", t, r);
        }
    }

    return 0;
}