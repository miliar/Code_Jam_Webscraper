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

vector <int> cur;
vector <long double> prob;
int n, k;

bool gennext(vector <int> &cur)
{
    for (int i = k - 1; i >= 0; --i)
    {
        if (cur[i] != n - (k - i))
        {
            ++cur[i];
            for (int j = i + 1; j < k; ++j)
                cur[j] = cur[i] + j - i;
            return true;
        }
    }
    return false;
}

map <pair <int, int>, long double> mp;

long double recur(int i, int k)
{
    if (mp.count({ i, k }))
        return mp[{i, k}];
    if (i == 0)
    {
        if (k == 1)
            return prob[cur[i]];
        if (k == 0)
            return 1 - prob[cur[i]];
        return 0;
    }
    mp[{i, k}] = recur(i - 1, k - 1) * prob[cur[i]] + recur(i - 1, k) * (1 - prob[cur[i]]);
    return mp[{i, k}];
}

int main()
{
    ::ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    cout.precision(20);
    for (int test = 1; test <= t; ++test)
    {
        cin >> n >> k;
        prob.resize(n);
        for (int i = 0; i < n; ++i)
            cin >> prob[i];
        cur.resize(k);
        for (int i = 0; i < k; ++i)
            cur[i] = i;
        long double ans = 0;
        while (true)
        {
            mp.clear();
            ans = max(ans, recur(k - 1, k / 2));
            if (!gennext(cur))
                break;
        }
        cout << "Case #" << test << ": " << fixed << ans << endl;
    }
    return 0;
}