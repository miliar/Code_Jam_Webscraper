#include<iostream>
using namespace std;
int main()
{int t;
cin>>t;
for(int aa=1;aa<=t;aa++)
{



  long a,b,k,c=0;
  cin>>a>>b>>k;
  for(long f=0;f<a;f++)
     {for(long g=0;g<b;g++)
       {
        if ((f&g)<k)
            {
           c++;}

       }
      }

 cout<<"Case #"<<aa<<": "<<c<<"\n";


}
 return 0;
        }
