#include<stdio.h>
#include<algorithm>
using namespace std;
main()
{
    int i,j,k,ti,te,n,mark,ans1,ans2;
    double nao[1333],ken[1333];

    freopen("D-large.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d",&te);
    for(ti=1;ti<=te;ti++)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%lf",&nao[i]);
        }
        for(i=1;i<=n;i++)
        {
            scanf("%lf",&ken[i]);
        }
        sort(nao+1,nao+n+1);
        sort(ken+1,ken+n+1);
        //printf("yesss\n");
        mark=n;
        ans1=0;
        for(i=n;i>=1;i--)
        {
            for(j=mark;j>=1;j--)
            {
                if(nao[i]>ken[j])
                {
                    ans1++;
                    mark=j-1;
                    break;
                }
            }
        }
        mark=n;
        ans2=0;
        for(i=n;i>=1;i--)
        {
            for(j=mark;j>=1;j--)
            {
                if(ken[i]>nao[j])
                {
                    ans2++;
                    mark=j-1;
                    break;
                }
            }
        }
        //printf("yesss");
        /*
        for(i=1;i<=n;i++)
        {
            printf("%.3lf ",nao[i]);
        }
        printf("\n\n");
        for(i=1;i<=n;i++)
        {
            printf("%.3lf ",ken[i]);
        }
        */
        printf("Case #%d: %d %d\n",ti,ans1,n-ans2);
    }
}
