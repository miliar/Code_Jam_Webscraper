/* itoa example */
#include<iostream>
#include <cstdio>
#include <cstdlib>
#include<string>
#include<cmath>
#define ll unsigned long long int
using namespace std;

ll ab[100000000];

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


void precalculate()
{
 char s[100];
 int count=0;
 for(ll i=1;i<10000009;i++)
 {
  itoa(i,s,10);
    //ispalin=palin(s);
    if(palin(s))
    {
     itoa(i*i,s,10);
     if(palin(s))
     {ab[count]=i;count++;}
    }
 }
 //cout<<count;
}


int main ()
{
  ll t,a,b,check,no=1;
  double result;
  precalculate();  
  char s[100];
  cin>>t;
  while(t--)
  {
   cin>>a>>b;
   result=sqrt(a);
   check=result;
   if(result>check)
   {a=check+1;}
   else a=check;
   
   result=sqrt(b);
   check=result;
   if(result<check)
   {b=check-1;}
   else b=check;
   //cout<<"\n"<<a<<"  "<<b<<"\n";
   int count=0;
   for(int i=0;i<21;i++)
   {
    if(ab[i]>=a&&ab[i]<=b)
    count++;
   }
   
   cout<<"Case #"<<no<<": "<<count<<"\n";
   no++;
   
  }
  
  
}








