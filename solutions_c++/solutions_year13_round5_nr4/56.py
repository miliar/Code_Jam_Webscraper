#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define for1(i, n) for (int i = 1; i <= (int)(n); i++)
#define forv(i, v) forn(i, v.size())

typedef pair<int, int> pii;
typedef long long ll;

string s;
int n;
map<string, double> d;

string mins(string s)
{
    string ret = s;
    forn(i, n - 1)
    {
        rotate(s.begin(), s.begin() + 1, s.end());
        ret = min(ret, s);
    }
    return ret;
}

double calc(string s)
{
    if (s.find('.') == string::npos) return 0.0;
    if (d.count(s)) return d[s];

    double ret = 0;

    forn(i, n)
    {
        int j = i, k = 0;
        while (s[j] == 'X')
        {
            k++;
            j = (j + 1) % n;
        }
        string ns = s;
        ns[j] = 'X';
        ret += calc(mins(ns)) + n - k;
    }

    return d[s] = ret / n;
}

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    cin >> s;
    n = s.size();
    d.clear();
    printf("%.10lf\n", calc(mins(s)));
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
