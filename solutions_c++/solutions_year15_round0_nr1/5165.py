#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <cstring>
using namespace std;
int fn();

char array[1009];
int n, cases, p = 1;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("c.out", "w", stdout);
    scanf("%d", &cases);
    while(cases--)
    {
        scanf("%d %s", &n, array);
        printf("Case #%d: %d\n", p++, fn());
    }

    return 0;
}

int fn()
{
    int accum = 0, ret = 0;

    for(int i = 0; i <= n; i++)
    {
        if(i <= accum || array[i] - '0' == 0)
            accum += array[i] - '0';
        else
            ret += i - accum, accum += i - accum, accum += + array[i] - '0';
    }

    return ret;
}
