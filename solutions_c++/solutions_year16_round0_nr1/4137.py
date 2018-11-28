
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
void IO()
{
    read("A-large.in");
    write("output.txt");
}
int main()
{
    IO();
    int T;
    sf("%d", &T);
    rep1(cas, T)
    {
        lng N, ans = -1;
        sf("%lld", &N);
        if(N == 0)
        {
            pf("Case #%d: INSOMNIA\n", cas);
            continue;
        }
        map<int, int> mp;
        for(lng i = 1;; ++i)
        {
            lng t = i * N;
            while(t)
            {
                mp[t % 10] = 1;
                t /= 10;
                if(mp.size() == 10)
                {
                    ans = i * N;
                    break;
                }
            }
            if(ans != -1)
                break;
        }
        pf("Case #%d: %lld\n", cas, ans);
    }
    return 0;
}
