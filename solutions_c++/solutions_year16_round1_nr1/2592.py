#include<bits/stdc++.h>
using namespace std;
int main()
{
    string str,ans;
    int n;
    int t0=1;
    cin>>n;
    while(n--)
    {
        ans="";
        cin>>str;
        ans=str[0];
        for(int i=1;i<str.length();i++)
        {
            if(str[i]>=ans[0])
                ans=str[i]+ans;
            else
                ans=ans+str[i];
        }
        cout<<"Case #"<<t0++<<": "<<ans<<endl;
    }
}