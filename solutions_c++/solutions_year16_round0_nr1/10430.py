#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
      freopen("in.txt", "r", stdin);
      freopen("out.txt", "w", stdout);
    ll t;
    cin >> t;
    ll k=1;

    while(t--)
    {
        set <ll> s;
        ll n;

        cin >> n;
        s.clear();
        ll i=1;
        ll m=n;
        if(n!=0)
        {
            while(s.size()!=10)
            {
                ll p = n*i;
                //cout << s.size() << " ";
                m=p;
                i++;

                while(p)
                {
                    s.insert(p%10);

                    //cout << p << " " ;
                    if(s.size()==10)
                        break;

                    p=p/10;
                }
            }
            printf("Case #%lld: %lld\n",k++,m);

        }
        else
        printf("Case #%lld: INSOMNIA\n",k++);

    }

}
