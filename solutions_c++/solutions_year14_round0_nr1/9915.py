#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<cmath>
#include<stack>
#include<queue>
#include<set>
#include<iostream>
#define N 110
#define eps 1e-6
#define ll long long
#define db double
#define inf 0x3fffffff
#define A(a) printf("a==%d",a);
#define CC(x,y) memset(x,y,sizeof(x))
#define lson l,mid,rt<<1
#define rson mid+1,r,(rt<<1)+1
using namespace std;
int i,j,k,m,n,x,y,z;
int a[N][N],b[N][N];
int main()
{    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    int t;
    scanf("%d",&t);
    int cas=1;

    while (t--)
    {
        scanf("%d",&x);
        for (i=0;i<4;i++)
            for (j=0;j<4;j++)
              scanf("%d",&a[i][j]);
        scanf("%d",&y);
        for (i=0;i<4;i++)
            for (j=0;j<4;j++)
               scanf("%d",&b[i][j]);
        z=0;
        m=0;
        for (i=0;i<4;i++)
            for (j=0;j<4;j++)
                if (a[x-1][i]==b[y-1][j])
            {
                m=a[x-1][i],z++;
            }
        printf("Case #%d: ",cas++);
        if (z==1)printf("%d\n",m);
        else if (z==0)printf("Volunteer cheated!\n");
          else printf("Bad magician!\n");
    }
}
