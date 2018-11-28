#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace __gnu_pbds;
using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvin;

typedef long long LL;
typedef unsigned long long ULL;

typedef
tree<
    LL,
    null_type,
    less<LL>,
    rb_tree_tag,
    tree_order_statistics_node_update
> ordered_set;

vector<string> nums{"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool solve(vector<int> &ans, map<char, int> &l_cnt, int i, int cnt)
{
    if (cnt == 0)
        return true;
    if (cnt < 0)
        return false;
    if (i >= (int)nums.size())
        return false;

    bool is_valid = true;
    map<char, int> added;
    for (const auto &c : nums[i])
    {
        is_valid &= (l_cnt[c] > 0);
        if (l_cnt[c] > 0)
        {
            added[c]++;
            l_cnt[c]--;
        }
    }

    bool is_soln = false;
    if (is_valid)
    {
        ans.push_back(i);
        is_soln = solve(ans, l_cnt, i, cnt - nums[i].size());
        if (!is_soln)
            ans.pop_back();
    }

    if (is_soln)
        return is_soln;

    for (const auto &it : added)
        l_cnt[it.first] += it.second;

    is_soln = solve(ans, l_cnt, i + 1, cnt);
    return is_soln;
}


int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        string s; cin >> s;
        map<char, int> l_cnt, l_cpy;
        for (const auto &c : s)
        {
            l_cnt[c]++;
            l_cpy[c]++;
        }

        vector<int> ans;
        solve(ans, l_cnt, 0, s.size());
        cout << "Case #" << t << ": ";
        map<char, int> r_cnt;
        for (const auto &a : ans)
        {
            for (const auto &c : nums[a])
                r_cnt[c]++;
            cout << a;
        }
        cout << endl;
    }
    return 0;
}
