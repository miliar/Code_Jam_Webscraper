#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
using namespace std;

#define eps 1e-9
#define PB push_back
#define LL long long
#define INF 0x3f3f3f3f

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}

int lcp(string a, string b)
{
    int i, j, n = min(a.size(), b.size());
    for(i = 0; i < n; i++)
        if(a[i] != b[i])
            break;
    return i;
}
int getCount(vector<string> &mset)
{
    int i, j, ret = 1;
    for(i = 0; i < mset.size(); i++)
    {
        int maxlcp = 0;
        for(j = 0; j < i; j++)
            checkMax(maxlcp, lcp(mset[i], mset[j]));
        ret += mset[i].size() - maxlcp;
    }
    return ret;
}
string str[10];
vector<string> mset[5];
int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int t, n, m, cas = 1, i, j;
    cin >> t;
    while(t--)
    {
        cin >> m >> n;
        for(i = 0; i < m; i++)
            cin >> str[i];
        int tot = 1;
        for(i = 0; i < m; i++)
            tot *= n;
        int ans = 0, way = 0;
        for(i = 0; i < tot; i++)
        {
            for(j = 0; j < n; j++)
                mset[j].clear();
            int mask = i;
            for(j = 0; j < m; j++)
            {
                int idx = mask % n;
                mset[idx].push_back(str[j]);
                mask /= n;
            }
            for(j = 0; j < n; j++)
                if(mset[j].size() == 0)
                    break;
            if(j < n)  continue;
            int sum = 0;
            for(j = 0; j < n; j++)
                sum += getCount(mset[j]);
            if(sum > ans)
            {
                ans = sum;
                way = 1;
            }
            else if(sum == ans)
            {
                way++;
            }
        }
        printf("Case #%d: %d %d\n", cas++, ans, way);
    }
    return 0;
}
