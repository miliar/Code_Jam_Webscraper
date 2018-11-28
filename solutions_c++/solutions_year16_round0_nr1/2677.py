#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll g=0;
const ll tar=(1<<10)-1;

void mark(ll x)
{
    while(x)
    {
        int cur=x%10;
        g|=(1<<cur);
        x/=10;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        ll x;
        cin>>x;
        if(x==0)
        {
            cout<<"Case #"<<T<<": INSOMNIA"<<"\n";
            continue;
        }
        ll lst=x;
        g=0;
        mark(x);
        while(g!=tar)
        {
            lst+=x;
            mark(lst);
        }
        cout<<"Case #"<<T<<": "<<lst<<"\n";
    }
    return 0;
}
