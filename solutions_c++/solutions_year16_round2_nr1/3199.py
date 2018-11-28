
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
#define     si(x)          sf("%d", &x);
#define     mem(x, y)      memset(x, y, sizeof(x));
#define     rep(i, x)      for(int i = 0; i < x; ++i)
#define     rep1(i, x)     for(int i = 1; i <= x; ++i)
#define     RAD_TO_DEG     180.0/PI
#define     read(a)        freopen(a, "r", stdin);
#define     write(a)       freopen(a, "w", stdout);
#define     pr2(aa,bb)     cout << aa << ' ' << bb << '\n';
#define     pr3(aa,bb,cc)  cout << aa << ' ' << bb << ' ' << cc << '\n';
#define     prv(x)         rep(i, x.size()) cout << x[i] << ' '; cout << '\n';
string store[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string S;
map<string, char> st;
int len;
void IO()
{
    read("A-large.in");
    write("output.txt");
}
map<char, int> mp;
bool isempty()
{
    for(char c = 'A'; c <= 'Z'; c++)
    {
        if(mp[c] > 0)
            return false;
    }
    return true;
}
int Main()
{
    string ss;
    while(cin >> ss)
    {
        sort(all(ss));
        cout << ss << endl;
    }
}
int main()
{
    IO();
    st["ZERO"] = '0';
    st["ONE"] = '1';
    st["TWO"] = '2';
    st["THREE"] = '3';
    st["FOUR"] = '4';
    st["FIVE"] = '5';
    st["SIX"] = '6';
    st["SEVEN"] = '7';
    st["EIGHT"] = '8';
    st["NINE"] = '9';
    int T;
    sf("%d", &T);
    rep1(cas, T)
    {
        cin >> S;
        len = S.size();
        mp.clear();
        rep(i, len)
        {
            mp[S[i]]++;
        }
//        for(map<char, int>:: iterator it = mp.begin(); it != mp.end(); it++)
//        {
//            cout << it -> first << ' ' << it -> second << endl;
//        }
        string ans = "";
        while(mp['Z']--)
        {
            ans += '0';
            mp['E']--;
            mp['R']--;
            mp['O']--;
        }

        while(mp['W']--)
        {
            ans += '2';
            mp['T']--;
            mp['O']--;
        }

        while(mp['U']--)
        {
            ans += '4';
            mp['F']--;
            mp['O']--;
            mp['R']--;
        }

        while(mp['X']--)
        {
            ans += '6';
            mp['S']--;
            mp['I']--;
        }

        while(mp['G']--)
        {
            ans += '8';
            mp['E']--;
            mp['I']--;
            mp['H']--;
            mp['T']--;
        }

        while(mp['O'] && mp['N'] && mp['E'])
        {
            mp['O']--;
            mp['N']--;
            mp['E']--;
            ans += '1';
        }
        while(mp['T'] && mp['H'] && mp['R'] && mp['E'] >= 2)
        {
            mp['T']--;
            mp['H']--;
            mp['R']--;
            mp['E']--;
            mp['E']--;
            ans += '3';
        }
        while(mp['F'] && mp['I'] && mp['V'] && mp['E'])
        {
            mp['F']--;
            mp['I']--;
            mp['V']--;
            mp['E']--;
            ans += '5';
        }
        while(mp['S'] && mp['E'] >= 2 && mp['V'] && mp['N'])
        {
            mp['S']--;
            mp['V']--;
            mp['E'] -= 2;
            mp['N']--;
            ans += '7';
        }
        while(mp['N'] >= 2 && mp['I'] && mp['E'])
        {
            mp['N'] -= 2;
            mp['I']--;
            mp['E']--;
            ans += '9';
        }
//        for(map<char, int>:: iterator it = mp.begin(); it != mp.end(); it++)
//        {
//            cout << it -> first << ' ' << it -> second << endl;
//        }
        sort(all(ans));
        pf("Case #%d: ", cas);
        cout << ans << endl;
    }
    return 0;
}
