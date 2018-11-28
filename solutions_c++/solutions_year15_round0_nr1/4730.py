#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn=1010;
char str[maxn];
int main()
{
    int T,cas=1;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d%s",&n,str);
        int curSum=0,ans=0;
        for(int i=0;i<=n;i++)
        {
            if(str[i]=='0') continue;
            if(curSum<i)
            {
                ans+=i-curSum;
                curSum=i;
            }
            curSum+=str[i]-'0';
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
