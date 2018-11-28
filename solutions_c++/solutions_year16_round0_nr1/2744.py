#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll t,n,x;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        cin >> n;
        bool u[10]{};
        ll x=0;
        while(n*1e6>x && accumulate(u,u+10,0ll)!=10)
        {
            x+=n;
            ll k=x;
            while(k>0)
            {
                u[k%10]=1;
                k/=10;
            }
        }
        if(x>=n*1e6)cout << "Case #" << i << ": INSOMNIA\n";
        else cout << "Case #" << i << ": " << x << "\n";
    }
    return 0;
}
