#include <queue>
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <cassert>
#include <map>
#include <ctime>
#include <cstdlib>
#include <unordered_map>
#include <random>
#include <deque>

using namespace std;

char wins[10000];
int n;

vector <int> recursion(char c, int depth)
{
    if (depth > n)
        return vector <int>(3, 0);
    vector <int> v(3, 0);
    if (depth == n)
    {
        if (c == 'R')
            v[0] = 1;
        if (c == 'P')
            v[1] = 1;
        if (c == 'S')
            v[2] = 1;
        return v;
    }
    vector <int> a = recursion(wins[c], depth + 1);
    for (int i = 0; i < 3; ++i)
        v[i] += a[i];
    a = recursion(c, depth + 1);
    for (int i = 0; i < 3; ++i)
        v[i] += a[i];
    return v;
}

string cur(char c, int depth)
{
    if (depth == n)
        return string(1, c);
    string a = cur(c, depth + 1);
    string b = cur(wins[c], depth + 1);
    if (a > b)
        return b + a;
    else
        return a + b;
}

vector <int> a1;
string s1;

int main()
{
    ::ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    wins['R'] = 'S';
    wins['S'] = 'P';
    wins['P'] = 'R';
    cin >> t;
    for (int test = 1; test <= t; ++test)
    {
        cin >> n;
        int p, r, s;
        cin >> r >> p >> s;
        string ans = "";
        a1 = recursion('R', 0);
        if (r == a1[0] && p == a1[1] && s == a1[2])
        {
            s1 = cur('R', 0);
            if (ans == "" || ans > s1)
                ans = s1;               
        }
        a1 = recursion('P', 0);
        if (r == a1[0] && p == a1[1] && s == a1[2])
        {
            s1 = cur('P', 0);
            if (ans == "" || ans > s1)
                ans = s1;
        }
        a1 = recursion('S', 0);
        if (r == a1[0] && p == a1[1] && s == a1[2])
        {
            s1 = cur('S', 0);
            if (ans == "" || ans > s1)
                ans = s1;
        }
        if (ans == "")
            cout << "Case #" << test << ": IMPOSSIBLE\n";
        else
            cout << "Case #" << test << ": " << ans << "\n";
    }

    return 0;
}