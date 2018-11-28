#include <iostream>
using namespace std;
#define ll long long

int main()
{
    ll t,n,p,c,temp,j;
    cin>>t;
    for(ll i=1;i<=t;i++)
    {
        cin>>n;
        ll a[10]={0};
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else
        {
            c=0;
           for(j=1;c<10;j++)
           {
              p=n*j;
              
              
              temp=p;
              while(p>0)
              {
                if(a[p%10]==0)
                {
                    a[p%10]++;
                    c++;
                }
                if(c==10)
                {
                    cout<<"Case #"<<i<<": "<<temp<<endl;
                    break;
                }
                 
                 p/=10;
                 
              }
              
           }
        }
    }
    return 0;
}

