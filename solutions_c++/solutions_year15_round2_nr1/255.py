#include <iostream>
#include <cstdio>

using namespace std;

const int N = 1000005;
int d[N];
int flip(int x)
{
    int res = 0;
    for(; x; x /= 10) res = res * 10 + x % 10;
    return res;
}

int main()
{
    freopen("A-small-attempt3.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int test;
    scanf("%i", &test);

    int n = 1000000;
    d[1] = 1;
    for(int i = 2; i <= N; i++) d[i] = 1 << 30;
        for(int a = 0; a < 300; a++)
            for(int i = 2; i <= n; i++)
                d[i] = min(d[i], min(d[i - 1], i % 10 ? d[flip(i)] : (1 << 30)) + 1);

    for(int tt = 1; tt <= test; tt++)
    {
        printf("Case #%i: ", tt);
        long long n;
        scanf("%lld", &n);
cout<<d[n]<<endl;
    }
    return 0;
}
