#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cmath>
#include <stack>
#include <map>

#pragma comment(linker, "/STACK:1024000000");
#define EPS (1e-8)
#define LL long long
#define ULL unsigned long long LL
#define _LL __int64
#define _INF 0x3f3f3f3f
#define Mod 1000000007
#define LM(a,b) (((ULL)(a))<<(b))
#define RM(a,b) (((ULL)(a))>>(b))

using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);

    int T;

    int icase = 1;

    int ans,i,j,k,a,b;

    scanf("%d",&T);

    while(T--)
    {
        scanf("%d %d %d",&a,&b,&k);

        printf("Case #%d: ",icase++);

        ans = 0;

        for(i = 0;i < a; ++i)
        {
            for(j = 0;j < b; ++j)
            {
                if((i&j) < k)
                    ans++;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}



