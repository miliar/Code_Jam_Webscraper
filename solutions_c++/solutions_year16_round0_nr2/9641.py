#include <iostream>
#include <bits/stdc++.h>
#include <string.h>
using namespace std;


int main() 
{

string s,s1;

long long int res=3,p,q,x=0,f,t;

cin>>t;


for(int l=1;l<=t;l++)
{

cin>>s;
s1=s;

q=s.length();

for(int k=1;;k++)
{

p=0;
while(s[p++]=='+')
{
}
p=p-2;

if(p==s.length()-1)
{
x=k-1;
break;// all bits +
}




if(p>=0)
{
for(int i=0;i<=p;i++)
s[i]='-';
}
else
{
q--;
while(s[q]=='+')
{
q--;
}
q=q+1;


{
s1=s;

for(int i=0;i<q;i++)
{
s1[i]=s[q-1-i];
if(s1[i]=='+')
s1[i]='-';
else
s1[i]='+';
}

s=s1;


}


}

f=3;
for(int i=0;i<s.length();i++)
{
if(s[i]!='+')
{f=0;
break;
}
}

}

cout<<"Case #"<<l<<": "<<x<<endl;


}
    return 0;
}
