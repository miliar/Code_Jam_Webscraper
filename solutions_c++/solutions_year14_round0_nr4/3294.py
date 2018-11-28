#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
double m1[2000],m2[2000];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int cas=1;
    while(T--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)scanf("%lf",m1+i);
        for(int i=0;i<n;i++)scanf("%lf",m2+i);
        sort(m1,m1+n);
        sort(m2,m2+n);
        int ans1=0,ans2=0;
        int j=n;
        for(int i=n-1;i>=0&&j>=0;i--)
        {
            j=lower_bound(m1,m1+j,m2[i])-m1;
            j--;
            if(j>=0)ans1++;
        }
        j=n;
        for(int i=n-1;i>=0&&j>=0;i--)
        {
            j=lower_bound(m2,m2+j,m1[i])-m2;
            j--;
            if(j>=0)ans2++;
        }
        printf("Case #%d: ",cas++);
        printf("%d %d\n",ans2,n-ans1);
    }
}
