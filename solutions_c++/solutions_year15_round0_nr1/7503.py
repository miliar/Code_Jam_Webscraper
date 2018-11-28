#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
int test=0;
ifstream input;
input.open("A-large.in");
freopen("large.out","w",stdout);
if(input.is_open())
{
string tst;
input>>tst;
for(int i=0;i<tst.length();i++)
		test=(test*10+tst[i]-'0');
for(int i=1;i<=test;i++)
{
string ipt1,arr;
input>>ipt1>>arr;
int smax=0;
for(int k=0;k<ipt1.size();k++)
{
smax=smax*10+ipt1[k]-'0';
}
if(smax==0)
{
cout<<"Case #"<<i<<": "<<"0"<<endl;
}
else
{
int clapped=0;
int add=0;
for(int j=1;j<=smax;j++)
{
clapped+=(arr[j-1]-'0');
if(arr[j]-'0'>0 && clapped<j)
{
add=add+(j-clapped);
clapped=j;
}
}
cout<<"Case #"<<i<<": "<<add<<endl;
}
}
}
return 0;
}
