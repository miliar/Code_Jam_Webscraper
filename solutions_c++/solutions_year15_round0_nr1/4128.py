#include <iostream>
#include <string>

using namespace std;

int main()
{
 int t,smax,length;
 long  long int sum,extra,temp;
 string c;
 cin>>t;
 for(int k=1;k<=t;k++)
 {
  cin>>smax>>c;
  sum=0;
  extra=0;
  length=c.length();
  for(int i=0;i<length;i++)
  {
   temp=c[i]-'0';
   if(i>sum)
   {
    extra+=i-sum;
    sum+=i-sum+temp;
   }
   else
   {
    sum+=temp;
   }
  }
  cout<<"Case #"<<k<<": "<<extra<<"\n";
 }
 return 0;
}
