#include<iostream>
#include<stdio.h>
#include<math.h>

using namespace std;
#define ll long long int
int main()
{
ll t,i;
int fl;
scanf("%lld",&t);
string a,b,c,d;
for(i=1;i<=t;i++)
{
  a="";
  cin>>b;
int l=b.length();
for(int j=0;j<l;j++)
{
  c=b[j]+a;
  d=a+b[j];
  if(c>d)
  a=c;
  else
  a=d;
}

printf("Case #%lld: ",i);
cout<<a;



if(i!=t)
  printf("\n");
}

  return 0;
}
