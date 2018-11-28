#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("D-small-attempt5.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t = 0, x = 0, r = 0, c = 0, m = 0;

    scanf("%d", &t);

    for(int i = 1; i <= t; i++)
    {
        m = 0;

        scanf("%d%d%d", &x, &r, &c);

        if(x > (r * c))
            m = 1;
        else
        if((r * c) == 3 && x == 3)
            m = 1;
        else
        if((r * c) == 4 && x == 4 && (r == 1 || c == 1))
            m = 1;
        else
        if((r * c) == 4 && x == 4 && r == 2)
            m = 1;
        else
        if((r * c) == 8 && x == 4)
            m = 1;
        else
        if(((r * c) % x) != 0)
            m = 1;

        if(m == 1)
            printf("Case #%d: RICHARD\n", i);
        else
            printf("Case #%d: GABRIEL\n", i);
    }

    return 0;
}
