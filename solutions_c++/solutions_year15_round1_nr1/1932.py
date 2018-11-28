#include <iostream>

using namespace std;

int main()
{
 int t;
 long long int n,m[1000],temp,m1,m2;
 cin>>t;
 for(int k=1;k<=t;k++)
 {
  cin>>n;
  for(int i=0;i<n;i++)
  {
   cin>>m[i];
  }
  temp=m[0];
  m1=0;
  for(int i=0;i<n;i++)
  {
   if(m[i]<temp)
   {
    m1+=temp-m[i];
   }
   temp=m[i];
  }
  temp=m[0]-m[1];
  m2=0;
  for(int i=1;i<n-1;i++)
  {
   if((m[i]-m[i+1]) > temp)
   {
    temp=m[i]-m[i+1];
   }
  }
  if(temp>0)
  {
   for(int i=0;i<n-1;i++)
   {
    if(m[i]<temp)
     m2+=m[i];
    else
     m2+=temp;
   }
  }
  cout<<"Case #"<<k<<": "<<m1<<" "<<m2<<"\n";
 }
 return 0;
}
  
