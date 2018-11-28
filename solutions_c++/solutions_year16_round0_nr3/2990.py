#include<bits/stdc++.h>
using namespace std;
#define ll unsigned long long
ll s;
ll n,j;

vector<ll>g[550];
vector<ll>L;

bool checkBit(int pos)
{
    return (s&(1<<pos))?true:false;
}
void clearBit(int pos)
{
    s=(s^(1<<pos));
}
void setBit(int pos)
{
    s=(s|(1<<pos));
}

ll myPow(int base, int power)
{
    ll ans=1;
    for(int i=0; i<power; i++)
        ans*=(ll)base;
    return ans;
}

bool isPrime(ll n)
{
    if(n==1)return false;
    if(n==2)return true;
    if((n%2)==0) return false;
    ll lim=sqrt(n);
    for(ll i=3; i<=lim; i+=2)
        if((n%i)==0)return false;
    return true;
}

ll bC(int b)
{
    ll re=0;
    for(int i=0; i<n; i++)
    {
        if( s &(1<<i) )
            re+=myPow(b,i);
    }
    return re;
}

ll divisor(ll n)
{
    for(ll i=2; i<n; i++)
    {
        if(!(n%i))return i;
    }
}

void solve()
{
    s=0;
    s=(s|1);
    s=(s|(1<<(n-1)));

    int c=0;
    bool flag;


    while(true)
    {
        flag=true;
        for(int i=1; i<(n-1); i++)
        {
            if(flag)
            {
                if(checkBit(i))
                    clearBit(i);
                else
                {
                    setBit(i);
                    flag=false;
                }
            }
            else break;
        }

        ll val;
        vector<ll>v;
        bool check=true;

        for(int i=2; i<=10; i++)
        {
            val=bC(i);
            if(isPrime(val)==false)
            {
                v.push_back(val);
            }
            else
            {
                check=false;
                break;
            }
        }

        if(check)
        {
            L.push_back(v[8]);
            for(int i=0; i<9; i++)
            {
                g[c].push_back(divisor(v[i]));
            }
            c++;
            if(c==j)
                break;
        }
    }
}

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    for(int c=1; c<=t; c++)
    {
        cin>>n>>j;
        solve();
        cout<<"Case #"<<c<<":"<<endl;
        for(int i=0; i<j; i++)
        {
            cout<<L[i];
            for(int j=0; j<9; j++)
                cout<<" "<<g[i][j];
            cout<<endl;
        }
    }
    return 0;
}
