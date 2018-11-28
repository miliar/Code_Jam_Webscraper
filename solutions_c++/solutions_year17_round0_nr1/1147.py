#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        string s;
        int i,n,k,flag=0,ans=0;
        cin>>s>>k;
        n=s.size();
        for(i=0;i<=n-k;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else s[j]='-';
                }
            }
        }
        for(i=n-k;i<n;i++)
        {
            if(s[i]=='-')
                flag=1;
        }
        if(flag==1)
            cout<<"Case #"<<tt<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<tt<<": "<<ans<<"\n";
    }
    return 0;
}
