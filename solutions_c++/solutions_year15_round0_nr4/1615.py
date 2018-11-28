#include <stdio.h>

char gab[] = "GABRIEL";
char ric[] = "RICHARD";

char* soln[4][4][4] =
{
    {// x = 1
        {gab, gab, gab, gab,},
        {gab, gab, gab, gab,},
        {gab, gab, gab, gab,},
        {gab, gab, gab, gab,},
    },
    {// x = 2
        {ric, gab, ric, gab,},
        {gab, gab, gab, gab,},
        {ric, gab, ric, gab,},
        {gab, gab, gab, gab,},
    },
    {// x = 3
        {ric, ric, ric, ric,},
        {ric, ric, gab, ric,},
        {ric, gab, gab, gab,},
        {ric, ric, gab, ric,},
    },
    {// x = 4
        {ric, ric, ric, ric,},
        {ric, ric, ric, ric,},
        {ric, ric, ric, gab,},
        {ric, ric, gab, gab,},
    },
};

void solve(int cnum) {
    int x, r, c;
    scanf("%d %d %d", &x, &r, &c);
    printf("Case #%d: %s\n", cnum, soln[x-1][r-1][c-1]);
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
    return 0;
}