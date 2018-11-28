#include<iostream>
#include<bits/stdc++.h> 
#include<fstream>
#include<set>
#include<map>
#define up(j,n,i) for(i=j;i<n;i++)
using namespace std;
typedef long long int lld;
vector < lld > convert(lld a)
{
vector < lld > b;
while(a>0)
{
b.push_back(a%10);
a=a/10;
}
return b;
}
int main()
{
lld t,k=0;
fstream I,O;
I.open("in.in",ios::in);
O.open("out.txt",ios::out);
I>>t;
k=1;
while(k<=t)
{
vector <lld> v;
lld n,i=0,j=0,l=0;
I>>n;
set <lld> s;
//cout<<t1<<endl;
up(0,10,i)
s.insert(i);
i=1;
if(n!=0)
{
while(s.size())
{
v=convert(n*i);
j=0;
while(j<v.size()&&s.size())
{
if(s.find(v[j])!=s.end())
{s.erase(s.find(v[j]));}
j++;
}
if(s.size()==0)
{l=n*i;}
i++;
}
}
O<<"Case #"<<k<<": ";
if(n!=0)
O<<l<<endl;
else
O<<"INSOMNIA"<<endl;
k++;
}
return 0;
}
