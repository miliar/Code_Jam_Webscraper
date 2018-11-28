#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

int t,n;
char s[1010];

int main()
{
#ifdef Haha
    freopen("A-large.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
#endif // Haha
    scanf("%d",&t);
    for(int cas=1; cas<=t; cas++)
    {
        scanf("%d",&n);
        scanf("%s",s);
        int ans=0;
        int now=0;
        for(int i=0; i<=n; i++)
        {
            int p=s[i]-'0';
            if(now<i)
            {
                ans+=i-now;
                now=i;
            }
            now+=p;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
