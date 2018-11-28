/*
    shubham_1286
   algo =             */
using namespace std;
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<sstream>
#include<algorithm>
#include<list>
#include<deque>
#include<bitset>
#include<limits>
#include<sstream>
#define max(x,y) x>y?x:y
#define min(x,y) x<y?x:y
#define inf INT_MAX
#define low INT_MIN
#define mod 1000000007
int main()
{
int t,test;
scanf("%d",&t);
test=1;
while(test<=t)
{
int n,m,flag,moun=0,coun=0;
scanf("%d%d",&n,&m);
int arr[n+1][m+1],c;
for(int i=0;i<n;i++)
{for(int j=0;j<m;j++)
scanf("%d",&arr[i][j]);}

for(int i=0;i<n;i++)
{
for(int j=0;j<m;j++)
{
flag=10;moun=0;coun=0;
if(arr[i][j]==1)
{
for(int k=0;k<m;k++)
{
if(arr[i][k]==1)
coun++;
}
//cout<<"coun   "<<coun<<endl;
for(int l=0;l<n;l++)
{
if(arr[l][j]==1)
moun++;
}
//cout<<"moun   "<<moun<<endl;
if((coun==m || moun==n))
{}
else
{
flag=0;
break;}
}}
if(flag==0)
break;
}
if(flag==10)
printf("Case #%d: YES\n",test);
else
printf("Case #%d: NO\n",test);
test++;
}

}
