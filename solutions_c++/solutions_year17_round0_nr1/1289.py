#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = (n)-1; i >= 0; i--)
using namespace std;
using lli = long long int;
void solve(string s, int k, int c)
{
    int n = s.size();
    int ans = 0;
    for (int i = 0; i + k <= n; i++) {
        if (s[i] == '-') {
            rep(j, k)
            {
                s[j + i] = (s[j + i] == '-' ? '+' : '-');
            }
            ans++;
        }
    }
    rep(i, n)
    {
        if (s[i] == '-')
            ans = -1;
    }
    if (ans == -1) {
        cout << "Case #" << c << ": "
             << "IMPOSSIBLE" << endl;
        //cout << s << endl;
    } else {
        cout << "Case #" << c << ": " << ans << endl;
    }
}
int main()
{
    int t;
    cin >> t;
    string s;
    int k;
    rep(i, t)
    {
        cin >> s >> k;
        solve(s, k, i + 1);
    }
}
