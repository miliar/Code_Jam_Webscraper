#include<iostream>
#include<cstdio>
using namespace std;
int main(void)
{
    int a[4][4];
    int b[4][4];
    int i,j,k,l,t,x=0;
    scanf("%d",&t);
    while(t--)
    {
        x++;
    scanf("%d",&k);
    k-=1;
    for(i=0;i<=3;i++)
    {
        for(j=0;j<=3;j++)
            scanf("%d",&a[i][j]);
    }
    scanf("%d",&l);
    l-=1;
    for(i=0;i<=3;i++)
    {
        for(j=0;j<=3;j++)
            scanf("%d",&b[i][j]);
    }
    int c=0,d;
    for(i=0;i<=3;i++)
    {
        for(j=0;j<=3;j++)
        {
            if(a[k][i]==b[l][j])
            {
                c++;
                d=a[k][i];
            }
        }
    }
    if(c==1)
        printf("Case #%d: %d\n",x,d);
    else if(c>1)
        printf("Case #%d: Bad magician!\n",x);
    else if(c==0)
        printf("Case #%d: Volunteer cheated!\n",x);
    }
    return 0;
}
