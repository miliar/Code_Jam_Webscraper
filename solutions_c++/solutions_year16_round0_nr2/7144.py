#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
int t,i;
string s;
cin>>t;
for(int x=1;x<=t;x++)
{
    bool onlyemp=true,onlyhappy=true;
    long long int ans=0;
    cin>>s;
    for(i=0;i<s.length();i++)
    {
        if(s[i]=='+')
            onlyemp=false;
        else if(s[i]=='-')
         onlyhappy=false;
            if(s[i]!=s[i+1])
            {
               ans++;
            }
    }
    if(onlyhappy)
        cout<<"Case #"<<x<<": "<<0<<"\n";
        else if(onlyemp)
        {
           cout<<"Case #"<<x<<": "<<1<<"\n";
        }
    else
        {
if(s[s.length()-1]=='+' && !onlyhappy)
     ans--;
cout<<"Case #"<<x<<": "<<ans<<"\n";
    }

}
return 0;
}
