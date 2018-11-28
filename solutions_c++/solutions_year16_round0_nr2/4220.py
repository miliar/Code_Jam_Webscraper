
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
    read("B-large.in");
    write("output.txt");
}
string flip(string x)
{
    reverse(all(x));
    for(int i = x.size() - 1; i >= 0; --i)
    x[i] = x[i] == '+' ? '-' : '+';
    return x;
}
bool check(string x)
{
    for(int i = x.size() - 1; i >= 0; --i)
    if(x[i] == '-')
        return false;
    return true;
}
int main()
{
    IO();
    int T;
    cin >> T;
    rep1(cas, T)
    {
        string s;
        cin >> s;
        int len = s.size();
        int ans = 0;
        while(!check(s))
        {
            char c = s[0];
            int ll = 1;
            for(int i = 1; i < len; ++i)
            {
                if(s[i] == c)
                {
                    ++ll;
                }
                else
                {
                    break;
                }
            }
            string r = s.substr(0, ll);
            r = flip(r);
            for(int i = 0; i < ll; ++i)
            {
                s[i] = r[i];
            }
            ++ans;
            //cout << s << endl;
        }
        pf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
