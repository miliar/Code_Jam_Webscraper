#include<stdlib.h>
#include<iostream>
using namespace std;
int main()
{
      int a, b, t, k, i, j, cnt=0, n;
      cin>>t;
      for(n=1; n<=t; n++)
      {
               cnt=0;
                cin>>a>>b>>k;
                for(i=0; i<a; i++)
                {
                         for(j=0; j<b; j++)
                         {
                                  if((i&j)<k)
                                  {
                                             cnt++;
                                  }
                         }
                }
                cout<<"Case #"<<n<<": "<<cnt<<"\n";
      }
      
      return 0;
}
      

      
