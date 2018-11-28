#include <bits/stdc++.h>

using namespace std;
#define ll long long
int main()
{
    ios_base::sync_with_stdio(0) ;
    freopen("A-large.in","r",stdin) ;
    freopen("A-large.out","w",stdout) ;
    ll t, cs = 1 ;
    cin >> t ;
    while(t--)
    {
        ll n ;
        cin >> n ;
        set<char> mys ;
        bool b = 0 ;
        for(ll i=1;i<=1000;i++)
        {
            ll temp = i*n ;
            stringstream ss ;
            string str ;
            ss << temp ;
            ss >> str ;
            for(int i=0;i<str.size();i++)
                mys.insert(str[i]) ;
            if(mys.size()==10)
            {
                cout << "Case #" << cs << ": " << temp << endl ;
                b = 1 ;
                break ;
            }
        }
        if(!b)
            cout << "Case #" << cs << ": INSOMNIA" << endl ;
        cs++ ;
    }

    return 0;
}
