#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,c=0;
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        int n,i;string s;
        cin>>n>>s;
        int available=s[0]-48,ans=0;
        for(i=1;i<=n;i++)
        {
        if(available<i)
        {
        ans+=(i-available);
        available+=(s[i]-48+i-available);
        }
        else
        available+=(s[i]-48);
        }
        c++;
        cout<<"Case #"<<c<<": "<<ans<<endl;
    }
    return 0;
}

