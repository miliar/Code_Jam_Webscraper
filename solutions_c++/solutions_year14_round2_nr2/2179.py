#include <iostream>
#include<string>
#include<stdio.h>
//#include<fstream.h>
using namespace std;

int main()
{
    freopen("A.in","r", stdin);
freopen("output.in","w", stdout);
   int   test,tt=1,n;
   cin>>test;

   while(test--)
   {

        cout<<"Case #"<<tt<<": ";

        int a,b,k,sum=0;
        cin>>a>>b>>k;
        for(int i=0;i<a;i++)
            {
                for(int j=0;j<b;j++)
                {
                    if((i&j)<k)sum++;
                }
            }
         cout<<sum<<endl;
        tt++;
   }
    return 0;
}
