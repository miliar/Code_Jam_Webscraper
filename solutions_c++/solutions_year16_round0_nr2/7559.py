#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
int t;
cin>>t;
for(int j=1;j<=t;j++)
{
string s;
cin>>s;
int co=0;
if(s.length()==1)
{
if(s[0]=='+')
cout<<"Case #"<<j<<": 0"<<endl;
else
cout<<"Case #"<<j<<": 1"<<endl;
}
else
{
for(int i=s.length()-1;i>=0;i--)
{
if(s[i]=='-')
{
if(s[i-1]=='+')
co=co+2;
else if(s[i-1]=='-')
continue;
else
co++;
}
}
cout<<"Case #"<<j<<": "<<co<<endl;
}
}
return 0;
}
