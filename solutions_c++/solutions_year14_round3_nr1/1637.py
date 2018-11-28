#include <iostream>
#include <stdio.h>

using namespace std;

long long gcd(long long a, long long b)
{
    if(a < b) return gcd(b, a);
    if(b == 0) return a;
    return gcd(b, a % b);
}

int main()
{
    int ttt;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &ttt);
    for(int tt = 1 ; tt <= ttt ; tt++)
    {
        printf("Case #%d: ", tt);
        long long a, b, t;
        scanf("%lld/%lld", &a, &b);
        int d = gcd(a, b);
        a /= d;
        b /= d;
        //printf("a %lld b %lld\n", a, b);
        int k = 0;
        t = b;
        while(t % 2 == 0 && t != 0)
            t /= 2, k++;
        if(t != 1)
        {
            printf("impossible\n");
            continue;
        }
        a = b - a;
        t = b / 2;
        k = 0;
        while(a > t && t != 1)
        {
            a -= t;
            t /= 2;
            k++;
        }
        printf("%d\n", k + 1);
    }
    return 0;
}
