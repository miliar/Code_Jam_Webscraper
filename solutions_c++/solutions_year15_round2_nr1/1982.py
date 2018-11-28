#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;

int reverse(int n)
{
    int temp = n;

    if(n % 10 == 0)
        return (n - 1);

    int res = 0;

    while(n > 0)
    {
       res = (res * 10) + (n % 10);
       n /= 10;
    }

    if(res < temp)
        return res;
    else
        return (temp - 1);
}

int min(int a, int b)
{
    if(a < b)
        return a;

    return b;
}

int a[1000000];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t = 0, n = 0;

    a[0] = 0;

    for(int i = 1; i <= 1000000; i++)
        a[i] = min(a[reverse(i)] + 1, a[i - 1] + 1);

/*
    int t = 0, r = 0, c = 0, n = 0, m = 0, opt = 0;
*/
    scanf("%d", &t);

    for(int i = 1; i <= t; i++)
    {
        scanf("%d", &n);

        printf("Case #%d: %d\n", i, a[n]);
    }

    return 0;
}
