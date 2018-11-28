#include <bits/stdc++.h>

using namespace std;

#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define forab(i,a,b) for (int i = int(a); i < int(b); ++i)

typedef long long ll;
typedef long double ld;

const int INF = 1000001000;
const ll INFL = 2000000000000001000;
int solve();


int main()
{
    srand(2317);
    cout.precision(10);
    cout.setf(ios::fixed);
    #ifdef LOCAL
    freopen("c.in", "r", stdin);
    #else
    #endif
    int tn = 1;
    cin >> tn;
    for (int i = 0; i < tn; ++i)
        solve();
    #ifdef LOCAL
    cerr << "Time: " << double(clock()) / CLOCKS_PER_SEC << '\n';
    #endif
}

int test = 1;

map<string, int> conv;
int words = 0;
vector<char> mask;

int getid(string s)
{
    if (conv.count(s))
        return conv[s];
    conv[s] = words++;
    mask.push_back(0);
    return words - 1;
}

string s;
vector<vector<int>> a;

int rec(int d, int bads = 0)
{
    if (d == sz(a))
        return bads;
    vector<char> old;
    for (int x: a[d])
        old.push_back(mask[x]);
    int res = INF;
    forn (q, 2)
    {
        if (d == 0 && q == 1)
            continue;
        if (d == 1 && q == 0)
            continue;
        int cbads = bads;
        forn (i, sz(a[d]))
        {
            int x = a[d][i];
            if (mask[x] != 3 && (mask[x] | (1 << q)) == 3)
                ++cbads;
            mask[x] |= (1 << q);
        }
        res = min(res, rec(d + 1, cbads));
        forn (i, sz(a[d]))
            mask[a[d][i]] = old[i];
    }
    return res;
}

int solve()
{
    mask.clear();
    words = 0;
    a.clear();
    conv.clear();
    int n;
    scanf("%d\n", &n);
    forn (i, n)
    {
        getline(cin, s);
        istringstream is(s);
        string word;
        a.emplace_back();
        while (is >> word)
        {
            int x = getid(word);
            a.back().push_back(x);
        }
    }
    int ans = rec(0);
    printf("Case #%d: %d\n", test++, ans);
    return 0;
}
