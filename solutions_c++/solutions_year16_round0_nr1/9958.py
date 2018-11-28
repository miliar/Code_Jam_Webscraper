#include <iostream>

using namespace std;

long int solve(long int n,long int a,int d[10])
{
 long int temp,test=1;
 if(n==0)
  return 0;
 else
 { 
  a=a+n;
  temp = a;
  while(temp>0)
  {
   d[temp%10]=1;
   temp=temp/10;
  }
  for(int i=0;i<10;i++)
  {
   if(d[i]==0)
   { 
    test=0;
    break;
   }
  }
  if(test==1)
   return a;
  else
   solve(n,a,d);
 }
}
 

int main()
{
 long int t,n,a;
 int d[10];
 cin>>t;
 for(int i=1;i<=t;i++)
 {
  for(int j=0;j<10;j++)
   d[j]=0;
  cin>>n;
  a=solve(n,0,d);
  if(a!=0)
   cout<<"Case #"<<i<<": "<<a<<"\n";
  else
   cout<<"Case #"<<i<<": INSOMNIA\n";
 }
 return 0;
}

