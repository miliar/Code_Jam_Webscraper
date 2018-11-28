#include <iostream>

using namespace std;

int checkhash(int a[])
{
   for(int i=0;i<10;i++)
   {
       if(a[i]==0)
       {
           return 1;
       }
   }
   return -1;
}
int main()
{
   long long int t;
   cin>>t;
   for(int i=1;i<=t;i++)
   {
      long long int num;
      int chck=1;
      cin>>num;
      int a[10]={0,0,0,0,0,0,0,0,0,0};
      if(num==0)
      {
         cout<<"Case #"<<i<<": INSOMNIA"<<endl;
         continue;
      }
      int k=1;
      long long int num2;
      while(chck==1)
      {
         long long int num1=k*num;
         num2=k*num;
         do{
            a[num1%10]++;
            num1=num1/10;

         }while(num1!=0);
         chck=checkhash(a);
         k++;

      }
      cout<<"Case #"<<i<<": "<<num2<<endl;
   }
   return 0;
}
