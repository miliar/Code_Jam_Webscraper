#include<cstdio>
#include<string>
#include<cstring>
using namespace std;


int main()
{
    // freopen("B-large.in","r",stdin);
//  freopen("out.out","w",stdout);

    int T;
    scanf("%d",&T);
    for(int t=0; t<T; t++)
    {
        int maxx=0;
        int ans=99999999;
        int D;
    scanf("%d",&D);
        int an[D];
        for(int i=0; i<D; i++)
        {
           scanf("%d",&an[i]);
            maxx=max(an[i],maxx);
        }
        for(int m=1; m<=maxx; m++)
        {
            int sum=m;
            for(int i = 0 ; i < D ; i++)
            {
                if( an[i] > m )
                {
                    if( an[i]%m == 0 )
                        sum += an[i]/m-1 ;
                    else
                        sum += an[i]/m ;
                }
            }
            ans = min(ans,sum);
        }

        printf("Case #%d: %d\n",t+1,ans);
    }
    return 0;
}
