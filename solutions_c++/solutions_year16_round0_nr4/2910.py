#include <iostream>
using namespace std;

typedef long long ll;

ll power(ll x,ll n)
{
    if(n == 0) return 1;
    
    if(n == 1) return x;
    
    ll t = power(x,n/2);
    
    if(n%2 == 0) return t*t;
    
    else return x*t*t;
}

int main()
{
    int t=1,T,K,C,S;
    cin>>T;
    
    while(t <= T)
    {
        cin>>K>>C>>S;
        
        cout<<"Case #"<<t<<": ";
        
        if(K == 1) cout<<1<<'\n';
        
        else
        {
            ll res = (power(K,C)-1)/(K-1);
            
            for(int i=0;i<K;++i) cout<<res*i+1<<' ';
            cout<<'\n';
        }
        
        ++t;
    }
        
    return 0;
}    