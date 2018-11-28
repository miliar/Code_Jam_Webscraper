#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;
bool palin(long long int x)
{
  int catalyst = 1,div=1;
  while(x/div>=10)
   {
    div*=10;
   }
  while(x!=0)
   {
    int l=x/div;
    int r=x%10;
    if(l!=r) return false;
    x=(x%div)/10;
    div/=100;
   }
  return true;
}
vector<long long int> a(10000003,0);
int main()
{
  ifstream fin("test.in");
  ofstream fout("test3.out");
  int t,i,flag=0,k=0;
  for(i=1;i<=10000000;i++)
  {
      if(palin((long long)i))
         if(palin(i*i))
            a[i]=1;

  }
  fin>>t;
  for(k=1;k<=t;k++)
{

  int n,m=0;
  fin>>n>>m;
  if(sqrt(n)*sqrt(n)==n)
  n=sqrt(n)-1;
  else
  n=sqrt(n);
  m=sqrt(m);
  for(i=n+1;i<=m;i++)
  {
      if(a[i]==1)
      flag++;
  }

//cout<<flag<<endl;
fout<<"Case #"<<k<<": "<<flag<<endl;
flag=0;

}

}
