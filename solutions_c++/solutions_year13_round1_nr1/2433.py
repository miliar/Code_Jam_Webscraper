#include<iostream.h>
#include<math.h>
using namespace std;
int main()
{
    int t,ring=0,i;
    float r,c,b;
    cin>>t;
    for(i=1;i<=t;i++)
    {
              ring=0;
           cin>>r>>b;
           while(1)
           {
                   c=0;
                   c=pow(r+1,2)-pow(r,2);
                   r+=2;
                   b-=c;
                   if(b>=0)
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
