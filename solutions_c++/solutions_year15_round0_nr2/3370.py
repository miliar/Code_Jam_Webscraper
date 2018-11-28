//   <-- Y.L.Asce -->   //
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T,D;
int P[1050];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&T);
    for(int cas = 1;cas <= T;cas++)
    {
        scanf("%d",&D);
        int Max = 0;
        for(int i = 1;i <= D;i++)
        {
            scanf("%d",&P[i]);
            Max = max(Max,P[i]);
        }

        int ans = 100000000;

        for(int eat = 1;eat <= Max;eat++)
        {
            int tmp = eat;

            for(int i=1;i<=D;i++)
                if(P[i] > eat)
            {
                if(P[i] % eat == 0) tmp += P[i]/eat - 1;
                else tmp += P[i]/eat;
            }

            ans = min(ans,tmp);
        }

        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
