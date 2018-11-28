#include<algorithm>
#include<iostream>
#include<string.h>
#include<sstream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<set>
#include<map>
//#pragma comment(linker,"/STACK:1024000000,1024000000")
using namespace std;
const int INF=0x3f3f3f3f;
const double eps=1e-8;
const double PI=acos(-1.0);
const int maxn=100010;
//typedef __int64 ll;
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
//        printf("------------------------------\n");
//        for(i=0;i<n;i++)
//            printf("%.3lf ",sa[i]);
//        printf("\n");
//        for(i=0;i<n;i++)
//            printf("%.3lf ",sb[i]);
//        printf("\n");
    }
    return 0;
}
/*
10
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458
*/
