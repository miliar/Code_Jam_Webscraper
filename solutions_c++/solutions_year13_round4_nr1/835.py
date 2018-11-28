#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>

#pragma comment(linker, "/stack:64000000")

using namespace std;

typedef unsigned long long u64;
typedef long long int i64;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vii;
typedef vector<bool> vb;
typedef vector<vb> vvb;

const int MOD = 1000002013;
const int INF = 1000 * 1000 * 1000;
const double EPS = 1e-9;
const long double PI = acos(-1.0);

int main() 
{
    std::ios_base::sync_with_stdio(false);
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t;
    cin >> t;
    map<pii, u64 > a;
    map<pii, u64 >::iterator it, jt, tmp;
    for (int cnt = 1; cnt <= t; ++cnt)
    {
        int n, m;
        cin >> n >> m;

        a.clear();
        int sum_p = 0;
        for (int i = 0; i < m; ++i)
        {
            int o, e, p;
            cin >> o >> e >> p;
            sum_p += p;
            if (a.count(make_pair(o, e)))
            {
                a[make_pair(o, e)] += p;
            }
            else
            {
                a.insert(make_pair(make_pair(o, e), p));
            }
        }
        
        u64 res = 0;
        int sum_p1 = 0;
        for (it = a.begin(); it != a.end(); ++it)
        {
            jt = it;
            for (++jt; jt != a.end() && jt->first.first <= it->first.second; ++jt);
            --jt;
            if (jt == it) 
            {
                sum_p1 += it->second;
                continue;
            }
            for (; it->second > 0 && jt->first.first > it->first.first; )
            {
                if (jt->second > 0 && jt->first.second > it->first.second)
                {
                    u64 d0 = jt->first.first - it->first.first;
                    u64 l2 = jt->first.second - jt->first.first;
                    u64 l1 = it->first.second - it->first.first;
                    
                    int new_p = min(it->second, jt->second);
                    res = (res + (d0 * (d0 + l2 - l1)) % MOD * (new_p % MOD)) % MOD;
                    if (a.count(make_pair(jt->first.first, it->first.second)))
                    {
                        a[make_pair(jt->first.first, it->first.second)] += new_p;
                    }
                    else
                    {
                        a.insert(make_pair(make_pair(jt->first.first, it->first.second), new_p));
                    }

                    if (a.count(make_pair(it->first.first, jt->first.second)))
                    {
                        a[make_pair(it->first.first, jt->first.second)] += new_p;
                    }
                    else
                    {
                        a.insert(make_pair(make_pair(it->first.first, jt->first.second), new_p));
                    }

                    it->second -= new_p;
                    jt->second -= new_p;
                    if (jt->second == 0)
                    {
                        tmp = jt;
                        --jt;
                        a.erase(tmp);
                    }
                    else
                    {
                        break;
                    }
                }
                else
                {
                    --jt;
                }
            }
            sum_p1 += it->second;
        }
        cout << "Case #" << cnt << ": " << res << endl;
    }

    return 0;	
}