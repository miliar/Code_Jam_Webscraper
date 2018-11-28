#include<iostream>
#include<string.h>
using namespace std;
int n, k;
string inp;

int check(string part)
{
int i,sl,s=0;
sl=part.length();
//cout<<part;
for(i=0;i<sl;i++)
{
if(part[i]=='a'||part[i]=='e'||part[i]=='i'||part[i]=='o'||part[i]=='u')
s=0;
else
s++;
if(s>=k)
{

//cout<<"exitng";
//cin>>i;
return 1;
}
}
return 0;
}
int main()
{
int t=1, tst;
cin>>tst;
while(t<=tst)
{
cin>>inp>>k;
int i,j,cnt=0,linp=inp.length();
for(i=0;i<linp;i++)
for(j=1;j<=linp-i;j++)
if(check(inp.substr(i,j)))
cnt++;

cout<<"Case #"<<t<<": "<<cnt<<endl;
t++;
}

}
