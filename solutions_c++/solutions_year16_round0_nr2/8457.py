#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvin;

typedef long long LL;
typedef unsigned long long ULL;

map<char, char> opp {
    {'+', '-'},
    {'-', '+'}
};

LL f(LL i, char b, const string &s, map<pair<int, char>, LL> &dp)
{
    if (i == 0)
        return s[i] == b ? 0 : 1;

    auto pr = make_pair(i, b);
    if (!dp.count(pr))
    {
        if (s[i] == b)
        {
            dp[pr] = min(f(i - 1, b, s, dp), f(i - 1, opp[b], s, dp) + 1);
        }
        else
        {
            dp[pr] = min(f(i - 1, opp[b], s, dp) + 1, f(i - 1, b, s, dp) + 2);
        }
    }

    return dp[pr];
}

int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    LL T; cin >> T;
    for (LL t = 1; t <= T; ++t)
    {
        string s; cin >> s;
        map<pair<int, char>, LL> dp;
        cout << "Case #" << t << ": " << f(s.size() - 1, '+', s, dp) << endl;
    }

    return 0;
}
