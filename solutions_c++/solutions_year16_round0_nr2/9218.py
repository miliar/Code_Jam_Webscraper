#include<bits/stdc++.h>
using namespace std ;

typedef long long ll ;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen ("out.txt","w",stdout);
    ll t , i = 1 ;
    cin >> t ;
    for(i=1;i<=t;i++)
    {
        string s ;
        cin >> s ;
        cout << "Case #" << i << ": " ;
        ll count = 0 , flag = 0 , ans = 0 ;
        while(1)
        {
            ll l ;
            count = 0 ;
            for(l=s.size()-1;l>=0;l--)
            {
                if(s[l]=='+')
                    count++ ;
                else
                    break ;
            }
            if(count==(s.size()))
            {
                flag = 1 ;
                break ;
            }
            ll st ;
            ans++ ;
            for(st=0;st<=l;st++)
            {
                if(s[st]=='+')
                    s[st] = '-' ;
                else
                    s[st] = '+' ;
            }

            /*for(ll x=0;x<s.size();x++)
                cout << s[x] ;
            cout << "\n" ;*/
        }
        cout << ans << "\n" ;
    }
}
