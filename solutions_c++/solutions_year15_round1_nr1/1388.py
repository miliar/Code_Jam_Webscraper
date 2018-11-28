#ifndef SOLUTION_HPP
#define SOLUTION_HPP

#include <QTextStream>
#include <QDebug>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define sz(x) int((x).size())
#define pb(x) push_back(x)
#define mkp(a, b) make_pair(a, b)
#define F first
#define S second
#define whole(a) a.begin(), a.end()
#define FOR(i, S, N) for (int i = S; i < N; ++i)
#define contains(C, key) (C.find(key) != C.end())
typedef vector<int> VInt;
typedef vector<VInt> VVInt;
typedef pair<int, int> PII;
typedef long long int int64;
typedef unsigned int uint;

struct Solution
{
    void input(QTextStream &in)
    {
        Q_UNUSED(in)
        in >> n;
        m.assign(n, 0);
        FOR(i, 0, n)
            in >> m[i];
    }

    void solve()
    {
        int max_diff = -1;

        ans1 = 0;
        FOR(i, 1, n)
        {
            int diff = m[i - 1] - m[i];
            if (diff > 0)
                ans1 += diff;

            max_diff = max(diff, max_diff);
        }

        ans2 = 0;
        FOR(i, 0, n - 1)
        {
            ans2 += min(max_diff, m[i]);
        }
    }

    void output(QTextStream &out)
    {
        Q_UNUSED(out)
        out << ans1 << " " << ans2 << "\n";
    }

protected:
    // input:
    int n;
    VInt m;

    // output:
    int64 ans1, ans2;

};

#endif // SOLUTION_HPP
