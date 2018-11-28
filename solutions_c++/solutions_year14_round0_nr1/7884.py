#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<iostream>
#include <utility>
#define PI 3.14159265359
using namespace std;
typedef long long LL;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int n,m,i,j,t,v[20];
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        memset(v,0,sizeof(v));
        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                int x;
                scanf("%d",&x);
                if(i==n)
                {
                    v[x]=1;
                }
            }
        }
        scanf("%d",&n);
        int num=0,ans;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                int x;
                scanf("%d",&x);
                if(i==n)
                {
                    if(v[x])
                    {
                        num++;
                        ans=x;
                    }
                }
            }
        }
        if(!num)printf("Case #%d: Volunteer cheated!\n",ca);
        else if(num>1)printf("Case #%d: Bad magician!\n",ca);
        else
        {
            printf("Case #%d: %d\n",ca,ans);
        }
    }
}
