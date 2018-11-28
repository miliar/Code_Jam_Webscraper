#include <stdio.h>
#include <iostream>
using namespace std;

#define MAXN (50+5)

int n;
long long p;
long long f[MAXN];

bool check(int n, long long x, long long p)
{
    long long  k ;

    if (x == 1) return true;
    if (p <= f[n-1]) return false;
    k = (x-2)/2;
    return check(n-1, k+1, p-f[n-1]);
}

bool large(int n, long long x, long long p)
{
    long long k;

    if (x == f[n])
    {
        if (p == f[n]) return true;
        else return false;
    }
    if (p > f[n-1]) return true;
    k = (f[n]-x-1)/2;
    return large(n-1, f[n-1]-k, p);
}

void doit()
{
    long long l, r, mid;

    cin >> n >> p;

    l = 1; r = f[n];
    while (l <= r)
    {
        mid = (l+r)/2;
        if (check(n, mid, p)) l = mid+1;
        else r = mid-1;
    }
    cout << r-1 << ' ';
    l = 1; r = f[n];

    while (l <= r)
    {
        mid = (l+r)/2;
        if (large(n, mid, p)) l = mid+1;
        else r = mid-1;
    }
    cout << r-1 << endl;

}

int main()
{
    int t;


    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    f[0] = 1;
    for (int i = 1;i <= 50;++i)
        f[i] = f[i-1]*2;

    cin >> t;
    for (int w = 1;w <= t;++w)
    {
        printf("Case #%d: ",w);
        doit();
    }
    return 0;
}
