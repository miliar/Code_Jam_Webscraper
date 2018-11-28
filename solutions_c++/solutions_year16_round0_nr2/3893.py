#include <iostream>
using namespace std;

int main()
{
  int t;
  int i;
  cin>>t;
 
  for(int j=1;j<=t;j++)
  { string s;
  cin>>s;
  int sum=0;
   if(s[0]=='+')
      sum=0;
       if(s[0]=='-')
      sum=1;
     // cout<<sum<<"\n";
  for(i=1;i<s.length();i++)
  {
      //if(s[i]=="+"&&s[i-1]=="+")
     // sum=sum;
       if(s[i-1]=='+'&&s[i]=='-')
      sum=sum+2;
       //if(s[i]=="-"&&s[i-1]=="-")
      //sum=sum;
       //if(s[i]=="-"&&s[i-1]=="+")
      //sum=sum;
  }
      
      
     cout<<"Case #"<<j<<": "<<sum<<"\n"; 
      
  }
    return 0;
}
