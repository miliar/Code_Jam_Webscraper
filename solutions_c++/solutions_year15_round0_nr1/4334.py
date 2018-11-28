#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int c=1,t,i,d,ans,a[100001],j,n;
    char s[100001];
    scanf("%d",&t);
    while(t--)
    {
        cin>>n>>s;
        ans=0;
        for(i=0;i<=n;i++)
            a[i]=s[i]-48;
        d=a[0];
        for(i=1;i<=n;i++)
        {
            if(d>=i)
                d=d+a[i];
            else
            {
                ans=ans+(i-d);
                d=i+a[i];
            }
        }
        printf("Case #%d: %d\n",c,ans);
        c++;
    }
    return 0;
}
