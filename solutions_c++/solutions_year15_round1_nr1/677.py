#include <bits/stdc++.h>
using namespace std;
#define ll long long
// Useful constants
#define INF (int)2e9
#define INFL (long long)1e18
#define EPS 1e-9
// Useful hardware instructions
#define bitcount __builtin_popcount
#define gcd __gcd
// Useful container manipulation / traversal macros
#define all(a) a.begin(), a.end()
#define in(a,b) ( (b).find(a) != (b).end())
#define pb push_back
#define fill(a,v) memset(a, v, sizeof a)// fill originally
#define mp make_pair

// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
#define tr(container, it) for(aut(it,container.begin()); it != container.end(); it++)


#define llu long long unsigned
#define ld long


#define DEBUG 1
#define debug(x) {if (DEBUG)cout <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cout <<#x <<" = "; tr((x),it) cout <<*it <<", "; cout <<endl; }}


#define checkbit(n,b) ( (n >> b) & 1)
#define setbit(n,b) (n | ((1 << b)))
#define unsetbit(n,b) (n & (~(1 << b)))
#define rep(i,n) for(int i=0; i<(int)n;i++)
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define mod (1000000007L)

//typedef pair<int,pair<int,pair<int,int> > >  pp;

//freopen (fname"in","r",stdin);
//freopen (fname"out","w",stdout);

int n,m;
int k;
int data[100009];

void solve()
{
	s(n);

	rep(i,n)
	{
		s(data[i]);
	}

	ll maxi=0;
	ll sum=0;
	for(int i=0;i<n-1;i++)
	{
		ll tmp = data[i+1] - data[i];

		if(tmp < 0)
		{
			sum += abs(tmp);
			maxi = max(maxi,abs(tmp));
		}

	}
	cout<<sum<<" ";

	ll mini = INFL;
	for(ll rate=maxi;rate<50000;rate++)
	{

		sum=0;

		for(int i=0;i<n-1;i++)
		{
			ll tmp = data[i+1] - data[i];
			ll con = data[i] - rate;
			ll diff = min(rate,abs(tmp));

			if(rate > data[i])
			{
				sum += data[i];
			}
			else if(rate <= data[i])
			{
				if(con==data[i+1])
				{
					sum += rate;
				}
				else if(con > data[i+1])
				{
					sum=INFL;
					break;
				}
				else
				{
					sum += rate;
				}
			}


		}

		mini = min(mini,sum);

	}
	cout<<mini<<endl;


}

int main()
{
	int t;
	s(t);

	for(int cno=1;cno<=t;cno++)
	{
		cout<<"Case #"<<cno<<": ";

		solve();

	}
}
