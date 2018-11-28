#include<cstdio>
#include<cstring>
using namespace std;
char s[1005];
int main()
{
//    freopen("A.in","r",stdin);
//    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    int ks=0;
    while(T--)
    {
        int n;
        scanf("%d",&n);
        scanf("%s",s);
        int sum=0;
        int ans=0;
        for(int i=0;i<=n;i++)
        {
            if(sum<i)
            {
                ans+=i-sum;
                sum=i;
            }
            sum+=s[i]-48;
        }
        printf("Case #%d: %d\n",++ks,ans);
    }
    return 0;
}
