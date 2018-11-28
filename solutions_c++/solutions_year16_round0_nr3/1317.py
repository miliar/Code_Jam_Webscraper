#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define pb push_back
#define sz(a) ((int)(a).size())
#define mp make_pair
#define fi first
#define se second

typedef pair<int,int> pint;
typedef long long ll;
typedef vector<int> vi;


#define MAX_N 35
#define MAX_S 12345

int N,J;
bool s[MAX_N];
vi primes;
bool mark[MAX_S];

void sieve()
{
	primes.pb(2);
	for (int i=4; i<MAX_S; i+=2)
		mark[i]=true;
	for (int i=3; i<MAX_S; i+=2)
		if (!mark[i])
		{
			primes.pb(i);
			if (i*1LL*i<MAX_S)
				for (int j=i*i; j<MAX_S; j+=i)
					mark[j]=true;
		}
}

bool check()
{
	vi fac;
	for (int b=2; b<=10; b++)
	{
		bool work=false;
		for (int p=0; p<sz(primes); p++)
		{
			int mod=primes[p],rem=0;
			for (int i=N; i>=0; i--)
				rem=(rem*b+s[i])%mod;
			if (rem==0)
			{
				fac.pb(mod);
				work=true;
				break;
			}
		}
		if (!work)
			return false;
	}
	for (int i=N; i>=0; i--)
		printf("%d",s[i]);
	printf(" ");
	for (int i=0; i<sz(fac); i++)
		printf("%d ",fac[i]);
	printf("\n");
	return true;
}

void f(int n)
{
	if (J==0)
		return;
	if (n==N)
	{
		if (check())
			J--;
		return;
	}
	s[n]=0;
	f(n+1);
	s[n]=1;
	f(n+1);
}

int main()
{
	sieve();
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		scanf("%d %d",&N,&J);
		printf("Case #%d:\n",asdf);
		N--;
		s[0]=s[N]=1;
		f(1);
	}
	return 0;
}
