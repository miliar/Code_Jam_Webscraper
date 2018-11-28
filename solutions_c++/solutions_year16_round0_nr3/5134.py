//  Mafi, KUET 2K11

#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef unsigned long long ull;

#define sc1(n) scanf("%d",&n)
#define sc2(a,b) scanf("%d %d",&a,&b)
#define sc3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define sl1(n) scanf("%lld",&n)
#define sl2(a,b) scanf("%lld %lld",&a,&b)
#define sl3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define mem(v,val) memset(v,val,sizeof v)
#define sz(v) v.size()
#define REVERSE(v) reverse(v.begin(),v.end())
#define SORT(v) sort(v.begin(),v.end())
#define pb push_back
#define ff first
#define ss second
#define MP make_pair
#define pp pair<int,int>
#define pp1 pair<int,pair<int,int> >
#define pp2 pair<pair<int,int>,int >

#define rep(i,n) for(i=1;i<=n;i++)
#define Rep(i,n) for(i=0;i<n;i++)
#define For(i,a,b) for(i=a;i<=b;i++)

#define INF INT_MAX
#define MAXN 100006
#define modu 1000003
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*b)/gcd(a,b)

#define read() freopen("C-small-attempt0.txt","r",stdin);
#define write() freopen("output.txt","w",stdout);

const double pi=acos(-1.0);

//int row[]={1,0,-1,0};int col[]={0,1,0,-1}; //4 Direction
//int row[]={1,1,0,-1,-1,-1,0,1};int col[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int row[]={2,1,-1,-2,-2,-1,1,2};int col[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction

ll leap(ll x)
{
    if((x%4==0&&x%100!=0)||x%400==0) return 1;
    return 0;
}

ll nCr(ll n, ll r)
{
    if(r==0) return 1;
    else return nCr(n-1,r-1)*n/r;
}

ll mod(ll N,ll M)//N%M
{
    ll temp = N/M;
    N-=temp*M;
    return N;
}

ll bigmod(ll N,ll M,ll MOD) //(N^M)%MOD
{
    if(M==0) return 1;
    if((M/2)*2==M)
    {
        ll ret = bigmod(N,M/2,MOD);
        return ((ret%MOD)*(ret%MOD))%MOD;
    }
    else return ((N%MOD)*bigmod(N,M-1,MOD)%MOD)%MOD;
}

ll modinverse(ll a,ll m)  //a*x=1(mod m)
{
    return bigmod(a,m-2,m);
}

struct Euclid
{
    ll x,y,d;
    Euclid() {};
    Euclid(ll xx,ll yy,ll dd)
    {
        x = xx, y = yy, d = dd;
    }
};

Euclid Extended_gcd(ll a, ll b)// input a,b Output x,y,d;ax+by = d,d=gcd(a,b)
{
    if(!b)
        return Euclid(1,0,a);
    Euclid e = Extended_gcd(b,a%b);
    return Euclid(e.y,e.x-a/b*e.y,e.d);
}

#define count_bit(x)    __builtin_popcountll(x) //number of 1 in binary of x; __builtin_popcount=int,__builtin_popcountl=long int,__builtin_popcountll=long long int
ll Set(ll N,ll pos)
{
    return N|(1LL<<pos);
}
ll reset(ll N,ll pos)
{
    return N&~(1LL<<pos);
}
ll check(ll N,ll pos)
{
    return (N&(1LL<<pos));
}

vector<ll>v;

int test,N,J;

ll mul(ll a, ll b, ll mod)
{
    ll ans = 0;
    while (b)
    {
        if (b & 1)
            ans = (ans + a) % mod;
        a = (a + a) % mod;
        b >>= 1;
    }
    return ans;
}
ll binByMod(ll a, ll to, ll mod)
{
    ll ans = 1;
    while (to)
    {
        if (to & 1)
            ans = mul(ans, a, mod);
        a = mul(a, a, mod);
        to >>= 1;
    }
    return ans;
}
ll randomLong()
{
    ll ans = 0;
    for (int i = 0; i < 1; ++i)
        ans = (ans << 20) ^ rand();
    return ans;
}

bool isPrime(ll n)
{
    if (n % 2 == 0 && n != 2||n==1)
        return false;
    for (int i = 0; i < 10; ++i)
    {
        ll a = (randomLong() % (n - 1));
        if (a < 0)
            a += n - 1;
        a += 1;

        a = binByMod(a, (n - 1) / 2, n);
        if (a != n - 1 && a != 1)
            return false;
    }

    return true;
}


ll solve(ll len,ll num)
{
    if(len==N)
    {
        v.pb(num);
        return 0;
    }

    if(len==0||len==N-1)
        solve(len+1,num*10+1);
    else
    {
        solve(len+1,num*10+1);
        solve(len+1,num*10);
    }
}

ll base_con(ll temp,ll base)
{
    ll res=0;

    ll mul=1;

    while(temp)
    {
        res+=(temp%10)*mul;
        mul*=base;
        temp/=10;
    }
    return res;
}



int main()
{
    //ios_base::sync_with_stdio(0);

    read();
    write();
    cin>>test;

    cin>>N>>J;

    solve(0,0);

    SORT(v);

    cout<<"Case #1:"<<endl;

    int cnt=0;

    for(int i=0; i<v.size(); i++)
    {
        ll temp=v[i];

        ll arr[11];

        for(ll j=2; j<=9; j++)
            arr[j]=base_con(temp,j);

        arr[10]=temp;

        if(!isPrime(arr[2])&&!isPrime(arr[3])&&!isPrime(arr[4])&&!isPrime(arr[5])&&!isPrime(arr[6])&&!isPrime(arr[7])&&!isPrime(arr[8])&&!isPrime(arr[9])&&!isPrime(temp))
        {
            cnt++;

            ll arr2[11];

            for(int k=2; k<=10; k++)
            {

                for(ll j=2; j*j<=arr[k]; j++)
                {
                    if((arr[k]/j)*j==arr[k])
                    {
                        arr2[k]=arr[k]/j;
                        break;
                    }
                }
            }

            printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld %lld\n",temp,arr2[2],arr2[3],arr2[4],arr2[5],arr2[6],arr2[7],arr2[8],arr2[9],arr2[10]);

        }

        if(cnt==J)
            break;
    }


    return 0;
}
