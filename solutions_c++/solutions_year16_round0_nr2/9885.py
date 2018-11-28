#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <ctime>
#include <unordered_map>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const double eps = 1e-10;
const int inf = 1000000000;

const int N = 100005;
const int mo = 1000000000 + 7;



void work()
{
    string s;
    cin >> s;
    map<string, int> f;
    f[s] = 0;
    queue<string> Q;
    Q.push(s);
    while (!Q.empty())
    {
        string s = Q.front();
        Q.pop();
        for (int pre = 0; pre < sz(s); ++pre)
        {
            string p = "", q = "";
            for (int i = 0; i < sz(s); ++i)
            {
                if (i <= pre) p += s[i];
                else q += s[i];
            }
            reverse(p.begin(), p.end());
            for (int i = 0; i < sz(p); ++i)
                if (p[i] == '+') p[i] = '-';
                else p[i] = '+';
            string t = p + q;
            if (f.count(t)) continue;
            f[t] = f[s] + 1;
            Q.push(t);
        }
    }
    for (int i = 0; i < sz(s); ++i)
        s[i] = '+';
    assert(f.count(s));
    cout << f[s] << endl;
}

int main()
{
    #ifdef LOCAL_TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
