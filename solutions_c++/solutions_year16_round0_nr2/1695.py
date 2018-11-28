#include <bits/stdc++.h>

using namespace std;

int main()
{
 long long t,ankur=1;
 cin>>t;
 while(t--)
 {
  string s;
  cin>>s;
  long count =0;
 
  
  for(long long i=s.size()-1;i>=0;i--)
  {
   if(s[i]=='-')
   {
    count++;
    s[i] = '+';
    for(long long j =0;j<i;j++)
    { 
     if(s[j]=='-')
     s[j] = '+';
     else
     s[j] = '-';
    }
    //cout<<s;
   }
  }


  cout<<"Case #"<<ankur++<<": "<<count<<endl;

 }

 return 0;
}

 
