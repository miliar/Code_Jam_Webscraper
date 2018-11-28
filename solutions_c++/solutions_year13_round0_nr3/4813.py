#include <iostream>
#include <stdio.h>
#include<math.h>
using namespace std;

int palindrome(unsigned __int64 k)
{
    unsigned __int64 n,k1;
    n = k;
    k1 = 0;
    while(n>0)
    {
              k1 = k1*10 + n%10;
              n = n/10;
    }
    if(k == k1)
    return 1;
    else
    return 0;
}

int main()
{
    unsigned __int64 a,b,c,k;
    int z=0,i,flag,n,count,t;
    cin>>t;
    while(z++<t)
    {
               cin>>a>>b;
               c = (int) sqrt(a);
               
               if(c*c < a)
               c++;
               count = 0;
               for(k=c;k*k<=b;k++)
               if(palindrome(k))
               if(palindrome(k*k))
               {
                   count++;
                   }
               cout<<"Case #"<<z<<": "<<count<<"\n";
    }
    return 0;
}
