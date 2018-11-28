#include<iostream>
using namespace std;
int main()
{
int i,j,t,s,fr,to;
string a;
cin>>t;
for(i=0; i<t; i++)
{
fr=0;
to=0;
cin>>s;
cin>>a;
for(j=0; a[j]!='\0'; j++)
{
if(to<j && a[j]!=48)
{
fr=fr+(j-to);
to=to+fr;
}
to=to+(a[j]-48);
}
cout<<"Case #"<<i+1<<": "<<fr<<endl;
}
return 0;
}
