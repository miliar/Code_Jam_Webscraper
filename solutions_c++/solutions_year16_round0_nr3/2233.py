#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

//const ll MAX=66000;

//vector<ll> primes;
//bool isprime[MAX+1];
int n;

//void sieve()
//{
//    for(int i=3;i<=MAX;i+=2)
//        isprime[i]=1;
//    isprime[2]=1;
//    for(ll i=3;i*i<=MAX;i+=2)
//        if(isprime[i])
//            for(ll j=i*i;j<=MAX;j+=i)
//                isprime[j]=0;
//    primes.push_back(2);
//    for(int i=3;i<=MAX;i+=2)
//        if(isprime[i])
//            primes.push_back(i);
//}

unordered_map<ll,ll> getDivMAP;

ll getDiv(ll x)
{
    if(getDivMAP.count(x))
        return getDivMAP[x];
    for(ll i=2;i*i<=x;i++)
        if(x%i==0)
            return getDivMAP[x]=i;
    return getDivMAP[x]=-1;
}

vector<ll> solve(ll x)
{
    vector<ll> ret;
    for(int base=2;base<=10;base++)
    {
        ll cur=0;
        ll temp=x;
        for(int i=n-1;i>=0;i--)
            cur=cur*base+((x>>i)&1);
        ll div=getDiv(cur);
        if(div==-1)
            return vector<ll>();
        ret.push_back(div);
    }
    return ret;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
//    sieve();
    int t;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        cout<<"Case #"<<T<<":\n";
        int rem;
        cin>>n>>rem;
        ll mn=(1ll<<(n-1))+1;
        ll mx=(1ll<<n)-1;
        for(ll i=mn;i<=mx && rem;i+=2)
        {
            vector<ll> cur=solve(i);
            if(cur.size()==0)
                continue;
            for(int j=n-1;j>=0;j--)
                cout<<((i>>j)&1);
            for(int j=0;j<cur.size();j++)
                cout<<" "<<cur[j];
            cout<<"\n";
            rem--;
        }
    }
    return 0;
}
