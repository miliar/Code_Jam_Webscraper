#include<bits/stdc++.h>
#include<algorithm>
#define ll long long int
using namespace std;
int main()
{
    string s,ans;
    char ch;
    int i,t,j,f,l;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        ans="";
        cin>>s;
        ans=s[0];
        f=s[0]-65;
        l=s[0]-65;
        for(i=1;i<s.length();i++)
        {
            ch=s[i];
            if((int)ch-65>=f)
            {
                ans=ch+ans;
                f=ch-65;
            }
            else
            {
                 ans=ans+ch;
                 l=ch-65;
            }

        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
    return 0;
}
