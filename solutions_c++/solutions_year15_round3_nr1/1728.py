#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t = 0, r = 0, c = 0, w = 0, m = 0;

    scanf("%d", &t);

    for(int i = 1; i <= t; i++)
    {
        scanf("%d%d%d", &r, &c, &w);

        m = w;

        if(c == w)
            m = c;
        else
            m = m + ((c - 1) / w);

        printf("Case #%d: %d\n", i, m);
    }

    return 0;
}
