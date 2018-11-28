#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

typedef pair <char, bool> mypair;
map <pair <char, char>, string> mymap;

inline mypair operator * (const mypair & p1, const mypair & p2)
{
    string tmp = mymap[mp(p1.first, p2.first)];
    if (tmp.length() == 1)
        return mp(tmp[0], p1.second ^ p2.second);
    else return mp(tmp[1], p1.second ^ p2.second ^ 1);
}

const int maxn = 1e4 + 5;

mypair suff[maxn];
mypair pref[maxn];

void solve(int test)
{
    int n, copies;
    scanf("%d%d", &n, &copies);
    string s1;
    cin >> s1;
    string s = "";
    forn(c, copies)
        s += s1;
    n *= copies;
    pref[0] = mp(s[0], false);
    fore(j, 1, n - 1)
        pref[j] = pref[j - 1] * mp(s[j], false);
    suff[n - 1] = mp(s[n - 1], false);
    for (int j = n - 2; j >= 0; j--)
        suff[j] = mp(s[j], false) * suff[j + 1];
    //cout << "s = " << s << endl;
    fore(start2, 1, n -  1) if (pref[start2 - 1] == mp('i', false))
    {
        mypair cur = mp('1', false);
        fore(finish, start2, n - 1)
        {
            cur = cur * mp(s[finish], false);
            if (cur == mp('j', false) && suff[finish + 1] == mp('k', false))
            {
                printf("Case #%d: YES\n", test);
                return;
            }
        }
    }
    printf("Case #%d: NO\n", test);
}

void init(char c1, char c2, string s)
{
    mymap[mp(c1, c2)] = s;
}

int main() {
#ifdef LOCAL
    freopen("inp", "r", stdin);
    freopen("outp", "w", stdout);
#else
    // freopen(TASKNAME ".in", "r", stdin);
    // freopen(TASKNAME ".out", "w", stdout);
#endif
    init('1', '1', "1");
    init('1', 'i', "i");
    init('1', 'j', "j");
    init('1', 'k', "k");

    init('i', '1', "i");
    init('i', 'i', "-1");
    init('i', 'j', "k");
    init('i', 'k', "-j");   

    init('j', '1', "j");
    init('j', 'i', "-k");
    init('j', 'j', "-1");
    init('j', 'k', "i");

    init('k', '1', "k");
    init('k', 'i', "j");
    init('k', 'j', "-i");
    init('k', 'k', "-1");
    int T;
    scanf("%d", &T);
    forn(test, T)
    {
        cerr << "test " << test << endl;
        solve(test + 1);
    }
}
