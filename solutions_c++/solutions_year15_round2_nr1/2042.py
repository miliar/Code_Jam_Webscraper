#include<bits/stdc++.h>
#define set(p) memset(p,-1,sizeof(p))
#define clr(p) memset(p,0,sizeof(p))
#define ll long long int
#define llu unsigned long long int
#define sll(n)                   scanf("%lld",&n)
#define sf(n)                   scanf("%lf",&n)
#define ss(n)                                   scanf("%s",n)
#define rep(i,a,n) for(i=(a);i<(n);i++)
#define pii pair<int,int>
#define pb(x) push_back(x)
#define v(x) vector<x>
using namespace std;

int gcd(int a,int b)
{
 int r, i;
  while(b!=0){
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}


long long int power(long long int x,long long int y,ll mod)
{
    long long int temp,ty,my;

    if( y == 0)
        return 1;
    temp = power(x, y/2,mod);
    ty=(temp%mod)*(temp%mod);
    if (y%2 == 0)
        {

                return ty%mod;
        }
    else
        {
                my=(x%mod)*(ty%mod);
                return my%mod;
        }
}

long long int mini(long long int a,long long int b)
{
        return a<b?a:b;
}

long long int maxi(long long int a,long long int b)
{
        return a>b?a:b;
}

ll maxx(ll a,ll b,ll c,ll d,ll e)
{
    return maxi(maxi(maxi(a,b),maxi(c,d)),e);
}


struct abhi
{
       ll val;
       ll pos;
};

struct abhi brr[100010];

bool cmp(struct abhi x,struct abhi y)
{
        return x.pos<y.pos;
}




ll REV(ll num_b)
{
	ll rever = 0;
	while(num_b!=0)
    {
		rever = rever * 10;

		rever = rever + num_b % 10;

		num_b = num_b /10;
	}

	return rever;
}

ll dp[1000110];

void precomp()
{
	dp[1] = 0;
	ll i;
	rep(i, 2, 1000100)
	{
		if (i % 10 == 0)
        {
			dp[i] = dp[i - 1] + 1;
			continue;
		}

		ll rever = REV(i);

		if (rever >= i)
        {
			dp[i] = dp[i - 1] + 1;
			continue;
		}

		dp[i] = mini(dp[i - 1] + 1, dp[rever] + 1);
	}
}

int main()
{
	precomp();

	ll t;
	//freopen("C:\\Users\\ABHISHEK004\\Desktop\\a1.in","r",stdin);
   // freopen("C:\\Users\\ABHISHEK004\\Desktop\\ab.out","w",stdout);


	sll(t);

	ll cas_n = 0;


	while (t--)
    {
		cas_n++;
		ll n;
		sll(n);
		ll ans=dp[n] + 1;
		printf("Case #%lld: %lld\n", cas_n,ans);
	}
    return 0;
}
