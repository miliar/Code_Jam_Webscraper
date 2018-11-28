#include<iostream>
#include<string>

using namespace std;

int isC(char a)
{
if(a=='a' || a=='e' || a=='i' || a=='o' || a=='u')
return 0;
else return 1;
}

int main()
{
int t;
cin>>t;

for(int k=1;k<=t;k++)
{

string s;
int n;

cin>>s>>n;

long ans=0;
for(int i=0;i<s.length();i++)
{
int c=0,flag=0;
for(int j=i;j<s.length();j++)
{
//cout<<s.substr(i,j)<<endl;
//cout<<i<<" "<<j<<endl;
//cout<<c<<" "<<flag<<" "<<ans<<endl;
if(isC(s[j]))
{
c++;
if(c>=n) flag=1;
}
else c=0;

if(flag==1)
ans++;

}
}

cout<<"Case #"<<k<<": "<<ans<<endl;

}

}