#define _CRT_SECURE_NO_WARNINGS
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iterator>
#include <ctime>
#include <iomanip>

using namespace std;

vector<int> f;

int bf()
{
    int n = f.size() - 1;
    int res = 0;

    for (int mask = 1; mask < (1 << n); ++mask)
    {
        vector<int> v;
        for (int i = 0; i < n; ++i)
            if (mask & (1 << i))
                v.push_back(i+1);

        int cs = v.size();
        if (cs == 1 || cs <= res)
            continue;

        do
        {
            bool ok = true;
            for (int i = 1; i+1 < v.size(); ++i)
            {
                if (f[v[i]] != v[i-1] && f[v[i]] != v[i + 1])
                    ok = false;
            }

            if (f[v[0]] != v[1] && f[v[0]] != v[cs - 1])
                ok = false;

            if (f[v[cs - 1]] != v[0] && f[v[cs - 1]] != v[cs - 2])
                ok = false;

            if (ok)
                res = max<int>(res, cs);

        } while (next_permutation(v.begin(), v.end()));

    }

    return res;
}


int main()
{
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        int n;
        cin >> n;
        f.clear();
        f.resize(n + 1);

        for (int i = 1; i <= n; ++i)
        {
            // i -> a
            int a; cin >> a;

            f[i] = a;
        }

        printf("Case #%d: ", CASE);
        {
            int res2 = bf();

            cout << res2 << endl;
        }
    }


    return 0;
}
