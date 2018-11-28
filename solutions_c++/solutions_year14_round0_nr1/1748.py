#include <stdio.h>
#include <string.h>
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,n,hash[20],k,mark,i,j,set,l=1;
    scanf("%d",&t);
    while(l<=t)
    {
        scanf("%d",&n);
        memset(hash,0,sizeof(hash));
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&k);
                if(i==n)
                hash[k]++;
            }
        }
        scanf("%d",&n);
        for(i=1,mark=0;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&k);
                if(i==n)
                {
                    hash[k]++;
                    if(hash[k]>1)
                    {
                        mark++;set=k;
                    }
                }
            }
        }
        printf("Case #%d: ",l++);
        if(mark==1)
        printf("%d\n",set);
        if(mark==0)
        printf("Volunteer cheated!\n");
        if(mark>1)
        printf("Bad magician!\n");
    }
    return 0;
}
