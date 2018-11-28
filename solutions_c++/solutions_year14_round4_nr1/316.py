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

const int N = 705;
int cnt[N];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 1, n, x, s, i, j;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &n, &x);
        memset(cnt, 0, sizeof(cnt));
        for(i = 1; i <= n; i++)
        {
            scanf("%d", &s);
            cnt[s]++;
        }
        int ans = 0;
        for(i = 1; i <= 700; i++)
        {
            while(cnt[i])
            {
                cnt[i]--;
                for(j = x - i; j >= i; j--)
                {
                    if(cnt[j] > 0)
                    {
                        cnt[j]--;
                        break;
                    }
                }
                ans++;
            }
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
