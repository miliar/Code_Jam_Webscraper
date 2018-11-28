#include<stdio.h>
#include<algorithm>
#include<utility>
#include<vector>
#include<string.h>
using namespace std;
long long a,b,c,d,e,f,g,h,i,n,m,ans,tot;
long long zz[1005],zz2[1005];
vector<pair<long long,long long> > v;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%I64d",&a);
    for (b=1;b<=a;b++)
    {
        memset(zz,0,sizeof(zz));
        memset(zz2,0,sizeof(zz2));
        tot=0;
        scanf("%I64d %I64d",&n,&m);
        for (f=1;f<=m;f++)
        {
            scanf("%I64d %I64d %I64d",&c,&d,&e);
            tot+=(d-c)*(d-c-1)/2*e;
            for (g=c+1;g<=d;g++)
                zz[g]+=e;
            zz2[c]+=e;
        }
        g=0;
        ans=0;
        for (f=1;f<=100;f++)
        {
            //if (zz2[f]>0) printf("%I64d\n",f);
            while(zz2[f]>0)
            {
                g=f;
                zz2[g]--;
                while(zz[g+1]>0)
                {
                    g++;
                    zz[g]--;
                }
                //printf("%I64d %I64d\n",g,f);
                ans+=(g-f)*(g-f-1)/2;
            }
        }
        printf("Case #%I64d: %I64d\n",b,(ans-tot)%1000002013);
    }
    return 0;
}
