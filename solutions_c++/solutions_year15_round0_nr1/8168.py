#include<cstdio>
#include<vector>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<map>
#include<stack>
using namespace std;
int num[1100];
char str[1100];
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d %s",&n,str);
        for(int i=0;i<=n;i++)
            num[i]=str[i]-'0';
        int ans=0;
        int sum=0;
        for(int i=0;i<=n;i++)
        {
            if(!num[i])
                continue;
            if(sum<i)
            {
                ans+=i-sum;
                sum=i;
            }
            sum+=num[i];
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
    return 0;
}
