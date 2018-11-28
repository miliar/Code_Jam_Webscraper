/* itoa example */
#include<iostream>
#include <cstdio>
#include <cstdlib>
#include<string>
#include<cmath>
#define ll unsigned long long int
using namespace std;

int palin(char s[])
{
 int len=strlen(s);
 for(int i=0,j=len-1;i<len/2;i++,j--)
 {
  if(s[i]!=s[j])
  return 0;
 }
 return 1;
}


int main ()
{
  ll t,a,b,check,no=1;
  double result;
  
  char s[100];
  cin>>t;
  while(t--)
  {
   cin>>a>>b;
   int ispalin=0;
   ll count=0;
   for(ll i=a;i<=b;i++)
   {
    itoa(i,s,10);
    ispalin=palin(s);
    if(ispalin==1)
    {
     //cout<<i<<"\n";
     result=sqrt(i);
     check=result;
     if(check*check==i)
     {
      itoa(check,s,10);
      if(palin(s))
      count++;
     }
    }
   }
   cout<<"Case #"<<no<<": "<<count<<"\n";
   no++;
  }
  //cin>>t;
}
