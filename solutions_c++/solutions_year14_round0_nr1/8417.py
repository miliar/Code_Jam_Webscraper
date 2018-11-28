#include<stdio.h>
#include<string.h>
int main()
{
    int tc,i,j,k,l,ll,n,item,m;
    int a[17];
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&tc);
    for(i=1;i<=tc;i++)
    {

        m=0;
        scanf("%d",&l);
        for(j=1;j<=4;j++)
        {
            for(k=1;k<=4;k++)
            {
                scanf("%d",&n);
                a[n]=j;
            }
        }
        scanf("%d",&ll);
        for(j=1;j<=4;j++)
        {
            for(k=1;k<=4;k++)
            {
                scanf("%d",&n);
                if(j==ll)
                {
                    if(a[n]==l)
                    {
                        m++;
                        item=n;
                    }
                }
            }
        }
        if(m==1)
            printf("Case #%d: %d\n",i,item);
        else if(m>1)
            printf("Case #%d: Bad magician!\n",i);
        else if(m==0)
            printf("Case #%d: Volunteer cheated!\n",i);
    }
    return 0;

}
