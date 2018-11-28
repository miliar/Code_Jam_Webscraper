#include <stdio.h>
#include <string.h>

int cnt[18],ans;

void process()
{
    int i,j,k,p;

    scanf("%d",&k);

    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            scanf("%d",&p);

            if(i==k)
            {
                cnt[p]++;

                if(cnt[p]==2)
                {
                    if(ans==0) ans=p;

                    else ans=20;
                }
            }
        }
    }
}

int main()
{
    int i,j,k,t,T;

    freopen("A-small-attempt0(4).in","r",stdin);
    freopen("a.txt","w",stdout);

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        ans=0;
        memset(cnt,0,sizeof(cnt));
        process();
        process();

        printf("Case #%d: ",t);



        if(ans && ans!=20) printf("%d\n",ans);

        else printf("%s\n",ans ? "Bad magician!" : "Volunteer cheated!");
    }

    return 0;
}
