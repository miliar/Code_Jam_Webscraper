#include <bits/stdc++.h>

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define LET(x,a) __typeof(a) x(a)
#define tr(v,it) for( LET(it,v.begin()) ; it != v.end() ; it++)
#define rtr(v,it) for( LET(it,v.rbegin()) ; it != v.rend() ; it++)
#define present(x,c) ((c).find(x) != (c).end())    //stl container find
#define cpresent(x,c) (find(all(c),x) != (c).end())       //standard library find
#define sorti(a) sort(a.begin(),a.end())
#define sortd(a) sort(a.rbegin(),a.rend())
 
#define MEM(a,b) memset(a,b,sizeof(a))
#define rep(i,st,en) for(int i=(int)st; i<=(int)en;i++)
#define rrep(i,st,en) for(int i=(int)st; i>=(int)en;i--)
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define pf(x) printf("%s",x)
#define deb(x) cerr<<">value ("<<#x<<") : "<<x<<endl;
#define mod 1000000007

using namespace std;

ofstream fout("testout.txt");
ifstream fin("testin.txt");

typedef long long int ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

ll _sieve_size;
bitset<10000010> bs;   
vi primes; 
ll powers[20][20];
ll bases[15], answer[15], divisor = -1;
vector<ll> bin;

void sieve(ll upperbound)
{
	_sieve_size = upperbound + 1;
	bs.set();
	bs[0] = bs[1] = 0;
	for(ll i = 2; i <= _sieve_size; i++)
	{
		if(bs[i])
		{
			for(ll j = i * i; j <= _sieve_size; j += i)
				bs[j] = 0;
			primes.pb((int)i);
		}
	}
}

bool isPrime(ll N)
{
	if (N <= _sieve_size && bs[N]) 
		return bs[N];
	for(int i = 0; i < sz(primes); i++)
	{
		if(N % primes[i] == 0)
		{
			divisor = primes[i];
			return false;
		}
	}
	return true;
}

void powder()
{
	ll ans;
	rep(i, 1, 10)
	{
		ans = 1;
		rep(j, 1, 17)
		{
			ans = ans * (ll)i;
			powers[i][j] = ans;
		}
	}
	rep(i, 1, 10)
	{
		powers[i][0] = 1;
	}
}

bool check(ll num)
{   
	if(num%ll(2) == 0)
		return false;

	ll temp, co;
	memset(bases, 0, sizeof(bases));
	co = 0;
	bin.clear();
	while(num > 0)
	{
		temp = num%(ll)2;
		bin.pb(temp);
		if(temp == (ll)1)
		{
			rep(i, 2, 10)
			{
				bases[i] += powers[i][co];
			}
		}
		num = num/(ll)2;
		co++;
	}

	memset(answer, 0, sizeof(answer));

	rep(i, 2, 10)
	{
		if(isPrime(bases[i]))
		{
			return false;
		}
		answer[i] = divisor;
	}
	return true;
}


int main()
{
	int co = 0;
	sieve(10000005);
	powder();
	fout<<"Case #1:\n";
	rep(i, 32769, 65536)
	{
		if(check(i))
		{
			rtr(bin, it)
			{
				fout<<*it;
			}
			fout<<" ";
			rep(i, 2, 10)
			{
				fout<<answer[i]<<" ";
			}
			fout<<"\n";
			co++;
		}

		if(co == 50)
			break;
	}
	return 0;
}
