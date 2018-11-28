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

ll n,b;
ll data[10009], fr[10009];

int checking(ll val)
{
	ll sum=0;

	rep(i,b)
	{
		sum += val/data[i];
		if(val%data[i] != 0) sum++;
	}

	if(sum <= n-1) return 1;
	return 0;

}
void solve()
{

	cin>>b>>n;

	rep(i,b)
	{
		cin>>data[i];
	}

	ll start = 	0, end = 1000000000000000L;
	ll mid;

	while(end-start>1)
	{
		mid=(end+start)/2;

		if(checking(mid)==1)
		{
			start=mid;
		}
		else
		{
			end=mid;
		}

	}

	fill(fr,0);
	ll sum=0,fin=0;

	rep(i,b)
	{
		sum += start/data[i];
		fin += start/data[i];
		if(start%data[i] != 0) sum++;
		fr[i]= (data[i] - (start)%data[i])%data[i];
		//cout<<fr[i]<<" , ";
	}

	//cout<<endl;
	//cout<<fin<<"  "<<sum<<" "<<start<<endl;
	ll mini=INFL;
	while(1)
	{
		mini=INFL;

		int indx;
		rep(i,b)
		{
			if(fr[i]<mini)
			{
				mini=fr[i];
				indx=i;
			}
		}



		rep(i,b)
		{
			fr[i] = ((fr[i] - mini));

		}

		fr[indx]=data[indx];


		fin++;
		sum++;
		if(sum==n)
		{
			cout<<indx+1<<endl;
			return ;
		}


	}
	/*
	mini=INFL;
	int indx;
	rep(i,b)
	{
		if(fr[i]<mini)
		{
			mini=fr[i];
			indx=i;
		}
	}

	cout<<indx+1<<endl;
*/
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
