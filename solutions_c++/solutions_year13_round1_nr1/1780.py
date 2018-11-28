#include<iostream.h>
#include<math.h>
using namespace std;
int main()
{
    int t,ring=0,i;
    float rad,col,bru;
    cin>>t;
    for(i=1;i<=t;i++)
    {
              ring=0;
           cin>>rad>>bru;
           while(1)
           {
                   col=0;
                   col=pow(rad+1,2)-pow(rad,2);
                   rad+=2;
                   bru-=col;
                   if(bru>=0)
                   {
                            ring++;
                   }
                   else
                   {
                       break;
                   }
           }
           cout<<"Case #"<<i<<": "<<ring<<endl;
    }
}
