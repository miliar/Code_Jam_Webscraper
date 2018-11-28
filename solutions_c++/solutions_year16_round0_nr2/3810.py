#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <cstdio>
#include <cassert>

using namespace std;

#define forsn(i, s, n) for (int i = s; i < n; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())
#define all(n) n.begin(), n.end()

char flip(char c)
{
    if (c == '+')
        return '-';
    else if (c == '-')
        return '+';
    else
        assert(false);
}

string flipOn(const string &s, int w)
{
    assert(w < s.size());

    string r(s.size(), '.');
    transform(s.rbegin() + s.size() - w - 1, s.rend(), r.begin(), [](char c) { return flip(c); });
    copy(s.begin() + w + 1, s.end(), r.begin() + w + 1);

    return r;
}

int solve(const string &s)
{
    queue <string> q;
    unordered_map <string, int> t;

    q.push(s);
    while (!q.empty())
    {
        string a = q.front(); q.pop();
        int p = t[a];

        if (none_of(all(a), [](char c) { return c == '-'; }))
            return p;

        fore (i, a)
        {
            string y = flipOn(a, i);
            if (t.find(y) == t.end())
            {
                t[y] = p + 1;
                q.push(y);
            }
        }
    }

    assert(false);
}

int main()
{
    int t;
    cin >> t;

    forsn(z, 1, t + 1)
    {
        string s;
        cin >> s;

        printf("Case #%d: %d\n", z, solve(s));
    }
}

