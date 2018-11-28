#include <iostream>
//#include <stdlib.h>
#include <assert.h>

using namespace std;

int main(){
int t=1,s=0,f=0,r=1;
cin>>t;
assert(t>=1 && t<=100);
while(t!=0)
{
t--;
f=0;
cin>>s;
assert(s>=0 && s<=6);
char ch[s];
for(int i=0;i<s+1;i++)
{
cin>>ch[i];
}
int c;
int u=1;
while(u==1)
{u=0;c=ch[0]-48;
for(int i=0;i<s+1;i++)
{
//cout<<i<<"\t"<<ch[i]-48<<"\t";
if (ch[i]-48 == 0 || i==0)
{//cout<<"\n";
continue;}
  else
  {
if (c>=i)
{//cout<<c<<" Y\n";
c=c+(ch[i]-48);}
  else
  {
//cout<<c<<" N short by: "<<i-c<<"\n";
f=f+(i-c);
ch[0]=ch[0]+i-c;u=1;//cout<<"\n";
break;
  }
  }
}
}
cout<<"Case #"<<r<<": " <<f<<"\n";r++;
}
return 0;
}
