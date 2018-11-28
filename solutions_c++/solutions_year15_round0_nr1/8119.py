#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int l,ans=0,sum=0;
        char s[1024];

        scanf("%d",&l);
        scanf("%s",&s);
        for(int i=0;i<=l;i++)
        {
            if(sum<i)
            {
                ans+=i-sum;
                sum=i;
            }
            sum+=s[i]-'0';

        }
        printf("Case #%d: %d\n",t,ans);
    }
}
