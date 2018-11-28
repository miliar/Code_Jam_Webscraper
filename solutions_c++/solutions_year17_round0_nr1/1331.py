#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, s, n) for(int i=(s); i<=(n); i++)
#define FORD(i, s, n) for(int i=(s); i>=(n); i--)
#define SIZE(x) ((int) (x).size())
#define DEBUG 0
#define D if(DEBUG)
typedef long long LL;
typedef pair<int, int> PII;

void flip(string & s, int at, int l)
{
    FOR(i, at, at + l - 1)
    {
        if(s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
}

void solve()
{
    string s; int k, c = 0;
    cin >> s >> k;
    REP(i, SIZE(s)) if(s[i] == '-')
    {
        if(i > SIZE(s) - k)
        {
            cout << "IMPOSSIBLE\n";
            return;
        }
        else
        {
            flip(s, i, k);
            c++;
        }
    }
    cout << c << '\n';
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    REP(i, t)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    } 
}