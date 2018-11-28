#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cmath>
using namespace std;

int isPalindrome(int n)
{
   int reverse=0;
   int temp = n;

   while( temp != 0 )
   {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
   }

   if ( n == reverse )
      return 1;
   else
      return 0;

}

int main()
{
 int t,k=0;
 cin>>t;
 while(t--)
 {
     k++;
     cout<<"Case #"<<k<<": ";
    // char A[200],B[200];
     //cin>>A>>B;
     int a,b,count=0;
     cin>>a>>b;
     for(int i=a;i<=b;i++)
     {

     if(isPalindrome(i))
     {
         double  sq = sqrt(i);
         int sqr_int=sq;
         if(sq-sqr_int==0)
         {
             if(isPalindrome(sq))
             count++;
         }
     }

 }
 cout<<count<<endl;
}
}
