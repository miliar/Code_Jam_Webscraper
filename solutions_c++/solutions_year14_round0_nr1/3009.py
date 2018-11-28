#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
main()
{
    int te,ti;
    int n;
    int i,j,k;
    int a[33][33],ch[33],ans;

    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d",&te);
    for(ti=1;ti<=te;ti++)
    {
        memset(ch,0,sizeof(ch));

        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        for(i=1;i<=4;i++)
        {
            ch[a[n][i]]++;
        }

        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        for(i=1;i<=4;i++)
        {
            ch[a[n][i]]++;
        }

        ans=-2;
        for(i=1;i<=16;i++)
        {
            if(ch[i]==2)
            {
                //printf("[%d]\n",i);
                if(ans==-2)
                {
                    ans=i;
                }
                else
                {
                    ans=-1;
                }
            }
        }
        printf("Case #%d: ",ti);
        if(ans==-2)printf("Volunteer cheated!");
        else if(ans==-1)printf("Bad magician!");
        else printf("%d",ans);
        printf("\n");
    }
}
