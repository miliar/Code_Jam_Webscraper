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
#define ULL unsigned long long int
#define _LL __int64
#define _INF 0x3f3f3f3f
#define Mod 1000000007
#define LM(a,b) (((ULL)(a))<<(b))
#define RM(a,b) (((ULL)(a))>>(b))

const double PI = acos(-1.0);

using namespace std;

int mark[20];

int num[4][5];

int main()
{
    int T;

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    scanf("%d",&T);

    int icase = 1;

    int i,j;

    int x;

    while(T--)
    {
        memset(mark,0,sizeof(mark));

        scanf("%d",&x);

        for(i = 1;i <= 4 ; ++i)
        {
            for(j = 1;j <= 4 ; ++j)
            {
                scanf("%d",&num[i][j]);
            }
        }

        for(i = 1;i <= 4; ++i)
        {
            mark[num[x][i]]++;
        }

        int ans = 0,site;

        scanf("%d",&x);

        for(i = 1;i <= 4; ++i)
        {
            for(j = 1;j <= 4; ++j)
            {
                scanf("%d",&num[i][j]);
            }
        }

        for(i = 1;i <= 4; ++i)
        {
            mark[num[x][i]]++;
            if(mark[num[x][i]] == 2)
                ans++ ,site = num[x][i];
        }

        printf("Case #%d: ",icase++);
        if(ans == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(ans > 1)
        {
            printf("Bad magician!\n");
        }
        else
        {
            printf("%d\n",site);
        }
    }


    return 0;
}





