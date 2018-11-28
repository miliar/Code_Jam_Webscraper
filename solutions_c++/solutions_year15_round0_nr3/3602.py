#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int T;
char str[10010];
int myhash(char x) {
    if (x == 'i') return 2;
    if (x == 'j') return 3;
    if (x == 'k') return 4;
    return 0;
}
int calc(int x, int y) {
    if (x == 1 || x == -1) {
        return x * y;
    }
    if (x == 2) {
        int opr = (x > 0) ? 1 : -1;
        switch (y) {
            case 2:
                return -1 * opr;
            case 3:
                return 4 * opr;
            case 4:
                return -3 * opr;
        }
    }
    if (x == -2) {
        int opr = (x > 0) ? 1 : -1;
        switch (y) {
            case 2:
                return -1 * opr;
            case 3:
                return 4 * opr;
            case 4:
                return -3 * opr;
        }
    }
    if (x == 3) {
        int opr = (x > 0) ? 1 : -1;
        switch (y) {
            case 2:
                return -4 * opr;
            case 3:
                return -1 * opr;
            case 4:
                return 2 * opr;
        }
    }
    if (x == -3) {
        int opr = (x > 0) ? 1 : -1;
        switch (y) {
            case 2:
                return -4 * opr;
            case 3:
                return -1 * opr;
            case 4:
                return 2 * opr;
        }
    }
    if (x == 4) {
        int opr = (x > 0) ? 1 : -1;
        switch (y) {
            case 2:
                return 3 * opr;
            case 3:
                return -2 * opr;
            case 4:
                return -1 * opr;
        }
    }
    if (x == -4) {
        int opr = (x > 0) ? 1 : -1;
        switch (y) {
            case 2:
                return 3 * opr;
            case 3:
                return -2 * opr;
            case 4:
                return -1 * opr;
        }
    }
    return 0;
}
int main() {
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int l, x;
        scanf("%d%d", &l, &x);
        scanf("%s", str);
        int now = 1;
        int state = 0;
        for (int i = 0; i < x; ++i) {
            for (int j = 0; j < strlen(str); ++j) {
                now = calc(now, myhash(str[j]));
                if (now == state + 2) {
                    ++state;
                    now = 1;
                }
            }
        }
        bool flag = (state == 3 && now == 1);
        printf("Case #%d: %s\n", ca, flag ? "YES" : "NO");
    }
    return 0;
}
