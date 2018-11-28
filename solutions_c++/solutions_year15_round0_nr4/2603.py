#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

char* Richard = "RICHARD";
char* Gabriel = "GABRIEL";

int T, t;
int X, R, C;

char* solve() {
    if (X == 1) {
        return Gabriel;
    }
    if (X == 2) {
        if (R == 1 && C == 1) {
            return Richard;
        }
        int odd = (R * C) & 1;
        return odd ? Richard : Gabriel;
    }
    if (X == 3) {
        if (R == 2 && C == 3) {
            return Gabriel;
        }
        if (R == 3 && C == 2) {
            return Gabriel;
        }
        if (R == 3 && C == 3) {
            return Gabriel;
        }
        if (R == 3 && C == 4) {
            return Gabriel;
        }
        if (R == 4 && C == 3) {
            return Gabriel;
        }
        return Richard;
    }
    if (X == 4) {
        if (R == 1 || C == 1) {
            return Richard;
        }
        if (R == 2 || C == 2) {
            return Richard;
        }
        if (R == 3 && C == 4) {
            return Gabriel;
        }
        if (R == 4 && C == 3) {
            return Gabriel;
        }
        if (R == 4 && C == 4) {
            return Gabriel;
        }
    }
    return Richard;
}

int main() {
    scanf("%d", &T);

    for (t = 1; t <= T; t++) {
        int r, c;
        scanf("%d%d%d", &X, &r, &c);
        R = min(r, c);
        C = max(r, c);
        printf("Case #%d: %s\n", t, solve());
    }

    return 0;
}
