#include <bits/stdc++.h>
#ifndef M_PI
#define M_PI 3.14159265358979323846264338327
#endif // M_PI
#define endl "\n"
#define FOR(x, y, z) for (int x = (y); x < (z); ++x)
#define FORR(x, y, z) for (int x = (y); x > (z); --x)
#define GET(a, n) for (int __i = 0; __i < (n); ++__i) cin >> a[__i];
#define GETM(a, n, m) for (int __i = 0; __i < (n); ++__i) for (int __j = 0; __j < m; ++__j) cin >> a[__i][__j];
#define PRINTM(a, n, m) for (int __i = 0; __i < (n); ++__i) { for (int __j = 0; __j < m; ++__j) cout << a[__i][__j] << " ";  cout << endl; };
#define PRINT(a, n) for (int __i = 0; __i < (n); ++__i) cout << a[__i] << " ";
#define IT(a) a.begin(), a.end()
#define SQR(x) (x) * (x)
#define CASE(a, s) cout << "Case #" << a << ": " << s << endl;
#define DEB(a) cout << #a << " = " << (a) << endl; cout.flush();
#define DEBA(a) for (auto __i: a) cout << __i << " "; cout << endl; cout.flush();
#define IFDEB(b, a) if (b) { cout << #a << " = " << (a) << endl; cout.flush(); }
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair <int, int> PII;
typedef pair <LL, LL> PLL;
const int MOD = 1000000007;
struct Sync_stdio { Sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); } } _sync_stdio;

int encode(const string &s)
{
    int x = 0;
    FOR (i, 0, s.size()) {
        x <<= 1;
        x += s[i] == '-';
    }
    return x;
}

string decode(int x, int n)
{
    string ans = "";
    FOR (i, 0, n) {
        ans.push_back(x % 2 == 1 ? '-' : '+');
        x /= 2;
    }
    reverse(IT(ans));
    return ans;
}

string flip(string x, int pos)
{
    reverse(x.begin(), x.begin() + pos + 1);
    FOR (i, 0, pos + 1) {
        x[i] = x[i] == '+' ? '-' : '+';
    }
    return x;
}

vector <vector <int>> g;
vector <int> d;

void bfs(int x)
{
    queue <int> q;
    q.push(x);
    d[x] = 0;
    while (q.size()) {
        int t = q.front();
        q.pop();
        for (auto i: g[t]) {
            if (d[i] != -1) {
                continue;
            }
            d[i] = d[t] + 1;
            q.push(i);
        }
    }
}

int solve(int l)
{
    string s;
    cin >> s;
    while (s.size() && s.back() == '+') {
        s.pop_back();
    }
    int ans = !!s.size();
    FOR (i, 0, int(s.size()) - 1) {
        if (s[i] != s[i + 1]) {
            ++ans;
        }
    }
    CASE(l + 1, ans);
    /*g.assign(1 << s.size(), vector <int> ());
    d.assign(1 << s.size(), -1);
    FOR (i, 0, (1 << s.size())) {
        string t = decode(i, s.size());
        FOR (k, 0, s.size()) {
            int j = encode(flip(t, k));
            g[i].push_back(j);
        }
    }
    bfs(encode(s));*/
    return 0;
}

int main()
{
    int t;
    cin >> t;
    FOR (i, 0, t) {
        solve(i);
    }
}
