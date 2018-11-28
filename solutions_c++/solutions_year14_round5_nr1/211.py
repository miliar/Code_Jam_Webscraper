//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;

int t;
int n,p,q,r,s;

int fun(int x)
{
    return ((LL)(x-1)*p+q)%r+s;
}

bool check(LL x)
{
    LL sum;

    int a = 1;
    sum = 0;
    while(a <= n && sum <= x)
    {
        sum += fun(a);
        a++;
    }
    a--;

    if(fun(a) > x) return false;

    int b = a;
    sum = fun(a);
    while(b < n && sum+fun(b+1) <= x)
    {
        b++;
        sum += fun(b);
    }

    //cerr << "A: " << a << "B :" << b << endl;

    sum = 0;
    for(int i = b+1;i <= n;i++)
        sum += fun(i);

    if(sum > x) return false;

    return true;
}

LL bin(LL p, LL k)
{
    LL sr, ret = k;

    while(p < k)
    {
        sr = (p+k)/2;
        bool res = check(sr);
        //cerr << "SR: " << sr << " check: " << res << endl;
        if(res)
        {
            ret = sr;
            k = sr;
        }
        else
            p = sr+1;
    }

    return ret;
}

LL obl()
{
    return bin(0, 1000000000012LL);
}

int main()
{
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);

        /*cerr << "FUN: ";
        for(int i = 1;i <= n;i++)
            cerr << fun(i) << " ";
        cerr << endl;*/

        LL sum = 0;
        for(int i = 1;i <= n;i++)
            sum += fun(i);

        LL wyn = bin(0LL, min(1000000000012LL,sum));
        LL ja = sum-wyn;

        //cerr << "Sum: " << sum << endl;
        //cerr << "Wyn: " << wyn << endl;
        //cerr << "Ja: " << ja << endl;

        long double kwyn = (long double)ja/(long double)sum;

        printf("Case #%d: %.10Lf\n", ti, kwyn);
    }
    return 0;
}
