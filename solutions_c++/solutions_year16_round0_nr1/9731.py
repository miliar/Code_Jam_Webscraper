#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main ()
{
    freopen("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    ll t; cin>>t;
    set<int > s; int cs = 1;
    while(t--)
    {
        s.clear();
        ll n; cin>>n; ll D; ll cnt = 0LL, rep = 0LL;
        for(ll i = 1; ; i++)
        {
            ll m = (ll)i*(ll)n;
            int sz = s.size();
            bool chk = false;
            D = m;
            while(D!=0)
            {
                if(D<10) s.insert((int) D);
                else
                {
                    int x = D%10;
                    s.insert((int)x);
                }
                if((int)s.size()==10)
                {
                    cout<<"Case #"<<cs<<": "<<m<<'\n';
                    cs++; chk = true; break;
                }
                D/=10;
            }
            if(chk) break;
            if(sz== (int)s.size()) cnt++;
            if(sz != (int) s.size()) cnt = 0LL;
            if(cnt > 111)
            {
                cout<<"Case #"<<cs<<": INSOMNIA"<<'\n';
                cs++; break;
            }
        }
    }
    return 0;
}

