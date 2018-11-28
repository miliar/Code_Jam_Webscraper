#include <iostream>
using namespace std;
int main()
{
    freopen ("B-small-attempt0.in","r",stdin);
	freopen ("output.in","w",stdout);
    long long int a,b,k,ctr=0,t,x=1;
    cin>>t;
    while(x<=t)
    {
               ctr=0;
    cin>>a>>b>>k;
    int i,j;
    for(i=0;i<a;i++)
    {
            for(j=0;j<b;j++)
            {
                   // cout<<i<<","<<j<<"="<<(i&j)<<"\n";
                     if((i&j)<k)
                     ctr++;
                    }
                      }
           cout<<"Case #"<<x<<": "<<ctr<<"\n";
           x++;
           }
                 // system("pause");
                  return 0;    
    
}
