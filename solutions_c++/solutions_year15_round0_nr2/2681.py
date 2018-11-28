#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
#include <stack>
#include <map>
#include <cmath>

#pragma comment(linker, "/STACK:1024000000")
#define LL long long int
#define INF 0x3f3f3f3f

using namespace std;

int ans[1010];

int main()
{
    // freopen("B-small-attempt1.in","r",stdin);
      //freopen("B-small-attempt1.out","w",stdout);
    freopen("B-large.in","r",stdin);
     freopen("B-large.out","w",stdout);

    int T,icase = 1;

    int n,Max,i,j,sum,Min;

    scanf("%d",&T);

    while(T--)
    {
        scanf("%d",&n);

        for(Max = 0,i = 1; i <= n; ++i)
        {
            scanf("%d",&ans[i]);
            Max = max(Max,ans[i]);
        }

        int L = 1,R = Max;

        Min = Max;

        for(L = 1; L <= R; ++L)
        {
            int mid = L;
            for(i = 1,sum = 0; i <= n; ++i)
                sum += (ans[i]-1)/mid;
            Min = min(sum+mid,Min);
        }


        printf("Case #%d: %d\n",icase++,Min);
    }

    return 0;
}
