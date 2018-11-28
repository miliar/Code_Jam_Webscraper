#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,i,cur,ans,l;
    char a[1001];
    scanf("%d",&t);
    l=1;
    while(l<=t)
    {
        scanf("%d",&n);
        scanf("%s",a);
       // printf("%s",a);
        ans=0;cur=0;
        for(i=0;i<=n;i++)
        {
            if(cur < i && (a[i]-'0') > 0)
            {
                ans=ans+i-cur;
                cur=i+a[i]-'0';
            }
            else
                cur+=a[i]-'0';
           // cout << cur << " " << ans << endl;
        }
        printf("Case #%d: %d\n",l,ans);
        l++;
    }
    return 0;
}
