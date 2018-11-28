#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        string s;
        int ans=0;
        cin>>s;
        int l=s.length();
        for(int j=1;j<l;j++)
        {
            if(s[j]!=s[j-1])
                ans++;
        }
        if(s[l-1]=='-')
            ans++;
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
