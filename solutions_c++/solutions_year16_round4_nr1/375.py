#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

char winner (char f, char s)
{
    assert(f != s);
    if (f == 'P')   return s == 'S' ? s : f;
    if (f == 'R')   return s == 'P' ? s : f;
    if (f == 'S')   return s == 'R' ? s : f;
    assert(false);
    return -1;
}

bool check (string ans)
{
    for (char ch : ans)
        assert(ch == 'P' || ch == 'S' || ch == 'R');
    if (sz(ans) == 1)
        return true;
    assert(sz(ans) % 2 == 0);

    string next;
    for (int i = 0; i < sz(ans); i += 2)
    {
        if (ans[i] == ans[i + 1])
            return false;
        next += winner(ans[i], ans[i + 1]);
    }
    return check(next);
}

const string NO = "IMPOSSIBLE";

string go (vector<pair<char, string>> hist)
{
    if (sz(hist) == 1)
        return hist[0].second;
    assert(sz(hist) % 2 == 0);

    map<char, int> cnt;
    for (const auto &pr : hist)
        cnt[pr.first]++;

    int p = cnt['P'];
    int s = cnt['S'];
    int r = cnt['R'];
    int total = (p + s + r) / 2;
    assert(total == sz(hist) / 2);

    int pr = total - s;
    int sp = total - r;
    int rs = total - p;
    if (pr < 0 || sp < 0 || rs < 0)
        return NO;

    map<char, multiset<string>> tmp;
    multiset<pair<string, char>> all;

    for (const auto &pr : hist)
    {
        all.insert(mp(pr.second, pr.first));
        tmp[pr.first].insert(pr.second);
    }

    vector<pair<char, string>> nw;

    while (!all.empty())
    {
        string cur = all.begin() -> first;
        char what = all.begin() -> second;

        char to = -1;
        string add;

        for (char prt : {'P', 'R', 'S'})
        if (prt != what && !tmp[prt].empty())
        if (to == -1 || *tmp[prt].begin() < add)
        {
            string txt{what, prt};
            sort(ALL(txt));
            assert(txt == "PR" || txt == "PS" || txt == "RS");
            if (txt == "PS" && sp == 0)
                continue;
            if (txt == "PR" && pr == 0)
                continue;
            if (txt == "RS" && rs == 0)
                continue;

            to = prt;
            add = *tmp[prt].begin();
        }

        string txt{to, what};
        sort(ALL(txt));
        assert("end" && txt == "PR" || txt == "PS" || txt == "RS");
        if (txt == "PS") sp--;
        if (txt == "PR") pr--;
        if (txt == "RS") rs--;

        assert(to != -1);
        all.erase(all.begin());
        tmp[to].erase(tmp[to].find(add));
        all.erase(all.find(mp(add, to)));
        tmp[what].erase(tmp[what].begin());
        nw.pb(mp(winner(to, what), min(cur + add, add + cur)));

        assert(to != -1);
    }

    return go(nw);
}

void solve (int n, int test)
{
    int rock, paper, scis;
    cin >> rock >> paper >> scis;
    assert(rock + paper + scis == (1 << n));

    vector<pair<char, string>> who;
    for (int i = 0; i < rock; i++)
        who.pb(mp('R', "R"));
    for (int i = 0; i < paper; i++)
        who.pb(mp('P', "P"));
    for (int i = 0; i < scis; i++)
        who.pb(mp('S', "S"));
    string ans = go(who);
    //cerr << ans << endl;
    if (ans != NO)
        assert(check(ans));
    //cerr << test << endl;
    printf("Case #%d: %s\n", test, ans.c_str());
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "rt", stdin);
    #endif // ONLINE_JUDGE

   // ios_base::sync_with_stdio(false);
   // cin.tie(0);

    int t;
    cin >> t;

    int n, test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
