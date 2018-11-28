#include <iostream>
#include <cstdio>
using namespace std;
int ans[20];
int m[5][5];

int main()
{
    freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
    int T,n;
    scanf("%d",&T);
    for(int cs=1;cs<=T;cs++)
    {
        for(int t=0;t<20;t++)
        ans[t]=0;
        int n;
        scanf("%d",&n);
        for(int t=0;t<4;t++)
        for(int tt=0;tt<4;tt++)
        scanf("%d",&m[t][tt]);
        for(int t=0;t<4;t++)
        ans[m[n-1][t]]++;



        scanf("%d",&n);
        for(int t=0;t<4;t++)
        for(int tt=0;tt<4;tt++)
        scanf("%d",&m[t][tt]);



        for(int t=0;t<4;t++)
        ans[m[n-1][t]]++;
        int d=0;int ret;
        for(int t=0;t<20;t++)
        {
            if(ans[t]==2)
            {
                d++ ;ret=t;
            }
        }

        if(d==0)printf("Case #%d: Volunteer cheated!\n",cs);
        else if(d!=1)printf("Case #%d: Bad magician!\n",cs);
        else printf("Case #%d: %d\n",cs,ret);
    }
    return 0;
}
