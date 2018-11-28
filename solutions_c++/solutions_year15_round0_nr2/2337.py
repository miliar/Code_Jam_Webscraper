#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int p[1005];
int main(void)
{
    int i,j,k;
    int cases,ca;
    int d;
    int sum,ans;
    freopen("B-large.in","r+",stdin);
    freopen("B_out.txt","w+",stdout);
    scanf("%d",&cases);
    for (ca=1;ca<=cases;ca++)
    {
        scanf("%d",&d);
        memset(p,0,sizeof(p));
        for (i=1;i<=d;i++)
            scanf("%d",&p[i]);
        ans=10000007;
        for (i=1;i<=1000;i++)
        {
            sum=0;
            for (j=1;j<=d;j++)
            if (p[j]>i)
                sum+=p[j]/i+(p[j]%i?0:-1);
            if (sum+i<ans)
                ans=sum+i;
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
