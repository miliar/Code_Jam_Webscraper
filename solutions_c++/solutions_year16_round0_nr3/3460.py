#include <iostream>
#include<math.h>
#include<bitset>
#include<iomanip>
using namespace std;
long unsigned int prime(long unsigned int n)
{  int i, flag=0;
   for(i=2;i<=sqrt(n);i++)
   {
       if(n%i==0)
       {
           flag=i;
           break;
       }
   }
   return flag;
}
int main()
{
   int t,n,s,j,i,flag=1;
   long unsigned int sum=0;
   string str;
   cin>>t;
   cin>>n>>s;
   for(i=0;i<n;i++)
   {
       sum+= (long unsigned int) pow(2,i);
   }


   cout<<"case #1:\n";
while(s>0)
 { long unsigned int base[10]={0,0,0,0,0,0,0,0,0,0};
      str= bitset<16>(sum).to_string();
      base[0]+= sum;
      for(i=15;i>=0;i--)
      {
          if(str[i]=='1')
          {
          base[1]+=   ceil( pow(3,(15-i)));
          base[2]+=   ceil(pow(4,(15-i)));
          base[3]+=   ceil(pow(5,(15-i)));
          base[4]+=   ceil(pow(6,(15-i)));
          base[5]+=   ceil(pow(7,(15-i)));
          base[6]+=   ceil(pow(8,(15-i)));
          base[7]+=   ceil(pow(9,(15-i)));
          base[8]+=   ceil(pow(10,(15-i)));
          }
      }

       for(i=0;i<=8;i++)
       {
           base[i] = prime(base[i]);
       }
    for(i=0;i<=8;i++)
     {
         if(base[i]==0)
         {  flag=0;
             sum-=2;
             break;
         }
     }

    if(flag ==1)
    {    s--;
         sum-=2;
        cout<<str.erase(0,16-n)<<" "<<base[0]<<" "<<base[1]<<" "<<base[2]<<" "<<base[3]<<" "<<base[4]<<" "<<base[5]<<" "<<base[6]<<" "<<base[7]<<" "<<base[8]<<"\n";
    }
   flag=1;
 }
return 0;
}
