#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int t;
int vec[11];

bool allDigits()
{
    for (int i=0; i<10; i++)
        if (vec[i] == 0)
            return false;
    return true;
}

long long lastNumber(long long n, int k = 1)
{
    long long aux = n * k;
    while(aux)
    {
        vec[aux%10]++;
        aux/=10;
    }

    if (allDigits())
        return n * k;
    return lastNumber(n, k+1);
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    long long n;
    scanf("%d\n", &t);
    for (int i=1; i<=t; i++)
    {
        scanf("%lld\n", &n);

        if (n == 0)
            printf("Case #%d: INSOMNIA\n", i);

        else
        {
            long long toPrint = lastNumber(n);
            if (toPrint != 0)
                printf("Case #%d: %lld\n", i, toPrint);
        }

        memset(vec, 0, sizeof(vec));
    }

    return 0;
}
