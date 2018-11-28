#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

const string no = "IMPOSSIBLE";

void solve (int n, int test)
{
    int l;
    cin >> l;

    string bad;
    cin >> bad;

    set<string> good;
    for (int i = 0; i < n; i++)
    {
        string ngood;
        cin >> ngood;
        assert(sz(ngood) == l);
        good.insert(ngood);
    }

    assert(sz(bad) == l);
    if (good.count(bad))
    {
        printf("Case #%d: %s\n", test, no.c_str());
        return;
    }

    string one = string(l - 1, '1');
    string two;
    for (int i = 0; i < l; i++)
        two += "?0";

    if (one.empty())
        one = "0";

    printf("Case #%d: %s %s\n", test, one.c_str(), two.c_str());
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
    int n;
    while (cin >> n)
        solve(n, test), test++;
}
