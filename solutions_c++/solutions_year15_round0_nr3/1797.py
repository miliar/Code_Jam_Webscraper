#include <bits/stdc++.h>

using namespace std;

int sgn(int n) { return n > 0 ? 1 : -1; }

int op(int x, int y) {
    static const int gg[5][5] = {
        {0, 0, 0, 0, 0},
        {0, 1, 2, 3, 4},
        {0, 2, -1, 4, -3},
        {0, 3, -4, -1, 2},
        {0, 4, 3, -2, -1}
    };

    int s = sgn(x) * sgn(y);

    return s * gg[abs(x)][abs(y)];
}

char *str; int l, X;
int totalL;

bool step(int &v, int &idx, int d) {
    if (idx < 0 or idx >= totalL) return false;

    if (d == 1)
        v = op(v, str[idx % l]);
    else
        v = op(str[idx % l], v);

    idx += d;

    return true;
}

bool jizzJIZZ();
bool jizz() {
    scanf("%d%d", &l, &X);
    totalL = l * X;
    str = new char [l+1];
    scanf("%s", str);

    for (int i = 0; i < l; ++i)
        str[i] -= 'i' - 2;

    bool ans = jizzJIZZ();

    delete [] str;

    return ans;
}

bool jizzJIZZ() {
    int idx_i = 0, idx_k = totalL - 1;

    for (int v = 1; v != 2; )
        if (not step(v, idx_i, 1))
            return false;

    for (int v = 1; v != 4; )
        if (not step(v, idx_k, -1))
            return false;

    int left = idx_k - idx_i + 1;
    if (left < 0) return false;

    left %= 4 * l;

    int v = 1;
    while (left--) step(v, idx_i, 1);

    return v == 3;
}

int main() {
    int T; scanf("%d", &T); for (int t = 1; t <= T; ++t)
         printf("Case #%d: %s\n", t, jizz() ? "YES" : "NO");

    return 0;
}