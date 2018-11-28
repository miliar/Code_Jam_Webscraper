#include<bits/stdc++.h>
using namespace std ;

typedef long long ll ;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen ("out.txt","w",stdout);
    ll t , i = 1 ;
    cin >> t ;
    for(i=1;i<=t;i++)
    {
        ll n ;
        cin >> n ;
        cout << "Case #" << i << ": " ;
        ll d = n ;
        if(n==0)
            cout << "INSOMNIA\n" ;
        else
        {
            ll a[10] = {0} , count = 0 ;
            while(1)
            {
                ll n1 = n ;
                do {
                    ll digit = n1 % 10;
                    if(a[digit]==0)
                        count++ ;
                    a[digit]++ ;
                //cout << digit << " " ;
                    n1 /= 10;
                } while (n1 > 0);
                if(count==10)
                    break ;
                n += d ;
            }
            cout << n << "\n" ;
        }
    }
}
