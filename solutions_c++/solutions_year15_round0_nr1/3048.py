#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    char s[2000];
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        scanf("%s",s);
        int sum = s[0]-'0';
        int ans=0;
        for(int i=1;i<=n;i++)
        {
            int now = i;
            if (sum >= i)
                sum += s[i]-'0';
            else
               {
                ans+= i-sum;
                sum+=i-sum;
                sum+=s[i]-'0';
               }
        }
        printf ("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
