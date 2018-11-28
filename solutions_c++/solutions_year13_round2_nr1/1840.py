#include <cstdio>
#include <algorithm>
using namespace std;
#define MAXN 133
#define inf 1000000000
int mo[MAXN];
int main()
{
    int cas_num,cas;
    int ans;
    int tmp;
    int a;
    int i,j;
    int n;
    int cnt;
    int cc0;
    int skp;
    double t2;
    int t1,t3;

    scanf("%d",&cas_num);
    //printf("%d\n",cas_num);
    cas=1;
    while(cas_num--)
    {
        scanf("%d%d",&a,&n);
        //printf("%d %d\n",a,n);
        cc0=0;
        for(i=0;i<n;i++)scanf("%d",&mo[i]);
        mo[n++]=inf;
        for(i=0;i<n;i++)if(mo[i]==0)cc0++;
        if(a==1)
        {
            printf("Case #%d: %d\n",cas++,n-cc0-1);
            continue;
        }
        sort(mo,mo+n);
        /*
        for(i=0;i<n-1;i++)
            printf("%d ",mo[i]);
        puts("");
        /**/
        cnt=0;
        ans=n;
        tmp=a;
        for(i=0;i<n;i++)
        {

            if(cnt+n-i<ans)
                ans=cnt+n-i;
            if(i==n-1)continue;
            if(mo[i]<tmp)
            {
               tmp+=mo[i];
               continue;
            }
            else
            {
               t1=0;
               t3=tmp;
               while(t3<=mo[i])
               {
                   t3+=(t3-1);
                   t1++;
               }
               cnt+=t1;
               tmp=t3;
               tmp+=mo[i];
            }
        }
        if(a==1)
        {
            printf("Case #%d: %d\n",cas++,n-cc0-1);
        }
        else
        {
            printf("Case #%d: %d\n",cas++,ans-1);
        }
    }
    return 0;
}
