#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;
int t,i,a,b,c[5][5],d[5][5],j,k,e,f;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        e=f=0;
        scanf("%d",&a);
        for(j=1;j<5;j++)for(k=1;k<5;k++)scanf("%d",&c[j][k]);
        scanf("%d",&b);
        for(j=1;j<5;j++)for(k=1;k<5;k++)scanf("%d",&d[j][k]);
        for(j=1;j<5;j++)for(k=1;k<5;k++)if(c[a][j]==d[b][k])
        {
            e=c[a][j];
            f++;
        }
        printf("Case #%d: ",i);
        if(f==1)printf("%d\n",e);
        else if(f>1)printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
    return 0;
}
