#include<cstdio>
#include<cmath>
#include<algorithm>

using namespace std;

int t,n,mn1,mn2,m[1005],mr;

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A_out_large.txt","w",stdout);
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        mr=mn1=mn2=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)    scanf("%d",&m[i]);
        for(int i=1;i<n;i++)
        {
            mr=max(m[i-1]-m[i],mr);
            mn1+=max(0,m[i-1]-m[i]);
        }
        for(int i=0;i<n-1;i++)  mn2+=min(mr,m[i]);
        printf("Case #%d: %d %d\n",z,mn1,mn2);
    }
    return 0;
}
