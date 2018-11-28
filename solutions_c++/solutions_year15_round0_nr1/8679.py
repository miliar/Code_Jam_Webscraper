#include<iostream>
using namespace std;
int main()
{
 long t,s,sum,p;
 string str;
 cin>>t;
 for(long h=1;h<=t;h++)
 {
  p=0;
  
   cin>>s;
   cin>>str;
   sum=str[0]-48;
   for(long i=1;i<=s;i++)
   {
    if(i>sum && (str[i]-48)!=0)
    {
     p+=i-sum;
     sum+=i-sum;
    }
    sum+=str[i]-48;
   }
   cout<<"Case #"<<h<<": "<<p<<endl;
 }
 return 0;
 
}
