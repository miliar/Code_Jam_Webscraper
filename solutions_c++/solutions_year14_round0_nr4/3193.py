#include<cstdio>
#include<algorithm>
#define maxn 1005
using namespace std;

double no1[maxn],no2[maxn];

int main()
{
    int t,n;
    int ca=1;
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(int i=0; i<n; i++)
            scanf("%lf",&no1[i]);
        for(int i=0; i<n; i++)
            scanf("%lf",&no2[i]);
        sort(no1,no1+n);
        sort(no2,no2+n);
        int tmp1=0,tmp2=n-1;
        int ans1=0,ans2=0;
        for(int i=n-1; i>=0; i--)
        {
            if(no1[tmp2]>no2[i])
            {
                ans1++;
                tmp2--;
            }
            else tmp1++;
        }
        tmp1=0,tmp2=n-1;
        for(int i=n-1; i>=0; i--)
        {
            if(no2[tmp2]>no1[i])
            {
                ans2++;
                tmp2--;
            }
            else tmp1++;
        }

        printf("Case #%d: %d %d\n",ca++,ans1,n-ans2);
    }
    return 0;
}
