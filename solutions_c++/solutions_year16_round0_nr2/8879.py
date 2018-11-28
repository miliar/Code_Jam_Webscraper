#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void flip(int n);
int solve(int n);


string s;

int main(void)
{
 
  int T;
  
  cin>>T;
  
  string data[T];
  
  for(int i=1; i<=T;i++)
  {
    cin>>data[i-1];
  }
  
  for(int i=1 ; i<=T;i++)
  {
    s=data[i-1];
    cout<<"Case #"<<i<<": "<<solve(s.size())<<"\n";
    
  }
  
  
  return 0;
  
}

int solve(int n)
{
  if(n==1)
  {
    if(s[0]=='-')
      return 1;
    else
      return 0;
  }
  
 if(s[n-1]=='+')
   return solve(n-1);
 else
 {
   if(s[0]=='-')
   {
     flip(n);
     return 1+solve(n-1);
   }
   else
   {
     int k =0;
     
     while(s[k]=='+')
       k++;
     
     flip(k);
     flip(n);
     return 2+solve(n-1);
   }
   
 }
  
  
}

void flip(int n)
{
  string s2 = string (s, 0, n);//subcopy of s, n first characters
  s2 = string ( s2.rbegin(), s2.rend() );//reverse s2
  
  for(int i=0;i<n;i++)
    s[i]=(s2[i]=='+')?'-':'+';//replace characters
  
  //cout<<"flipped string : "<<s<<"\n";
  
}
