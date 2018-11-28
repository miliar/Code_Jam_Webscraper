#include <iostream>
using namespace std;

int main()
{
    long long int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        long long int n,res=0,s=0,temp=2,a;
        cin>>n;
        if(n==0)
        {
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
        }
        else
        { 
           s=n;
           int x[10]={0};
           while(1)
           {
               while(res!=10&&n)
               {
                   if(x[n%10]==0)
                   {
                      res++;
                      x[n%10]=1;
                   }
                   n=n/10;
               }
               if(res==10)
               {
                   break;
               }
               n=temp*s;
               a=n;
               temp++;
           }
           cout << "Case #" << i << ": " << a << endl;
        }
       
    }
    return 0;
}
