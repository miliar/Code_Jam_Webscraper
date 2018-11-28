#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <ctime>
#include <iostream>
#include <cmath>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cassert>


const long double PI(acosl(-1.0));

#define pb push_back
#define mp(a,b) make_pair(a,b)
#define all(x) x.begin(), x.end()
#define sqr(x) ((x)*(x))
#define F first
#define S second
#define eps 1e-7
#define inf (int)(1e9+7)
#define infll (ll)(1e18+3)
#define sz(x) ((int)x.size())
#define bits(x) __builtin_popcount(x)
#define bitsl(x) __builtin_popcountll(x)


using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef vector < ll > vll;
typedef vector<int> vi;
typedef pair < ll, ll > pll;
typedef pair < int, int > pii;
typedef vector<vi> vii;
typedef int huint;

int f[100000];
int cnt[4];
int m;

int mpar(int v)
{
    if (v == 1) return 3;
    if (v == 2) return 1;
    if (v == 3) return 2;
}
char make(int x)
{
    if (x == 1) return 'R';
    if (x == 2) return 'P';
    if (x == 3) return 'S';
}
void dfs(int v, int c)
{
    f[v] = c;
    if (v >= m)
    {
        return;
    }
    int x = mpar(c);

    dfs(v * 2, c);
    dfs(v * 2 + 1, x);

}
bool check()
{
    vector<int> st(4);
    for (int i(0); i < 4; i++)
        st[i] = 0;
    for (int i(m); i < m * 2; i++)
        st[f[i]]++;
    if (st[1] == cnt[1] && st[2] == cnt[2] && st[3] == cnt[3])
        return true;
    return false;

}
string st;
void resort(string &s, int l, int r)
{
    if (l == r) return;
    int m = (r + l) / 2;
    int ln = (r - l + 1) / 2;
    resort(s, l, m);    resort(s, m + 1, r);
    string ga = s.substr(l, ln);
    string gb = s.substr(m + 1, ln);
    if (ga > gb)
        for (int i = 0; i < ln; ++i)
            swap(s[l + i], s[m + 1 + i]);

}

int  main()
{
    ios_base::sync_with_stdio(false);  cin.tie(0); cout.tie(0);
  //  freopen("input.txt", "r", stdin);
 //   freopen("output.txt", "w", stdout);


    int test;
    cin >> test;
    int tl = 0;
    while (test-- > 0)
    {
        tl++;
        int n, p, r, s;
        cin >> n >> r >> p >> s;
        cnt[1] = r;
        cnt[2] = p;
        cnt[3] = s;

        m = 1 << n;
        string ans = "";
        dfs(1, 1);
        if (check())
        {
            st = "";
            for (int i(m); i < m * 2; i++)
            {
                st = st + make(f[i]);
            }
            resort(st, 0, st.size() - 1);
            if (ans == "" || st < ans)
                ans = st;

        }
        dfs(1, 2);
        if (check())
        {
            st = "";
            for (int i(m); i < m * 2; i++)
            {
                st = st + make(f[i]);
            }
            resort(st, 0, st.size() - 1);
            if (ans == "" || st < ans)
                ans = st;

        }
        dfs(1, 3);
        if (check())
        {
            st = "";
            for (int i(m); i < m * 2; i++)
            {
                st = st + make(f[i]);
            }
            resort(st, 0, st.size() - 1);
            if (ans == "" || st < ans)
                ans = st;
        }
        if (ans == "")
        {
            cout << "Case #" << tl << ": IMPOSSIBLE\n";
        }
        else
        {
            cout << "Case #" << tl << ": " << ans << "\n";
        }
    }

}