#include <iostream>
#include <bits/stdc++.h>
#include <string.h>
using namespace std;


int main() 
{


long long int x,y,t,flag;

cin>>t;

string s;



int a[11];


for(int l=1;l<=t;l++)
{

for(int i=0;i<10;i++)
a[i]=1;

cin>>x;
if(x==0)
{
cout<<"Case #"<<l<<": "<<"INSOMNIA"<<endl;
continue;
}


for(int i=1;;i++)
{
y=x*i;
stringstream r;
r<<y;
s=r.str();


for(int j=0;j<s.length();j++)
a[int(s[j]-'0')]=0;

flag=3;

for(int k=0;k<10;k++)
{

if(a[k]!=0)
{
flag=0;
break;
}
}

if(flag==3)
{
cout<<"Case #"<<l<<": "<<y<<endl;
break;
}
}


}
    return 0;
}
