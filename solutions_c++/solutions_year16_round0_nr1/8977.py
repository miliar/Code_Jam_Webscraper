#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

typedef long long ll;

struct liczer
{
    bool cyfry[10];
    ll left;
    
    void clear()
    {
        memset(cyfry, 0, sizeof(cyfry) );
        left = 10;
    }
    
    liczer()
    {
        clear();
    }
    
    bool dodaj(ll lic)
    {
        while(lic != 0)
        {
            ll a = lic % 10;
            if(!cyfry[a])
            {
                cyfry[a] = true;
                left--;
            }
            
            if(left == 0)
                return true;
            
            lic /= 10;
        }
        return false;
    }
};

ll stopien(ll n)
{
    ll cnt = 10;
    
    while(n >= cnt)
        cnt *= 10;
    
    return cnt*10;
}

liczer bera;

int main()
{
    ios_base::sync_with_stdio(0);
    
    ll t;
    cin>>t;
    
    for(ll x=1; x<=t; x++)
    {
        bera.clear();
        ll done = -1;
        ll n;
        cin>>n;
        ll en = stopien(n) * n;
        
        for(ll i=n; i < en; i += n)
        {
            if(bera.dodaj(i) )
            {
                done = i;
                break;
            }
        }
        
        cout<<"Case #"<<x<<": ";
        if(done == -1)
            cout<<"INSOMNIA\n";
        else
            cout<<done<<"\n";
        
    }
    
    
    return 0;
}