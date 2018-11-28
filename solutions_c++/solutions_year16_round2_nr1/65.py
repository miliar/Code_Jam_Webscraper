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
    const int let = 26;
    vi cnt(let);
    const vector<string> digits =
    {
        "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
    };
    vvi dig_cnt(sz(digits), vi(let));
    for (int i = 0; i < sz(digits); i++)
    {
        for (int j = 0; j < let; j++)
            dig_cnt[i][j] = count(ALL(digits[i]), j + 'A');
    }

    for (char ch : s)
        cnt[ch - 'A']++;
    int total_cnt = sz(s);

    string who;
    while (total_cnt > 0)
    {
        bool ok = false;

        auto search_dg = [&] (int i) -> void
        {
            bool cur = true;
            for (int j = 0; j < let; j++)
                cur &= cnt[j] >= dig_cnt[i][j];

            if (cur)
            {
        //        cerr << i;
                who += i + '0';
                for (int j = 0; j < let; j++)
                    cnt[j] -= dig_cnt[i][j];
                ok = true;
                total_cnt -= sz(digits[i]);
            }
        };

        if (cnt['X' - 'A'] >= 1)
            search_dg(6);
        else if (cnt['G' - 'A'] >= 1)
            search_dg(8);
        else if (cnt['Z' - 'A'] >= 1)
            search_dg(0);
        else if (cnt['U' - 'A'] >= 1)
            search_dg(4);
        else if (cnt['F' - 'A'] >= 1)
            search_dg(5);
        else if (cnt['S' - 'A'] >= 1)
            search_dg(7);
        else if (cnt['N' - 'A'] >= 1)
            search_dg(9);
        else if (cnt['W' - 'A'] >= 1)
            search_dg(2);
        else if (cnt['R' - 'A'] >= 1)
            search_dg(3);

        for (int i = 9; i >= 0 && !ok; i--)
            search_dg(i);

        assert(ok);
    }

    sort(ALL(who));
//cerr << endl;
    printf("Case #%d: %s\n", test, who.c_str());
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

   // ios_base::sync_with_stdio(false);
   // cin.tie(0);

    int t;
    cin >> t;

    string n;
    int test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
