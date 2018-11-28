#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int casenum;
int n;
int a[1005];
int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&casenum);
    for(int k=1;k<=casenum;k++)
    {
        memset(a,0,sizeof(a));
        char x[1005];
        scanf("%d %s",&n,x);
        int length=strlen(x);
        for(int i=0;i<length;i++)
        {
            a[i]=x[i]-'0';
        }
        int n=a[0];
        int ans=0;
        for(int i=1;i<length;i++)
        {
            if(i<=n)
            {
                n=n+a[i];
            }
            else
            {
                a[i]=a[i]+i-n;
                ans=ans+i-n;
                n=n+a[i];
            }
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
