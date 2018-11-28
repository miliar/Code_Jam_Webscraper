#include <bits/stdc++.h>

using namespace std;

#define lol long long
#define fi first
#define se second
#define pb push_back
#define sz(s) (int)s.size()
#define must ios_base::sync_with_stdio(0)

#define inp(s) freopen(s, "r", stdin)
#define out(s) freopen(s, "w", stdout)

char nx[300];
int n, p, r, s;

string solve(int cur, char c)
{
    if (cur == n)
    {
        switch(c)
        {
            case 'p': p--; break;
            case 'r': r--; break;
            case 's': s--; break;
        }
        if (p >= 0 && r >= 0 && s >= 0)
        {
            string d;
            d += c - 'a' + 'A';
            return d;
        }
        switch(c)
        {
            case 'p': p++; break;
            case 'r': r++; break;
            case 's': s++; break;
        }
    return "";
    }
    else
    {
        string d = solve(cur + 1, min(c, nx[c]));
        string d1 = solve(cur + 1, max(c, nx[c]));
        if (d == "" || d1 == "")
        {
            d1 = d = "";
        }
        return min(d, d1) + max(d, d1);
    }
}

int main()
{
    inp("input.txt");
    out("output.txt");
    int t, tt;
    scanf("%d", &t);
    nx['p'] = 'r';
    nx['r'] = 's';
    nx['s'] = 'p';
    for (tt = 1; tt <= t; tt++)
    {
        int r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        string ans = "z";
        ::r = r;
        ::p = p;
        ::s = s;
        string curr = solve(0, 'r');
        if (curr != "") {
            ans = min(ans, curr);
        }
        ::r = r;
        ::p = p;
        ::s = s;
        curr = solve(0, 'p');
        if (curr != "") {
            ans = min(ans, curr);
        }
        ::r = r;
        ::p = p;
        ::s = s;
        curr = solve(0, 's');
        if (curr != "") {
            ans = min(ans, curr);
        }
        cout << "Case #" << tt << ": ";
        cout << (ans == "z" ? "IMPOSSIBLE\n" : ans + "\n");
    }
    return 0;

}
