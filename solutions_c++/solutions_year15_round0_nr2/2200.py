#include<stdio.h>
int main()
{
    int task,maxtask,n,maxa,i,j,a[1100],ans,total;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&maxtask);
    for(task=1;task<=maxtask;task++)
    {
        scanf("%d",&n);
        maxa=0;
        for(i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            if(a[i]>maxa)
                maxa=a[i];
        }
        ans=maxa;
        
        for(j=1;j<=maxa;j++)
        {
            total=0;
            for(i=1;i<=n;i++)
            {
                total+=a[i]/j;
                if(a[i]%j==0)
                    total--;
            }
            total+=j;
            if(total<ans)
                ans=total;
        }
        printf("Case #%d: %d\n",task,ans);
    }
    fclose(stdout);
    return 0;
}
