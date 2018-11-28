#include <iostream>
using namespace std;

typedef long long ll;

ll power(ll x,ll n)
{
    if(n == 0) return 1;

    if(n == 1) return x;

    ll t=power(x,n>>1);

    if(n%2 == 0) return t*t;

    else return (ll)x*t*t;
}


ll convert(ll n,int base)
{
    ll res=0ll;
    int i=0;
    while(n)
    {
        int digit=n%2;
        res+=digit*power(base,i);

        ++i;
        n>>=1;
    }
    return res;
}

ll notprime(ll n)
{
    ll i;
    for(i=2;i*i<=n;++i)
        if(n%i == 0) break;

    if(n%i == 0) return i;

    else return 0;      //boolean false
}

void printbin(ll n)
{
    if (n == 0) return ;

    printbin(n/2);
    cout<<n%2;
}

int main()
{
    //ios_base::sync_with_stdio(false);

    int t;
    cin>>t;

    ll N,J;
    cin>>N>>J;

    cout<<"Case #1:\n";

    ll n = (1llu<<N-1llu) + 1llu;
    ll iter=1;
    while(iter <= J)     //it is guaranteed that there is a solution
    {
        ll temp,out[9],k=0;
        for(int i=2;i<=10;++i)
        {
            temp=convert(n,i);
            ll x=notprime(temp);
            if(x != 0)
                out[k++]=x;

            else break;
        }

        if(k == 9)
        {
            printbin(n);
            cout<<' ';
            for(int i=0;i<k;++i) cout<<out[i]<<' ';
            cout<<'\n';

            iter++;
        }

        n+=2;
    }

    return 0;
}
