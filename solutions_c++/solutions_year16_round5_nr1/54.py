#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

void solve (string s, int test)
{
    int n = sz(s);
    assert(n % 2 == 0);
    for (char ch : s)
        assert(ch == 'C' || ch == 'J');

    char cur = s[0];
    int cnt = 1;
    string parts;

    int ans = 10 * n / 2;

    for (int i = 1; i <= n; i++)
    {
        if (i == n || s[i] != s[i - 1])
        {
            if (cnt % 2 == 1)
                parts += cur;
            while (sz(parts) >= 2 && parts[sz(parts) - 1] == parts[sz(parts) - 2])
            {
                parts.pop_back();
                parts.pop_back();
            }
            cnt = 1;
            cur = (i == n ? -1 : s[i]);
        }
        else
            cnt++;
    }

    assert(sz(parts) % 2 == 0);
    ans -= 5 * sz(parts) / 2;
    printf("Case #%d: %d\n", test, ans);
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "rt", stdin);
    #endif // ONLINE_JUDGE

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    int test = 1;
    string n;
    while (cin >> n)
        solve(n, test), test++;
}
