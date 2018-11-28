#include <bits/stdc++.h>
#ifndef M_PI
#define M_PI 3.14159265358979323846264338327
#endif // M_PI
#define endl "\n"
#define S struct
#define X first
#define Y second
#define V vector
#ifndef __linux__
#define LLD "%I64d"
#else
#define LLD "%ll""d"
#endif
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
typedef long double LD;
typedef unsigned long long ULL;
typedef pair <int, int> PII;
typedef pair <LL, LL> PLL;
const int MOD = 1000000007;
void sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); }
S Sync_stdio { Sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); } } _sync_stdio;

string minimize(string s)
{
    if (s.size() == 1) {
        return s;
    }
    int n = s.size();
    string s1 = minimize(s.substr(0, n / 2));
    string s2 = minimize(s.substr(n / 2, n / 2));
    if (s1 + s2 < s2 + s1) {
        return s1 + s2;
    }
    return s2 + s1;
}

int solve(int t)
{
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    vector <vector <int>> dp(n + 1, vector <int> (10000));
    dp[0][0] = 1;
    FOR (i, 0, n) {
        FOR (j, 0, 1 << i) {
            dp[i + 1][2 * j] = dp[i][j];
            dp[i + 1][2 * j + 1] = (dp[i][j] + 2) % 3;
        }
    }
    string ans1;
    string ans2;
    string ans3;
    FOR (i, 0, 1 << n) {
        if (dp[n][i] == 2) {
            ans1.push_back('R');
            ans2.push_back('P');
            ans3.push_back('S');
        }
        if (dp[n][i] == 1) {
            ans1.push_back('P');
            ans2.push_back('S');
            ans3.push_back('R');
        }
        if (dp[n][i] == 0) {
            ans1.push_back('S');
            ans2.push_back('R');
            ans3.push_back('P');
        }
    }
    ans1 = minimize(ans1);
    ans2 = minimize(ans2);
    ans3 = minimize(ans3);
    string ans(1, 'Z' + 3);
    if (count(IT(ans1), 'R') == r && count(IT(ans1), 'P') == p && count(IT(ans1), 'S') == s) {
        ans = min(ans1, ans);
    }
    if (count(IT(ans2), 'R') == r && count(IT(ans2), 'P') == p && count(IT(ans2), 'S') == s) {
        ans = min(ans2, ans);
    }
    if (count(IT(ans3), 'R') == r && count(IT(ans3), 'P') == p && count(IT(ans3), 'S') == s) {
        ans = min(ans3, ans);
    }
    if (ans == string(1, 'Z' + 3)) {
        CASE(t + 1, "IMPOSSIBLE");
    } else {
        CASE(t + 1, ans);
    }
    return 0;
}

int go(string s) {
    if (s.size() == 1) {
        return 1;
    }
    string s2;
    for (int i = 0; i < s.size(); i += 2) {
        if (s[i] == s[i + 1]) {
            return 0;
        }
        if (s[i] == 'R' && s[i + 1] == 'S') {
            s2 += 'R';
        }
        if (s[i] == 'S' && s[i + 1] == 'R') {
            s2 += 'R';
        }
        if (s[i] == 'P' && s[i + 1] == 'S') {
            s2 += 'S';
        }
        if (s[i] == 'S' && s[i + 1] == 'P') {
            s2 += 'S';
        }
        if (s[i] == 'P' && s[i + 1] == 'R') {
            s2 += 'P';
        }
        if (s[i] == 'R' && s[i + 1] == 'P') {
            s2 += 'P';
        }
    }
    return go(s2);
}

int solve2(int t)
{
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    string ss;
    ss += string(r, 'R');
    ss += string(p, 'P');
    ss += string(s, 'S');
    sort(IT(ss));
    do {
        if (go(ss)) {
            CASE(t + 1, ss);
            return 0;
        }
    } while (next_permutation(IT(ss)));
    CASE(t + 1, "IMPOSSIBLE");
    return 0;
}

int main()
{
    int n;
    cin >> n;
    FOR (i, 0, n) {
        solve(i);
    }
    return 0;
}
