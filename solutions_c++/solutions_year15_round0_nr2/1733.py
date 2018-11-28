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


ll n;
ll data[10009];
ll sex[1009];
int isPossible(ll t)
{

	rep(i,n) sex[i]=data[i];

	sort(sex,sex+n);
	int flag=0;

	for(int i=0;i<t;i++)
	{
		ll val=i;
		ll com = t-i;

		flag=0;

		for(int j=n-1;j>=0;j--)
		{
			val -= ceil(data[j]/(double)com) - 1;
			if(val <0){
				flag=1;
				break;
			}
		}

		if(flag==0)
		{
			return 1;
		}
	}

	return 0;

}

void solve()
{
	cin>>n;

	rep(i,n) cin>>data[i];

	ll start=1,end=1000001;
	ll mid;

	if(isPossible(start)) {
		cout<<start<<endl;
		return ;
	}

	while(end-start>1)
	{
		mid=(start+end)/2;

		if(isPossible(mid))
		{
			end=mid;
		}
		else start=mid;
	}

	cout<<end<<endl;

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
