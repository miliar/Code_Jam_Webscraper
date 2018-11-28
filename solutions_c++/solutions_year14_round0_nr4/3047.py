#include<algorithm>
#include<iostream>
#include<string.h>
#include<sstream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
using namespace std;
const int INF=0x3f3f3f3f;
const double eps=1e-8;
const int maxn=100010;
double sa[1010],sb[1010];

int main()
{
    int t,cas=1,n,i,j,p,lb,ans1,ans2;

    freopen("D-large.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf",&sa[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&sb[i]);
        sort(sa,sa+n);
        sort(sb,sb+n);
        lb=0;
        ans1=ans2=0;
        for(i=0;i<n;i++)
            if(sa[i]>sb[lb])
                ans1++,lb++;
        for(i=n-1;i>=0;i--)
        {
            p=-1;
            for(j=0;j<n;j++)
            {
                if(sb[j]>eps)
                {
                    if(p==-1)
                        p=j;
                    if(sb[j]>sa[i])
                    {
                        sb[j]=0;
                        p=-1;
                        break;
                    }
                }
            }
            if(p!=-1)
                sb[p]=0,ans2++;
        }
        printf("Case #%d: %d %d\n",cas++,ans1,ans2);
    }
    return 0;
}
