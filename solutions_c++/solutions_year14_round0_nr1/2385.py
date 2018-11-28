//#pragma comment(linker, "/STACK:102400000,102400000")
#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#include<cctype>
#include<string>
#include<algorithm>
#include<iostream>
#include<ctime>
#include<map>
#include<set>
using namespace std;
#define MP(x,y) make_pair((x),(y))
#define PB(x) push_back(x)
typedef long long LL;
//typedef unsigned __int64 ULL;
/* ****************** */
const int INF=1000111222;
const double INFF=1e100;
const double eps=1e-8;
const int mod=20115601;
const int NN=2005;
const int MM=401010;
/* ****************** */

int a[4][4],b[4][4];

int main()
{
    freopen("E:A-small-attempt4.in","r",stdin);
    freopen("E:A-small-attempt4.out","w",stdout);

    int cas,x,y,i,j,n=4;
    int ans[4],tol,ee=0;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d",&x);
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&y);
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                scanf("%d",&b[i][j]);

        tol=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
                if(a[x-1][i]==b[y-1][j])
                {
                    ans[tol++]=a[x-1][i];
                }
        }

        printf("Case #%d: ",++ee);
        if(tol==1)
        {
            printf("%d\n",ans[0]);
        }
        else if(tol==0)
        {
            puts("Volunteer cheated!");
        }
        else
        {
            puts("Bad magician!");
        }
    }
    return 0;
}
