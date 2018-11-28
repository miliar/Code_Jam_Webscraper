#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;
const int maxn = 1005;

int N;
int m[maxn];

int solve1()
{
    int ans = 0;
    for(int i=1;i<N;i++)
    {
        if(m[i] < m[i-1])ans += m[i-1] - m[i];
    }
    return ans;
}

int f(int x)
{
    int ans = 0;
    int cur = m[0];
    for(int i=1; i<N; i++)
    {
        ans += min(x, cur);
        cur -= x;
        if(cur < 0)cur = 0;
        if(cur <= m[i])
        {
            cur = m[i];
        }
        else
        {
             return 0x3f3f3f3f;
        }
    }
    return ans;
}

int solve2()
{
    int l=1, r=10000;
    int ans = 0x3f3f3f3f;

    for(int i=0;i<=r;i++)
    {
        //if(f(i) == 253)printf("i = %d\n", i);
        ans = min(ans, f(i));
    }
    /*
    while(l <= r)
    {
        int mid = (l + r)/2;
        int midmid = (mid + r)/2;
        int y1 = f(mid);
        int y2 = f(midmid);
        //printf("%d %d %d %d\n",l ,r, y1, y2);
        ans = min(ans, y1);
        ans = min(ans, y2);
        if(y1 < y2)
        {
            r = midmid - 1;
        }
        else
        {
            l = mid + 1;
        }
    }
    */

    return ans;
}

int main()
{
    int T;
    freopen("in.txt","r",stdin);
    freopen("codejam.ans","w",stdout);
    cin >> T;
    int cas = 1;
    while(T --)
    {
        cin >> N;
        for(int i=0; i<N;i ++)
        {
            cin >> m[i];
        }
        int ans1 = solve1();
        int ans2 = solve2();
        printf("Case #%d: %d %d\n",cas++, ans1, ans2);
    }
    return 0;
}
