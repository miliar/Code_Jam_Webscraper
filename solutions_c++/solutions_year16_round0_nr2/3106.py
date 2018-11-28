#include<iostream>
using namespace std;
int main()
{ int t,i;
cin>>t;
for(i=1;i<=t;i++)
{ long int n,count=0,j;
 string s;
cin>>s;
n=s.length();
if(n==1)
{ if(s[0]=='+')
   { cout<<"Case #"<<i<<": "<<0<<endl; continue; }
  else
  { cout<<"Case #"<<i<<": "<<1<<endl; continue;}
}
else
 for(j=1;j<n;j++)
   if(s[j-1]!=s[j])
    count++;
    
 if(s[n-1]=='+')
  cout<<"Case #"<<i<<": "<<count<<endl;
  else
   cout<<"Case #"<<i<<": "<<count+1<<endl;
}
} 
    