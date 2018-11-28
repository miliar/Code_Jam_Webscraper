#include <iostream>
#include <string>

using namespace std;

int solve(int s[10],int l,int d,int f)
{
 int t1,t2;
 if(l==0)
  return f;
 else if(s[l-1]==d)
  return solve(s,l-1,d,f);
 else if(s[0]==(d+1)%2)  
 {
  int s1[10];
  for(int j=0;j<10;j++)
   s1[j]=s[j];
  for(int i=0;i<l;i++)
  {
   s[i]=(s1[l-i-1]+1)%2;
  }
  t1=solve(s,l-1,d,f+1);
  t2=solve(s1,l-1,(d+1)%2,f)+1;
  if(t1<t2)
   return t1;
  else
   return t2;
 }
 else
 {
  int s1[10];
  for(int j=0;j<10;j++)
   s1[j]=s[j];
  s[0]=(d+1)%2;
  for(int i=0;i<l;i++)
  {
   s[i]=(s1[l-i-1]+1)%2;
  }
  s[l-1]=(s[l-1]+1)%2;
  t1=solve(s,l-1,d,f+2);
  t2=solve(s1,l-1,(d+1)%2,f)+1;
  if(t1<t2)
   return t1;
  else
   return t2;
 }
}


int main()
{
 int t,s[10],l,a;
 string c;
 cin>>t;
 for(int i=1;i<=t;i++)
 {
   cin>>c;
   l=c.length();
   for(int j=0;j<l;j++)
   {
    s[j]=(c[j]=='+')?1:0;
   }
   a=solve(s,l,1,0);
   cout<<"Case #"<<i<<": "<<a<<"\n";
 }
 return 0;
}
   
