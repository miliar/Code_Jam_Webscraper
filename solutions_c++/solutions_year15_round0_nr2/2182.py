#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int d[100010];
int test(int mid,int n)
{
    int ans=0;
    /*if(mid==0)
    {
        return n;
    }*/
    for(int i=0; i<n; i++)
    {
        int temp=d[i];
        while(temp>mid)
        {
            temp-=mid;
            ans++;
        }
    }
    return ans;
}
int main()
{
    int n,t,cases,maxx,maxi,day,tot;
    //freopen("B-small-attempt4.in","r",stdin);
    while(scanf("%d",&t)!=EOF)
    {
        cases=0;
        while(t--)
        {
            maxx=0;
            day=0;
            maxi=0;
            cases++;
            scanf("%d",&n);
            tot=n;
            for(int i=0; i<n; i++)
            {
                scanf("%d",&d[i]);
                if(d[i]>maxx)
                {
                    maxx=d[i];
                }
            }
            int mid=maxx/2;
            int ans=maxx;
            int l=1,r=maxx;
            if(maxx==1)
            {
                printf("Case #%d: 1\n",cases);
                continue;
            }
            for(mid=maxx; mid>0; mid--)
            {
                int temp=test(mid,n);
                //printf("%d %d\n",temp,mid);
                //ans=temp+mid;
                if(ans>temp+mid)
                {
                    ans=temp+mid;
                }
                //printf("%d\n",ans);
            }
            printf("Case #%d: %d\n",cases,ans);
        }
    }
    return 0;
}
