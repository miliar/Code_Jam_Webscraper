#include <stdio.h>

int solve()
{
    int x, r, c;
    scanf("%d%d%d", &x, &r, &c);
    switch (x){
        case 1:
            return 0; // gab
        case 2:
            if((r * c) % 2)
                return 1; // ric
            return 0; // gab
        case 3:
            if((r * c) % 3)
                return 1; // ric
            if(r == 1 || c == 1)
                return 1; // ric
            return 0; // gab
        case 4:
            if((r * c) % 4)
                return 1; // ric
            if(r == 1 || c == 1)
                return 1; // ric
            if(r == 2 || c == 2)
                return 1; // ric
            return 0; // gab
        case 5:
            if((r * c) % 5)
                return 1; // ric
            if(r == 1 || c == 1)
                return 1; // ric
            if(r == 2 || c == 2)
                return 1; // ric
            if(r == 3 && c == 5)
                return 1; // ric
            if(r == 5 && c == 3)
                return 1; // ric
            return 0; // gab
        case 6:
            if((r * c) % 6)
                return 1; // ric
            if(r == 1 || c == 1)
                return 1; // ric
            if(r == 2 || c == 2)
                return 1; // ric
            if(r == 3 || c == 3)
                return 1; // ric
            return 0; // gab
        default:
            return 1;
        }

}


int main()
{
    int t, t0;
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        printf("Case #%d: %s\n", t0 + 1, solve() ? "RICHARD" : "GABRIEL");
        }
    return 0;
}
