
/// /* Bismillahir Rahmanir Rahim *\

/// S. M. Shakir Ahsan Romeo
/// Khulna University
/// CSE Discipline
#include <bits/stdc++.h>
using namespace std;
typedef long long lng;
#define     rt             return
#define     PI             acos(-1.0)
#define     eps            1e-9
#define     inf            (1<<30)
#define     FAST           ios_base::sync_with_stdio(0);cin.tie(0);
#define     endl           '\n'
#define     pb             push_back
#define     sf             scanf
#define     pf             printf
#define     bin_sea        binary_search
#define     dbg(x)         cout << x << " came here\n";
#define     all(x)         x.begin(), x.end()
#define     mem(x, y)      memset(x, y, sizeof(x));
#define     rep(i, x)      for(int i = 0; i < x; ++i)
#define     rep1(i, x)     for(int i = 1; i <= x; ++i)
#define     RAD_TO_DEG     180.0/PI
#define     read(a)        freopen(a, "r", stdin);
#define     write(a)       freopen(a, "w", stdout);
lng POW(lng b, lng p);
lng to10(int a, string x);
string toBase(lng x, int base);
int isprime(lng x)
{
    if(x < 2LL)
        return false;
    if(x == 2LL)
        return true;
    if(x % 2 == 0)
        return false;
    lng s = sqrt(x * 1.0);
    for(lng i = 3; i <= s; i += 2)
    {
        if(x % i == 0)
        {
            return false;
        }
    }
    return true;
}
bool allbasecheck(lng x);
int main()     /// Main
{
    freopen("out.txt", "w", stdout);
    int xxx;
    cin >> xxx;
    pf("Case #1:\n");
    lng k = 1LL << 16;
    lng J = 50;
    for(lng i = (1 + (1LL << 15)); i < k ; i += 2LL)
    {
        string s = "";
        for(lng j = 15; j >= 0; --j)
        {
            if(i & (1LL << j))
                s += '1';
            else
                s += '0';
        }
        int cnt = 0;
        //s = "1001";
        vector<lng> dv;
        for(lng base = 2; base <= 10; ++base)
        {
            lng r = 0LL;
            for(lng ii = 0, jj = s.size() - 1; jj >= 0; ++ii, --jj)
            {
                r += ((s[ii] - 48) * POW(base, jj));
            }
            if(!isprime(r))
            {
                ++cnt;
                lng ss = sqrt(r * 1.0);
                for(lng vv = 2LL; vv <= ss; ++vv)
                {
                    if(r % vv == 0)
                    {
                        dv.pb(vv);
                        break;
                    }
                }
            }
            else
            {
                break;
            }
        }
        if(cnt == 9)
        {
            cout << s;
            for(int ii = 0; ii < dv.size(); ++ii)
            {
                cout << ' ' << dv[ii];
            }
            cout << endl;
            J--;
            if(J == 0)
                break;
        }
        //break;
    }
}
int Main()
{
    //bool b = allbasecheck(1001);
    cout << isprime(9) << endl;
    cout << isprime(28) << endl;
    cout << isprime(65) << endl;
    cout << isprime(126) << endl;
    cout << isprime(217) << endl;
    cout << isprime(344) << endl;
    cout << isprime(513) << endl;
    cout << isprime(730) << endl;
    cout << isprime(1001) << endl;
}
lng POW(lng b, lng p)
{
    if(p == 0)
        return 1;
    lng t = POW(b, p >> 1);
    if(p & 1LL)
        return b * t * t;
    return t * t;
}
lng to10(int a, string x)
{
    lng r = 0LL;
    for(lng i = 0, j = x.size() - 1; i < x.size(); ++i, --j)
    {
        r += ((x[i] - 48) * POW(a, j));
    }
    return r;
}
bool allbasecheck(lng x)
{
    for(int b = 2; b <= 10; ++b)
    {
        cout << toBase(x, b) << endl;
    }
}
string toBase(lng x, int base)
{
    string r = "";
    while(x)
    {
        r = (char)((x % base) + 48) + r;
        x /= base;
    }
    return r;
}
