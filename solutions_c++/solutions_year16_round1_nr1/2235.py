#include <iostream>
#include <omp.h>
#include <string.h>
#include <bits/stdc++.h>
using namespace std;

int main() 
{

long long int t;
cin >>t;

for(int k=1;k<=t;k++)
{
string s,s1,s2;
cin>>s;
s1=s[0];
for(int i=1;i<s.length();i++)
{

if(s1[0]>s[i])
{
s1+=s[i];
}
else
{
s2=s[i];
s2+=s1;
s1=s2;
}

}
cout<<"CASE #"<<k<<": "<<s1<<endl;

}

return 0;
}
