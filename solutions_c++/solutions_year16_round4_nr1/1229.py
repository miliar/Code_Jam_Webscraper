#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <ctime>
#include <cstdio>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <memory>
#include <bitset>
#include <functional>
#include <cassert>
#include <fstream>
#include <chrono>
using namespace std;


#define fori(i, n) for (int i = 0; i < (int)(n); i++)
#define mp(x, y) make_pair((x), (y))

int tres[] = { 2, 0, 1 };
char cres[] = { 'R', 'P', 'S' };
vector<pair<int, int> > v;
vector<int> game;
vector<int> cur, v_next;


string dfs(int level, int t, int n)
{
    if (level == n)
    {
        string p;
        p += cres[t];
        return p;
    }
    game[tres[t]]--;
    string a1 = dfs(level + 1, t, n), a2 = dfs(level + 1, tres[t], n);
    if (a1 < a2)
        return a1 + a2;
    return a2 + a1;
}

bool try_game(int n, string &ans)
{
    string tans;
    tans = dfs(0, cur.front(), n);

    for (int j = 0; j < 3; j++)
        if (game[j] != 0)
            return false;
        
    if (ans == "" || tans < ans)
        ans = tans;
    return true;
}

void run()
{
    int n, r, p, s;
    cin >> n >> r >> p >> s;

    cur.clear();
    v_next.clear();
    v = { mp(p, 1), mp(r, 0), mp(s, 2) };
    game = { r, p, s };
    //r = 0, p = 1, s = 2

    string ans;
    bool is_ok = false;

    for (int j = 0; j < 3; j++)
        if (v[j].first != 0)
        {
            cur.push_back(v[j].second);
            game[v[j].second]--;
            is_ok |= try_game(n, ans);
            cur.clear();
            game = { r, p, s };
        }
    if (is_ok)
        cout << ans << endl;
    else
        cout << "IMPOSSIBLE" << endl;
    return;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;

    fori(i, tests)
    {
        cout << "Case #" << to_string(i + 1) << ": ";
        run();
    }
 
    return 0;
}