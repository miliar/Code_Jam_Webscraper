#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

struct node
{
    int num,id;
    bool operator <(const node &b)const
    {
        return num<b.num;
    }
}a[1010];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int n,i,j,x;
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%d",&a[i].num);
            a[i].id=i;
        }
        sort(a+1,a+1+n);
        int l=1,r=n,ans=0;
        for(i=1;i<=n;i++)
        {
            x=a[i].id;
            if(x-l<r-x)
            {
                ans=ans+x-l;
                for(j=i+1;j<=n;j++)
                {
                    if(a[j].id<x)
                        a[j].id++;
                }
                l++;
            }
            else
            {
                ans=ans+r-x;
                for(j=i+1;j<=n;j++)
                {
                    if(a[j].id>x)
                        a[j].id--;
                }
                r--;
            }
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
