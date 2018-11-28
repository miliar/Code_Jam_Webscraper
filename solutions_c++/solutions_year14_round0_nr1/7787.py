#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
 //   freopen("A-small-attempt0.in","r",stdin);
   // freopen("out.txt","w",stdout);
    int c[16],d[16];
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int a,b;
        cin>>a;
        int i;
        for(i=0;i<16;i++)
            cin>>c[i];
        cin>>b;
        for(i=0;i<16;i++)
            cin>>d[i];
        int e[4],f[4];
        int j;
        for(i=4*(a-1),j=0;i<4*a;i++)
            e[j++]=c[i];
        for(i=4*(b-1),j=0;i<4*b;i++)
            f[j++]=d[i];
        int ans=-1,flag=0;
        int aa=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(e[i]==f[j])
                {
                    flag=true;
                    ans=e[i];
                    aa++;
                }
            }
        }

        if(aa==0)
            printf("Case #%d: Volunteer cheated!\n",cas);
        else if(aa==1)
            printf("Case #%d: %d\n",cas,ans);
        else printf("Case #%d: Bad magician!\n",cas);
        cas++;
    }
    return 0;
}
