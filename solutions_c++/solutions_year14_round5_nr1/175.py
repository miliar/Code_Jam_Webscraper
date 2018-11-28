#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
using namespace std;


typedef long long LL;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}
const int N = 1000005;
int num[N];
LL sum[N];
LL getMax(int mid, int n)
{
    return max(sum[mid - 1], sum[n] - sum[mid - 1]);
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 1, i, j;
    int n, p, q, r, s;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
        int cur = 0;
        for(i = 1, sum[0] = 0; i <= n; i++)
        {
            num[i] = ((LL)(i - 1) * p + q) % r + s;
            sum[i] = sum[i - 1] + num[i];
        }
        LL ans = 0;
        for(i = 1; i <= n; i++)
        {
            LL rv = sum[n] - sum[i];
            int l = 1, r = i;
            while(l + 1 < r)
            {
                //cout << l << " " << r << endl;
                int lmid = (l + r) / 2;
                int rmid = (lmid + r) / 2;
                LL lans = getMax(lmid, i);//max(sum[lmid - 1], sum[r] - sum[lmid - 1]);
                LL rans = getMax(rmid, i);//max(sum[rmid - 1], sum[r] - sum[rmid - 1]);
                if(lans < rans) r = rmid;
                else            l = lmid;
            }
            LL lv = min(getMax(l, i), getMax(r, i));

            //if(i == 6)  cout << lv << endl;
            checkMax(ans, sum[n] - max(lv, rv));
        }
       // cout << ans << endl;
        printf("Case #%d: %.10lf\n", cas++, ans * 1.0 / sum[n]);
    }
    return 0;
}
