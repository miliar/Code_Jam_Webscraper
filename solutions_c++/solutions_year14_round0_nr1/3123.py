#pragma warning(disable:4786)
#include<iostream>
#include<algorithm>
#include<cmath>
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<queue>
#include<set>
#include<vector>
#include<string>
#include<ctime>
#include<string.h>
using namespace std;
#define pi acos(-1.0)
//#define LL __int64
typedef long long LL;
#define INF 0x7fffffffffffffff
#define bug puts("hear!")
#define inf 0x7fffffff
#define eps 1e-10
#define FRE freopen("A-small-attamp1.in","r",stdin)
#define E exp(1.0)
#define mod 1000000007
#include<stdio.h>
#include<string.h>
#include<stdbool.h>

int i,j,n,m,t,sum,p,
    a[10][10],b[10][10];
bool c[20];

int
pre()
{
    memset(a,0,sizeof(a));
    memset(b,0,sizeof(b));
    memset(c,0,sizeof(c));
    sum=0;
    return 0;
}

int
init()
{
    scanf("%d",&n);

    for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&a[i][j]);

    scanf("%d",&m);

    for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&b[i][j]);

    return 0;
}

int
main()
{
    int casi;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&t);
for(casi=1;casi<=t;casi++)
{
    pre();
    init();

    for(i=1;i<=4;i++)
    c[a[n][i]]=true;

    for(i=1;i<=4;i++)
    if(c[b[m][i]])
    {
        sum++;
        p=b[m][i];
    }

    if(sum==1) printf("Case #%d: %d\n",casi,p);
    else if(sum==0) printf("Case #%d: Volunteer cheated!\n",casi);
    else printf("Case #%d: Bad magician!\n",casi);

}

    return 0;
}
