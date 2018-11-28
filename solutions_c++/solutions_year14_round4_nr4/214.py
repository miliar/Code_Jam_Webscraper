#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define MP make_pair
#define F first
#define S second

int getNodes(const vector<string> &s)
{
    set<string> p;
    for (string x : s)
        for (int i = 1; i <= x.length(); i++)
            p.insert(x.substr(0, i));
    return p.size() + 1;
}

vector<string> all;
int n, m;
int best, ways;
vector<int> color;

void check()
{
    int sum = 0;
    for (int c = 1; c <= n; c++)
    {
        vector<string> cur;
        for (int i = 0; i < m; i++)
            if (color[i] == c)
                cur.push_back(all[i]);
        if (cur.empty())
            return;
        sum += getNodes(cur);
    }
    if (sum == best)
    {
        ways++;
    }
    else if (sum > best)
    {
        best = sum;
        ways = 1;
    }
}

void gen(int pos)
{
    if (pos == m)
    {
        check();
        return;
    }
    for (int c = 1; c <= n; c++)
    {
        color[pos] = c;
        gen(pos + 1);
    }
}

void solve(int test)
{
    cin >> m >> n;
    all.resize(m);
    color.resize(m);
    best = -1;
    ways = 0;
    for (int i = 0; i < m; i++)
        cin >> all[i];
    gen(0);
    cout << "Case #" << test << ": ";
    cout << best << " " << ways << "\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    #ifdef TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    cout.setf(ios::fixed);
    cout.precision(10);
    cerr.setf(ios::fixed);
    cerr.precision(10);

    int t;
    cin >> t;
    for (int q = 1; q <= t; q++)
        solve(q);

    return 0;
}
