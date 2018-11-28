#include<iostream>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{

freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
int test,r1,r2,a[4][4],b[4][4],e[4],i,j,k,l,ans,c;
int *p;
std::cin>>test;
for(i=1;i<=test;i++)
{
ans=0;
cin>>r1;
for(j=0;j<=3;j++)
{
for(k=0;k<=3;k++)
{
cin>>a[j][k];
if(j==r1-1)
e[k]=a[j][k];
}
}
cin>>r2;
for(j=0;j<=3;j++)
{
for(k=0;k<=3;k++)
{
cin>>b[j][k];
if(j==r2-1)
{
p=find(e,e+4,b[j][k]);
//cout<<p-e<<endl;
if((p-e)>=0 && (p-e)<=3)
{
ans++;
if(ans==1)
c=p-e;
}

}
}
}
if(ans==0)
cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
else if(ans==1)
cout<<"Case #"<<i<<": "<<e[c]<<endl;
else
cout<<"Case #"<<i<<": Bad magician!"<<endl;

}
return 0;
}
