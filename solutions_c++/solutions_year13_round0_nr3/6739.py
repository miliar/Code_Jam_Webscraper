#include<stdio.h>
int main()
{
    freopen("C2.in","r",stdin);
    freopen("CC2.txt","w",stdout);
    int n,m,t,i,sum,k=1,a[5]={1,4,9,121,484};
    scanf("%d",&t);
    while(t--)
    {
        sum=0;
        scanf("%d%d",&n,&m);
        for(i=0;i<5;i++)
            if(n<=a[i]&&a[i]<=m)
                sum++;
            printf("Case #%d: %d\n",k++,sum);
    }
}
