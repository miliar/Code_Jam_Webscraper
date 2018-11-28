#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

char get_winner(char a, char b)
{
    if (a == b)
        return -1;
    if (a > b)
        swap(a, b);
    if (a == 'P' && b == 'R')
        return 'P';
    if (a == 'P' && b == 'S')
        return 'S';
    if (a == 'R' && b == 'S')
        return 'R';
    assert(false);
}

bool is_good(string s)
{
    while ((int)s.length() > 1)
    {
        string q;
        for (int i = 0; i < (int)s.length(); i += 2)
        {
            char c = get_winner(s[i], s[i + 1]);
            if (c == -1)
                return false;
            q += c;
        }
        s = q;
    }
    return true;
}

string slow(int n, int r, int p, int s)
{
    string init_guys;
    for (int i = 0; i < r; i++)
        init_guys += 'R';
    for (int i = 0; i < p; i++)
        init_guys += 'P';
    for (int i = 0; i < s; i++)
        init_guys += 'S';

    vector<int> perm(n);
    for (int i = 0; i < n; i++)
        perm[i] = i;
    string best = "Z";

    do
    {
        string guys;
        for (int i = 0; i < n; i++)
            guys += init_guys[perm[i]];
        if (is_good(guys))
            best = min(best, guys);
    }
    while (next_permutation(perm.begin(), perm.end()));

    return best;
}

string gen(int n, char c)
{
    if (n == 1)
        return string(1, c);
    string s1, s2;
    if (c == 'P')
    {
        s1 = gen(n / 2, 'P');
        s2 = gen(n / 2, 'R');
    }
    else if (c == 'R')
    {
        s1 = gen(n / 2, 'R');
        s2 = gen(n / 2, 'S');
    }
    else
    {
        s1 = gen(n / 2, 'S');
        s2 = gen(n / 2, 'P');
    }
    if (s1 > s2)
        swap(s1, s2);
    return s1 + s2;
}

void solve()
{
    int n, r, p, s;
    scanf("%d%d%d%d", &n, &r, &p, &s);
    n = 1 << n;

    string best = "Z";
    for (char start : {'P', 'R', 'S'})
    {
        string cur = gen(n, start);
        int cnt_p = 0, cnt_r = 0, cnt_s = 0;
        for (char c : cur)
        {
            if (c == 'P')
                cnt_p++;
            if (c == 'R')
                cnt_r++;
            if (c == 'S')
                cnt_s++;
        }
        if (cnt_p == p && cnt_r == r && cnt_s == s)
            best = min(best, cur);
    }

    //assert(best == slow(n, r, p, s));

    if (best == "Z")
        cout << "IMPOSSIBLE" << endl;
    else
        cout << best << endl;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }

    eprintf("time = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
}
