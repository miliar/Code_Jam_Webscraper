#include <iostream>
#include <cstdio>

using namespace std;

long long solvef(long long a, long long b, long long k) // koliko ima i <= a, j <= b takvih da i & j > k
{
    if(k == 0) return 0;

    printf("solve %lld %lld %lld:\n", a, b, k);

    long long m = 0;
    for(int i = 0; i < 32; i++)
        if((1LL << i) & k)
            m = 1LL << i;

    printf("m = %lld\n", m);

    if(m > a || m > b) return a * b;
    else return m + solvef(a & (~m), b & (~m), k & (~m));
}

long long solve(long long a, long long b, long long k)
{
    long long res = 0;
    for(int i = 0; i < a; i++)
        for(int j = 0; j < b; j++)
            if((i & j) < k)
                res++;
    return res;
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    scanf("%i", &t);

    for(int i = 0; i < t; i++)
    {
        int a, b, k;
        scanf("%i %i %i", &a, &b, &k);
        printf("Case #%i: %lld\n", i + 1, solve(a, b, k));
    }
    return 0;
}
