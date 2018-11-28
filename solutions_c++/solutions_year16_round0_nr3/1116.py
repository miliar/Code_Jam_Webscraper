#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

const int bound = 1000;

int find_div (const string &s, int base)
{
    vi rem(bound);
    for (int i = 0; i < sz(s); i++)
    {
        for (int j = 2; j < bound; j++)
            rem[j] = (rem[j] * base + s[i] - '0') % j;
    }

    for (int j = 2; j < bound; j++)
    if (rem[j] == 0)
        return j;
    return -1;
}

bool check_good (const string &s, vi &who)
{
    for (int base = 2; base <= 10; base++)
    {
        int div = find_div (s, base);
        who.pb(div);
        if (div == -1)
            return false;
    }
    return true;
}

void solve (int n, int j, int test)
{
    int cnt = 0;
    mt19937 rng;

    vector<pair<string, vi>> result;
    set<string> was;

    while (sz(result) < j)
    {
        string ns = "1";
        for (int i = 1; i < n - 1; i++)
            ns += (rng() % 2 + '0');
        ns += "1";
        if (was.count(ns))
            continue;

        vi who;
        if (check_good(ns, who))
        {
            result.pb(mp(ns, who));
            was.insert(ns);
        }
    }

    printf("Case #%d:\n", test);
    assert(sz(result) == j);
    for (int i = 0; i < sz(result); i++)
    {
        printf("%s", result[i].first.c_str());
        assert(sz(result[i].second) == 9);
        for (int x : result[i].second)
            printf(" %d", x);
        printf("\n");
    }
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "w", stdout);
    #endif

 //   ios_base::sync_with_stdio(false);
 //   cin.tie(0);

    int t;
    cin >> t;

    int n, j;
    int test = 1;
    while (cin >> n >> j)
        solve (n, j, test), test++;
}

