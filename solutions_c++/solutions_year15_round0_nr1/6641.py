#include<stdio.h>
int main()
{
    int t,n,i,k,count,j;
    char a[1010];
    scanf("%d",&t);
    for(j=1;j<=t;++j)
    {
        scanf("%d%s",&n,a);
        count=a[0]-'0';
        k=0;
        for(i=1;i<=n;++i)
        {
            if(i>count)  {k+=(i-count);count=i;}
            count+=a[i]-'0';
        }
        printf("Case #%d: %d\n",j,k);
    }
    return 0;
}
