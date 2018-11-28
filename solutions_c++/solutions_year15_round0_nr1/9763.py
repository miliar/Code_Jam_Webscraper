#include<iostream>
using namespace std;
int main()
{
int i,x,t,s,f,tot;
string a;
cin>>t;
for(i=0; i<t; i++)
{
f=0;
tot=0;
cin>>s;
cin>>a;
for(x=0; a[x]!='\0'; x++)
{
if(tot<x && a[x]!=48)
{
f=f+(x-tot);
tot=tot+f;
}
tot=tot+(a[x]-48);
}
cout<<"Case #"<<i+1<<": "<<f<<endl;
}
return 0;
}
