#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;
int test (int a[])
{
int flag=0,i,k,minima,l;
for(i=9;i>=1;i--)
{
if(a[i]>0){
l=i;
flag=1;
break;
}
}
if(l==1)
return 1;
if(flag==0)
return 0;
minima=l;
for(k=2;k<=(l+1)/2;k++)
{
a[k]+=1;
a[l-k]+=1;
a[l]-=1;
minima = min(minima,1+ test(a));
a[k]-=1;
a[l-k]-=1;
a[l]+=1;
}
return minima;
}

int main()
{
int T,d,i,j,p,m;
cin >> T;
for(i=1;i<=T;i++)
{
int b[10]={0};
cin >> d;
for(j=0;j<d;j++)
{
cin >> p;
b[p]+=1;
}
m=test(b);
cout <<"Case #"<<i<<": "<<m<<"\n";
}
return 0;
}

