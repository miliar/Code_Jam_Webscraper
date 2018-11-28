#include <bits/stdc++.h>
#define f first
#define s second
#define ll long long
#define pii  pair<int,int>
#define pli pair<ll,int>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define mod 1000000007

using namespace std;
int read()
{
    int  x;
    scanf("%d",&x);
    return x;
}

int getsum(ll a)
{
    int sum =0;
    while(a)
    {
        sum+=a%10;
        a/=10;
    }
    return sum;
}
ll Power(ll a , int b)
{
    ll res =1;
    while(b)
    {
        if(b%2) res = res*a;
        b/=2;
        a*=a;
    }
    return res;
}
ll convert_to_base(int base, ll num, int n)
{
    ll ans =0;
    for(int i=0;i<n;i++)
    {
        if(num&(1<<i)) ans+=Power(base,i);
    }
    return ans;
}


ll get_divisor(ll num,vector<ll> &primes)
{
    for(int i=0;i<primes.size() && primes[i] < num;i++)
    {
        if(num%primes[i]==0) return primes[i];

    }
    return -1;
}

string toString(ll a)
{
    string ans ="";
    for(int i=15;i>=0;i--)
    {
        if(a&(1<<i)) ans+='1';
        else ans+='0';
    }
    return ans;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int n3 = read(),n1=read(),n2=read();
    vector<ll> primes;
    primes.pb(2);
    for(int i=3;i<=1000000;i+=2)
    {
        bool flag =true;
        for(int j=0;primes[j]*primes[j]<=i;j++)
            {
                 if(i%primes[j]==0)
                {
                    flag =0;
                    break;
                }
            }
        if(flag) primes.pb(i);
    }

    int n=15;
    ll a = (ll)((1<<n) + 1);
    int j=0;
    cout << "Case #1:\n";
    while(j<50 && a<(1<<16))
    {
        vector<ll>divisors;
        bool flag =true;
        for(int i=2;i<=10;i++)
        {
            ll in = convert_to_base(i,a, 16);
            //cout << in <<  endl;
            ll div = get_divisor(in,primes);
            if(div==-1)
            {
                flag =0;
                break;
            }

            divisors.pb(div);
        }

        if(flag)
        {
            cout << toString(a) << ' ';
            for(int i=0;i<divisors.size();i++) printf("%d ", divisors[i]);
            printf("\n");
            j++;
        }

        a+=2;
    }

    return 0;
}
