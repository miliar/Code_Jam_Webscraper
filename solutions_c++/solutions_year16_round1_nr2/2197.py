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

long long int n,x,y;

int b[2503]={0};
cin>>n;
int a[n];



for(int i=0;i<(2*n)-1;i++)
{
for(int j=0;j<n;j++)
{
cin>>x;
b[x]++;
}
}


y=0;
for(int i=1;i<2503;i++)
{
if(b[i]%2!=0)
{
a[y]=i;
y++;
}
}

sort(a,a+y);

cout<<"Case #"<<k<<":";

for(int i=0;i<n;i++)
cout<<" "<<a[i];

cout<<endl;
}

return 0;
}
