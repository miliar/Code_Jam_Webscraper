#include<bits/stdc++.h>
#define s(x) scanf("%d",&x)
#define ll long long
#define l(x) scanf("%I64d",&x)
#define cst int t; s(t); while(t--)
#define fr freopen("C-small-attempt0.in", "r", stdin)
#define finp ios_base::sync_with_stdio(false)
#define pb push_back
#define pf printf
using namespace std;

class jamcoin
{
    ll n, j;
public:
    void getinput(){
    cin>>n>>j;}
    bool isprime(ll n);
    ll conv(ll n,ll b);
    void solve();
    ll pow(ll a, ll b);
    ll getnum(ll n);
};

ll jamcoin::getnum(ll n)
{
    ll res=0;
    stack<ll> s;
    while(n>0){
        s.push(n%2);
        n/=2;
    }
    while(!s.empty())
    {
        res=res*10+s.top();
        s.pop();
    }
    return res;
}

ll jamcoin::pow(ll a, ll b)
{
    ll res=1;
    while(b--)
        res*=a;
    return res;
}

bool jamcoin::isprime(ll n)
{
    if(n<=1)
        return 0;
    for(ll i=2; i*i<=n; i++)
        if(n%i==0)
            return 0;
    return 1;
}

ll jamcoin::conv(ll n, ll b)
{
    if(b==10)
        return n;
    ll x=1;
    ll res=0;

    while(n>0){
        res+=(n%10)*x;
        n/=10;
        x*=b;
    }
    return res;
}

void jamcoin::solve()
{
    ll p=pow(2,n-1) , q=pow(2,2*n-n)-1;
    while(p<=q && j>0){
        ll x=getnum(p++);
        if(x%10==0)
            continue;
        bool flag=1;
        vector<ll> res;
        for(int i=2; i<=10 && flag; i++){
            ll y=conv(x, i);
            if(isprime(y))
                flag=0;
            res.pb(y);
        }
        if(flag==0)
            continue;
        j--;
        cout<<x<<' ';
        for(int i=0; i<res.size(); i++){
            for(ll k=2; k*k<=res[i]; k++)
                if(res[i]%k==0){
                    cout<<k<< ' ';
                    break;
                }
        }
        cout<<endl;
    }
}




int main()
{
    fr;
    freopen("out.txt", "w", stdout);
    int ct=0;
    cst{
        jamcoin ob;
        ob.getinput();
        cout<<"Case #"<<++ct<<":"<<endl;
        ob.solve();

    }
    return 0;
}
