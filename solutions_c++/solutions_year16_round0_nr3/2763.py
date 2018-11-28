#include<bits/stdc++.h>
#define sf scanf
#define pf printf

using namespace std;


typedef unsigned long long llu;

llu kye[20] ;

llu mulmod(llu  a, llu  b, llu  mod)
{
    llu  x = 0 , y = a % mod;
    while (b > 0)
    {
        if (b & 1) x = (x + y) % mod;
        y = (y << 1) % mod;
        b = b >> 1;
    }
    return x % mod;
}

llu modulo(llu  base, llu  exponent, llu  mod)
{
    llu  x = 1;
    llu  y = base;
    while (exponent > 0)
    {
        if (exponent & 1) x = mulmod(x , y , mod) ;
        y = mulmod(y ,  y , mod) ;
        exponent = exponent >> 1;
    }
    return x % mod;
}

bool Miller(llu p , int ind)
{
    if (p < 2) return false;
    if (p != 2 && !(p & 1)) return false;
    llu  last , s = p - 1;
    while (!(s & 1)) s = s >> 1;
    for (int i = 0; i < 5 ; i++)
    {
        llu  a = rand() % (p - 1) + 1 , temp = s;
        llu  mod = modulo(a, temp, p);
        while (temp != p - 1 && mod != 1 && mod != p - 1)
        {
            mod = mulmod(mod, mod, p);
            if(mod != 1)
            {
                last = __gcd(mod - 1 , p);
                if(kye[ind] <= 1 && last != 1 ) kye[ind] = last;
                last = __gcd(mod + 1 , p);
                if(kye[ind] <= 1 && last != 1 ) kye[ind] = last;
            }
            temp = temp << 1;
        }
        if (mod != p - 1 && !(temp & 1)) return false;

    }
    return true;
}

llu power(int n , int p)
{
    if(p == 0) return 1;
    if(p & 1) return (n * power(n , p - 1));
    llu temp = power(n , p / 2);
    return (temp * temp);
}

int main()
{
    freopen("output.in" , "w" , stdout);
    freopen("input.txt" , "r" , stdin);
    int t , len , cnt , s , e , temp , cc = 0;
    llu ar[20];
    bool flag;
    string str ;
    sf("%d" , &t);
    while(t--)
    {
        pf("Case #%d:\n" , ++cc);
        sf("%d %d" , &len , &cnt);
        s = (1 << (len - 1));
        e = (1 << (len)) ;
        for(int i = s + 1 ; i < e ; i = i + 2)
        {
            memset(ar , 0 , sizeof(ar));
            memset(kye , 0 , sizeof(kye));
            str.clear();
            for(int j = 0 ; j < len ; ++j)
            {
                temp = ( i & (1 << j) );
                if(temp) str = '1' + str;
                else str = '0' + str;
                for(int k = 2 ; k <= 10 ; ++k)
                {
                    if(temp) ar[k] = ar[k] + power(k , j);
                }
            }
            flag = false;
            for(int k = 2 ; k <= 10 ; ++k)
            {
                if(Miller(ar[k] , k))
                {
                    flag = true;
                    break ;
                }
            }
            if(!flag)
            {
                int ll = 0;
                for(int i = 2 ; i <= 10 ; ++i)
                {
                    if(ar[i] && ar[i] % 2 == 0) ++ll;
                    else if(kye[i] >= 2) ++ll;
                }
                if(ll >= 9)
                {
                    pf("%s" , str.c_str());
                    for(int i = 2 ; i <= 10 ; ++i)
                    {
                        if(ar[i] % 2 == 0) pf(" 2");
                        else pf(" %llu" , kye[i]);
                    }
                    pf("\n");
                    --cnt;
                }
            }
            if(cnt <= 0) break ;
        }
    }
    return 0;
}
