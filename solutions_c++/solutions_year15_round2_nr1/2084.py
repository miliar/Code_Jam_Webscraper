#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

long long log10(long long n)
{
    long long l = 0;
    while(n >= 10)
    {
        ++l;
        n /= 10;
    }
    
    return l;
}

long long p10(long long e)
{
    long long ret = 1;
    for(long long i=0;i<e;++i)
    {
        ret *= 10;
    }
    
    return ret;
}

long long reverse(long long n)
{
    long long p = p10(log10(n));
    long long ret = 0;
    while(n > 0)
    {
        ret += p * (n % 10);
        p /= 10;
        n /= 10;
    }
    
    return ret;
}

long long resp[1000001];
//bool mrk[1000001];

/*
long long rec(long long n)
{
    if(n > 1000000)
    {
        cout << n << "\n";
        assert(false);
    }
    if(mrk[n])
    {
        return resp[n];
    }
    
    mrk[n] = true;
    resp[n] = 1 + rec(n-1);
    if((n % 10) != 0)
    {
        resp[n] = min(resp[n], 1 + rec(reverse(n)));
    }
    
    return resp[n];
}
*/

long long calc(long long n)
{
    /*
    for(int i=0;i<=1000000;++i)
    {
        resp[i] = 1000000;
        mrk[i] = false;
    }
    */
    
    resp[1] = 1;
    //mrk[1] = true;
    for(long long i=2;i<=n;++i)
    {
        resp[i] = 1+resp[i-1];
        if((i % 10) != 0)
        {
            auto r = reverse(i);
            if(r < i)
            {
                resp[i] = min(resp[i], 1+resp[r]);
            }
        }
    }
    
    
    return resp[n];
}

int main()
{
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp)
    {
        long long n;
        cin >> n;
        cout << "Case #" << lp << ": " << calc(n) << "\n";
    }
    
    return 0;
}