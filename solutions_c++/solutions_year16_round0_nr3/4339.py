#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define f first
#define s second
#define si(x)   scanf("%d",&x)
#define sl(x)   scanf("%I64d",&x)
#define CLR(x)  memset(x,0,sizeof(x))
#define RESET(x,a) memset(x,a,sizeof(x))
#define pi pair<int,int>
#define pb push_back
#define mp make_pair
#define debug(x) cerr<<">value ("<<#x<<") : "<<x<<endl;

int lp[100000004];
vector<int>pr;
void primelp(int n)
{
    for(int i=2; i<=n; i++)
    {
        if(lp[i]==0)
        {
            lp[i]=i;
            pr.pb(i);
        }
        for(int j=0; j<pr.size() && pr[j]<=lp[i] && i*pr[j]<=n; j++) lp[i*pr[j]]=pr[j];
    }
}

ll mulmod(ll a, ll b, ll mod)
{
    ll x = 0,y = a % mod;
    while (b > 0)
    {
        if (b % 2 == 1)
        {
            x = (x + y) % mod;
        }
        y = (y * 2) % mod;
        b /= 2;
    }
    return x % mod;
}
/*
 * modular exponentiation
 */
ll modulo(ll base, ll exponent, ll mod)
{
    ll x = 1;
    ll y = base;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            x = (x * y) % mod;
        y = (y * y) % mod;
        exponent = exponent / 2;
    }
    return x % mod;
}

/*
 * Miller-Rabin primality test, iteration signifies the accuracy
 */
bool Miller(ll p,int iteration)
{
    if (p < 2)
    {
        return false;
    }
    if (p != 2 && p % 2==0)
    {
        return false;
    }
    ll s = p - 1;
    while (s % 2 == 0)
    {
        s /= 2;
    }
    for (int i = 0; i < iteration; i++)
    {
        ll a = rand() % (p - 1) + 1, temp = s;
        ll mod = modulo(a, temp, p);
        while (temp != p - 1 && mod != 1 && mod != p - 1)
        {
            mod = mulmod(mod, mod, p);
            temp *= 2;
        }
        if (mod != p - 1 && temp % 2 == 0)
        {
            return false;
        }
    }
    return true;
}

int f(ll n)
{
    for(int i=0;i<(int)pr.size();i++)
    {
        if(n%pr[i]==0)
            return pr[i];
    }
    return -1;
}

int main()
{
//    ios_base::sync_with_stdio(false);
//    cin.tie(NULL);
    //freopen("1.in","r",stdin);
    freopen("C_helper.txt","w",stdout);
    int tt,t,n,i,j,k,cnt;
    primelp(100000000);
    n=pr.size();
    ll m,tm;
    vector<ll> val;
    val.resize(11);
    for(n=4; n<=16; n++)
    {
        printf("%d\n",n);
        cnt=0;
        for(int ii=0;ii<(1<<(n-2));ii++)
        {
            bool ok=true;

            for(i=2;i<=10;i++)
            {
                m=1LL;
                tm=(ll)i;
                for(j=0;j<n-2;j++)
                {
                    if(ii&(1<<j))
                        m+=tm;
                    tm=tm*(ll)i;
                }
                m+=tm;
                if(Miller(m,6))
                {
                    ok=false;
                    break;
                }
                val[i]=m;
            }
            if(ok)
            {
                ll tans=val[10];
                for(i=2;i<=10;i++)
                {
                    val[i]=f(val[i]);
                    if(val[i]==-1)
                        break;
                }
                if(i!=11)
                    continue;
                cnt++;
                printf("%lld ",tans);
                for(i=2;i<=10;i++)
                {
                    printf("%d ",val[i]);
                }
                printf("\n");
                if(cnt>=50)
                    break;
            }
        }
        debug(cnt);
        //printf("Case #%d: %d\n",t,ans);
    }
    printf("-1\n");
    return 0;
}

