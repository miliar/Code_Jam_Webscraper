#include<stdio.h>
#include<iostream>
#include<fstream>
#include<math.h>
#include<cstring>
using namespace std;

int digits[10];

bool asleep()
{
   int count1=0;
   for(int j=0;j<10;j++)
   if(digits[j]==1)
   count1++;
   if(count1==10)
   return true;
   else
   return false;

}

int main()
{
   ifstream input;
   ofstream output;
   int tcase;
   input.open("A-large.in");
   output.open("output.in");
   input>>tcase;
   for(int i=1;i<=tcase;i++)
   {

      long long int n,k;
      input>>n;
      if(n==0)
      output<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
      else
      {
          //n = abs(n);
          memset(digits, 0, sizeof(digits));
          k=1;
          long long int m=n,flag=0,p;
          while(k<1000000000000){
          n=m*k;
          p=n;
          do {
            int digit= n % 10;
            if(digits[digit]==0)
            digits[digit]=1;
             n /= 10;
            if(asleep()){
            output<<"Case #"<<i<<": "<<p<<endl;
            flag=1;
            break;
            }
          } while (n>0);
          k=k+1;
          if(flag==1){
          flag=0;
          break;
          }
      }
      if(k>=1000000000000)
      output<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;

   }
 }
   input.close();
   output.close();

return 0;
}
