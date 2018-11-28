#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<time.h>
#include<stdlib.h>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#define LL long long
using namespace std;
int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int T, cse = 1;
    scanf("%d", &T);
    while(T--)
    {
        int a[1005];
        int n;
        int ans1 = 0, ans2 = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        int maxx = 0;
        for(int i = 0; i < n - 1; i++)
        {
            if(a[i] - a[i + 1] > 0)
            {
                maxx = max(maxx, a[i] - a[i + 1]);
                ans1 += a[i] - a[i + 1];
            }
        }
        for(int i = 0; i < n - 1; i++)
        {
            if(a[i] < maxx)
                ans2 += a[i];
            else
                ans2 += maxx;
        }
        printf("Case #%d: %d %d\n", cse++, ans1, ans2);
    }
    return 0;
}

