#include<iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include<math.h>
using namespace std;

int ispalin(long long m)
{
    long long int a=m;
    long long int rev=0;
    int dig;
    while(m>0)
   {
        rev=rev*10 + (m%10);
        m/=10;

   }
   if (rev==a)
   return 1;
   else
   return 0;
}

int main()
{
    int T;
    cin>>T;
    for (int z=1;z<=T;z++)
    {
        long long A,B,x,y;
        int cnt=0;
        cin>>A>>B;
        x=floor(sqrt(A));
        if (x*x<A)
        x++;
        y=floor(sqrt(B));
        for(int i=x;i<=y;i++)
        {
            if (ispalin(i)==1)
            {
                if(ispalin(i*i)==1)
                cnt++;
            }
        }

        cout<<"Case #"<<z<<": "<<cnt<<endl;


}
}
