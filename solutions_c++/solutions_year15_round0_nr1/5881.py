#include<iostream>
using namespace std;
int main()
{
freopen("A-large.in","r",stdin);
freopen("out.in","w",stdout);
int t;
cin>>t;
for(int d=1;d<=t;d++)
{
int k;
cin>>k;
string s;
cin>>s;
int total=0;
int left=0;
int g;
for(g=0;g<=k;g++)
{
if((s[g]-48)==0)
total++;
else
break;
}
for(int r=g;r<=k;r++)
{
left+=s[r]-48;
if(left==0)	
total+=1;
else
left-=1;
}
cout<<"Case #"<<d<<": "<<total<<endl;
}

return 0;
}
