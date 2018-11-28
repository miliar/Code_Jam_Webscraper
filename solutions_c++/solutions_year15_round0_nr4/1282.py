#include <bits/stdc++.h>

int main()
{
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int X, R, C; scanf("%d%d%d", &X, &R, &C);
        bool win = true;
        if (R > C) std::swap(R, C);
        if (X == 1) win = true;
        else if (X == 2) win = ((R*C) % 2 == 0);
        else if (X == 3) win = ((R == 2 && C == 3) || (R == 3 && C == 3) || (R == 3 && C == 4));
        else win = ((R >= 3) && C == 4);
        printf("Case #%d: %s\n", t, win ? "GABRIEL" : "RICHARD");
    }
}

