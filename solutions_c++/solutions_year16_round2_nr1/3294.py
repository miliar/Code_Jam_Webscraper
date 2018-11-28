#include<bits/stdc++.h>
using namespace std ;

typedef long long ll ;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen ("output.in","w",stdout);
    ll t ;
    cin >> t ;
    for(ll i=1;i<=t;i++)
    {
        cout << "Case #" << i << ": " ;
        string s ;
        cin >> s ;
        ll a[200] = {0} ;
        for(ll j=0;j<s.size();j++)
            a[s[j]]++ ;
        vector<ll> v ;
        ll count = 0 ;
        if(a['Z']>=1)
        {
            ll temp = a['Z'] ;
            for( ll j=0;j<temp;j++)
                v.push_back(0) ;
            a['Z']-=temp ; a['E']-=temp ; a['R']-=temp ; a['O']-=temp ;
        }
        if(a['W']>=1)
        {
            ll temp = a['W'] ;
            for( ll j=0;j<temp;j++)
                v.push_back(2) ;
            a['T']-=temp ; a['W']-=temp ; a['O']-=temp ;
        }
        if(a['U']>=1)
       {
            ll temp = a['U'] ;
            for( ll j=0;j<temp;j++)
                v.push_back(4) ;
            a['F']-=temp ; a['O']-=temp ; a['U']-=temp ; a['R']-=temp ;
        }
        if(a['X']>=1)
        {
            ll temp = a['X'] ;
            for( ll j=0;j<temp;j++)
                v.push_back(6) ;
            a['S']-=temp ; a['I']-=temp ; a['X']-=temp ;
        }
        if(a['F']>=1)
       {
            ll temp = a['F'] ;
            for( ll j=0;j<temp;j++)
                v.push_back(5) ;
            a['F']-=temp ; a['I']-=temp ; a['V']-=temp ; a['E']-=temp ;
        }
        if(a['S']>=1)
       {
            ll temp = a['S'] ;
            for( ll j=0;j<temp;j++)
                v.push_back(7) ;
            a['S']-=temp ; a['E']-=temp ; a['V']-=temp ; a['E']-=temp ; a['N']-=temp ;
        }
         if(a['G']>=1)
       {
            ll temp = a['G'] ;
            for( ll j=0;j<temp;j++)
                v.push_back(8) ;
            a['E']-=temp ; a['I']-=temp ; a['G']-=temp ; a['H']-=temp ; a['T']-=temp ;
        }
         if(a['H']>=1)
       {
            ll temp = a['H'] ;
            for( ll j=0;j<temp;j++)
                v.push_back(3) ;
            a['T']-=temp ; a['H']-=temp ; a['R']-=temp ; a['E']-=temp ; a['E']-=temp ;
        }
         if(a['O']>=1)
       {
            ll temp = a['O'] ;
            for( ll j=0;j<temp;j++)
                v.push_back(1) ;
            a['O']-=temp ; a['N']-=temp ; a['E']-=temp ;
        }
         if(a['N']>=1)
       {
            ll temp = a['N']/2 ;
            for( ll j=0;j<temp;j++)
                v.push_back(9) ;
            a['N']-=temp ; a['I']-=temp ; a['N']-=temp ; a['E']-=temp ;
        }
        sort(v.begin(),v.end()) ;
        for(ll j=0;j<v.size();j++)
            cout << v[j] ;
        cout << "\n" ;
        v.clear() ;
    }
}
