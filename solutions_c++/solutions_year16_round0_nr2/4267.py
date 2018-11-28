#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define FILE "pancakes"

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const ull ULLINF = numeric_limits<ull>::max();
const double PI = acos(-1.0);

int solve(string & s, int r, char need)
{
    bool pl = 0, mi = 0;
    for(int i = 0; i < r; i++)
        if(s[i] == '+')
            pl = 1;
        else
            mi = 1;
    if(pl ^ mi)
        return (need == '+' && pl ? 0 : 1);
    if(s[r - 1] == need)
    {
        for(; s[r - 1] == need; r--);
        return solve(s, r, need);
    }
    else
    {
        for(; s[r - 1] != need; r--);
        return 1 + solve(s, r, need == '+' ? '-' : '+');
    }
}

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int tt = 1; tt <= T; tt++)
    {
        string s;
        cin >> s;
        int n = s.length();
        cout << "Case #" << tt << ": " << solve(s, n, '+') << '\n';
    }
    return 0;
}
