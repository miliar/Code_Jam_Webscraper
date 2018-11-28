#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
#define MAXN 1005
using namespace std;
int n;
int star[MAXN];
bool judge(int mid)
{
    for(int maxT = 1; maxT <= mid; maxT++)
    {
        int temp = 0;
        bool flag = true;
        for(int i = 1; i <= n; i++)
        {
            if(star[i] <= maxT) continue;
            else
            {
                if(star[i] % maxT) temp += (star[i] / maxT);
                else
                    temp += ((star[i] / maxT) - 1);
            }
            if(maxT + temp > mid)
            {
                flag = false;
                break;
            }
        }
        if(flag) return true;
    }
    return false;
}
int solve(int maxNum)
{
    int l = 1, r = maxNum;
    while(l <= r)
    {
        int mid = (l + r) >> 1;
        if(judge(mid)) r = mid - 1;
        else
            l = mid + 1;
    }
    return l;
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("Bout.out", "w", stdout);
    int t;
    int numCase = 1;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        int maxNum = 0;
        for(int i = 1; i <= n; i++)
        {
            int x;
            scanf("%d", &star[i]);
            maxNum = max(maxNum, star[i]);
        }
        int ans = solve(maxNum);
        printf("Case #%d: %d\n", numCase++, ans);
    }
    return 0;
}
