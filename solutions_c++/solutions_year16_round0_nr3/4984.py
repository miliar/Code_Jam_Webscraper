#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
typedef long long LL;
int n, j, tol;
const int S = 8;
LL ans[15];

long long mult_mod(long long a,long long b,long long c)
{
    a %= c;
    b %= c;
    long long ret = 0; long long tmp = a; while(b )
    {
        if(b & 1)
        {
            ret += tmp;
            if(ret > c)ret -= c;
        }
            tmp <<= 1;
            if(tmp > c)tmp -= c; b >>= 1;
        }
        return ret;
}
long long pow_mod(long long a,long long n,long long mod)
{
    long long ret = 1;
    long long temp = a%mod;
    while(n)
    {
        if(n & 1)ret = mult_mod(ret,temp,mod);
        temp = mult_mod(temp,temp,mod);
        n >>= 1;
    }
    return ret;
}
bool check(long long a,long long n,long long x,long long t)
{
    long long ret = pow_mod(a,x,n);
    long long last = ret;
    for(int i = 1;i <= t;i++)
    {
        ret = mult_mod(ret,ret,n);
        if(ret == 1 && last != 1 && last != n-1)
            return true;//合数
        last = ret;
    }
    if(ret != 1)
        return true;
    else
        return false;
}
bool Miller_Rabin(long long n)
{
    if( n < 2)
        return false;
    if( n == 2)
        return true;
    if( (n&1) == 0)
        return false;//偶数
    LL x = n - 1;
    LL t = 0;
    while( (x&1)==0 )
    {
        x >>= 1;
        t++;
    }
    srand(time(NULL));
    for(int i = 0;i < S;i++)
    {
        LL a = rand()%(n-1) + 1;
        if( check(a,n,x,t) )
            return false;
    }
    return true;
}
long long gcd(long long a,long long b)
{
    long long t;
    while(b)
    {
        t = a;
        a = b;
        b = t%b;
    }
    if(a >= 0)
        return a;
    else
        return -a;
}
LL pollard_rho(LL x, LL c)
{
    LL i = 1, k = 2;
    srand(time(NULL)) ;
    LL x0 = rand()%(x-1) + 1;
    LL y = x0;
    while(1)
    {
        i++;
        x0 = (mult_mod(x0,x0,x) + c)%x;
        long long d = gcd(y - x0,x);
        if( d != 1 && d != x)
            return d;
        if(y == x0)
            return x;
        if(i == k)
        {
            y = x0;
            k += k;
        }
    }
}
LL findfac(LL n,int k)
{
    LL p = n;
    int c = k;
    while(p >= n)
        p = pollard_rho(p, c--);//值变化,防止死循环k
    return p;
    //findfac (p,k) ;
    //findfac (n/p, k);
}

LL getFactor(LL x)
{
    if(Miller_Rabin(x)) return 0;
    else
    {
        tol = 0;
        LL ans = findfac(x, 107);
        //for(int i = 1;i < tol;i++)
         //   ans = min(ans,factor[i]);
        //printf( "%I64 d\n" ,ans) ;
        return ans;
    }
}
    
bool work(LL x)
{
    ans[2] = getFactor(x);
    if (ans[2] == 0)
        return false;
    int a[20];
    for (int i = n - 1; i >= 0; i--)
    {
        a[i] = x & 1;
        x >>= 1;
    }
//    for (int i = 0; i < n; i++)
//        printf("%d", a[i]);
//    printf("\n");
    LL num = 0;
    for (int i = 3; i <= 10; i++)
    {
        num = 0;
        for (int j = 0; j < n; j++)
            num = num * i + a[j];
        //printf("%d %lld\n", i, num);
        ans[i] = getFactor(num);
        if (ans[i] == 0)
            return false;
    }
    for (int i = 0; i < n; i++)
        printf("%d", a[i]);
    for (int i = 2; i <= 10; i++)
        printf(" %lld", ans[i]);
    printf("\n");
    return true;
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int t, Case = 0;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d%d", &n, &j);
        printf("Case #%d:\n", ++Case);
        int m = (1 << n) - 1, count = 0;
        for (int i = (1 << (n - 1)); i <= m; i++)
        {
            if ((i & 1) == 0) continue;
            //printf("%d\n", i);
            if (work(LL(i)))
            {
                count++;
            }
            if (count == j)
                break;
        }
    }
    
}