#include <iostream>
#include <math.h>
using namespace std;

int palindrome(long x,long y)
{
    int count=0;
    for(long j=x;j<=y;j++)
    {
  //      cout<<j<<"\n";
         long temp1=j;
         long rev=0;
         long dig=0;
         long a=sqrt(j);
//         int rev1=0;
//         int dig1=0;
         while(temp1>0)
         {
             dig=temp1%10;
             rev=rev*10+dig;
             temp1=temp1/10;
         }
    //     cout<<rev<<"\n";
         if(j==rev)
         {
             rev=0;
             float temp2=sqrt(j);
             if(temp2*temp2==j)
             {
                  while(a>0)
                  {
         
                      dig=a%10;
                      rev=rev*10+dig;
                      a=a/10;
                  }
      //            cout<<"rev:"<<rev;
                  if(temp2==rev)
                  {
                    //  cout<<"hey it is fair and square";
                      count++;
                  }
             }
         
         }
    }
    
    return count;
}
    
int main()
{
    int t=0;
    long long a=0,b=0;
    int temp;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
      cin>>a;
      cin>>b;
    
//        cout<<"calling function";
        temp=palindrome(a,b);
        cout<<"Case #"<<i<<": "<<palindrome(a,b)<<"\n";
    }
    return 0;
}




    
        

