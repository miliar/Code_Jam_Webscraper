//Author : pakhandi
//
using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)

#define si(n) scanf("%d", &n)
#define sll(l) scanf("%lld",&l)
#define ss(s) scanf("%s", s)
#define sc(c) scanf("%c", &c)
#define sd(f) scanf("%lf", &f)

#define pi(n) printf("%d\n", n)
#define pll(l) printf("%lld\n", l)
#define ps(s) printf("%s\n", s)
#define pc(c) printf("%c\n", c)
#define pd(f) printf("%lf\n", f)

#define debug(x) cout<<"\n#("<<x<<")#\n"
#define nline printf("\n")

#define mem(a,i) memset(a,i,sizeof(a))

#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int

#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define PB push_back
#define SZ size
#define MP make_pair
#define fi first
#define sec second

std::vector<ll> v, x;

ll myPow(ll val, ll expo)
{
	if(expo == 0)
		return 1;
	if(expo == 1)
		return val;

	ll temp = myPow(val, expo / 2);
	temp = temp * temp;
	if(expo % 2)
		temp *= val;

	return temp;
}


//------------------------------------<BEGIN> SIEVE SNIPPET --------------------------


bool is_prime[1000006];


void sieve()
{
	ll limit=1000006, i, j;

	mem(is_prime,0);

	fl(i,2,limit+1)
	{
		is_prime[i] = 1;
	}

	ll inlimit = sqrt(limit);
	inlimit++;

	fl(i,2,inlimit)
	{
		if(is_prime[i]==1)
		{
			for(j=i*i; j<limit; j+=i)
			is_prime[j] = 0;
		}
	}

	return;
}

//------------------------------------<END> SIEVE SNIPPET --------------------------


ll numberOfBitsIn(ll x)
{
	ll ret = 0;

	ret += !(__builtin_popcount(x));

	while(x)
	{
		x /= 2;
		ret ++;
	}
	return ret;
}

ll DecimaltoBase(ll val, ll base)
{
	ll ret = 0;
	ll pos = 1;

	while(val)
	{
		ll temp = val % base;
		val /= base;
		ret = (pos * temp) + ret;
		pos *= 10;
	}

	return ret;
}

ll BasetoDecimal(ll val, ll base)
{
	ll pos = 0;
	ll ret = 0;

	while(val)
	{
		if(val % 10)
		{
			//cout<<pos<<" ";
			ret += myPow(base,pos);
			//cout<<ret<<" ";
		}
		pos++;
		val /= 10;
	}
	return ret;
}

int main()
{
	sieve();

	//cout<<BasetoDecimal(100011,2);

	ll i, j, n, k, l;

	ll cases;
	ll caseNo = 1;

	sll(cases);

	wl(cases)
	{
		sll(n);	sll(j);

		ll limit = (1 << n);

		fl(i,1,limit)
		{
			//cout<<i<<" "<<numberOfBitsIn(i); nline;
			if(numberOfBitsIn(i) != n)
				continue;

			if( (i&(1<<n-1)==(1<<n-1)) && (i&1) )
			{
				v.PB(i);
			}
			else
			{
				continue;
			}
		}
		cout<<"Case #"<<caseNo<<": ";
		nline;
		caseNo++;

		fl(i,0,v.SZ())
		{

			if(!j)
				break;

			ll ele = v[i];
			x.clear();


			ll bin = DecimaltoBase(ele,2);

			fl(k,2,11)
			{
				x.PB(BasetoDecimal(bin,k));
			}

			bool isAns = 1;

			fl(k,0,x.SZ())
			{
				int b = x[k];

				bool hasDiv = 0;

				fl(l,2,sqrt(x[k])+10)
				{
					if(l == x[k])
						break;
					if(x[k] % l == 0)
					{
						hasDiv = 1;
						break;
					}
				}

				if(hasDiv == 0)
					isAns = 0;
			}

			if(isAns == 0)
				continue;

			cout<<bin<<bin<<" ";
			fl(k,0,x.SZ())
			{
				fl(l,2,sqrt(x[k])+10)
				{
					if(x[k] % l == 0)
					{
						cout<<l<<" ";
						break;
					}
				}
			}
			nline;
			j--;
		}
		nline;
	}





	return 0;
}
/*
	Powered by Buggy Plugin
*/
