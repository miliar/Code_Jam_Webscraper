#include <stdio.h>
int a[1005]={0};
int fun()
{
    int i;
    a[11*11]=1,a[22*22]=1;
    for(i=1;i<=3;i++)
    {
     a[i*i]=1;
    }
    return 0;
}
int main()
{
    freopen("A1.in","r",stdin);
    freopen("A1.txt","w",stdout);
     fun();
    int t,r=1,c,i,d,sum;
    scanf("%d",&t);
    while(t--)
    {
        sum=0;
        scanf("%d %d",&c,&d);
        printf("Case #%d: ",r);
        for(i=c;i<=d;i++)
        {
            if(a[i]==1) sum++;
        }
        printf("%d\n",sum);
        r++;
    }
    return 0;
}
