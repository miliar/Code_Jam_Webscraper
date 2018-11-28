#include <bits/stdc++.h>
using namespace std;
#define ll long long
// Useful constants
#define INF (int)2e9
#define INFL (long long)1e18
#define EPS 1e-8
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

#define down 0
#define upp 1
#define left 2
#define right 3

//typedef pair<int,pair<int,pair<int,int> > >  pp;

//freopen (fname"in","r",stdin);
//freopen (fname"out","w",stdout);

int n;


double r[109],c[109];

void solve()
{

	s(n);

	double v,t;
	cin>>v>>t;

	double x1,x2,t1,t2;

	rep(i,n)
	{
		cin>>r[i]>>c[i];
	}

	if(n==1)
	{
		if(c[0] <= t + EPS && c[0] >= t-EPS)
		{

			double ans = v/r[0];
			printf("%0.9lf\n",ans);
			return;
		}
		else cout<<"IMPOSSIBLE"<<endl;
		return;
	}

	t1 = c[0];t2=c[1];

	if(t1 <= t-EPS && t2 <= t-EPS)
	{
		cout<<"IMPOSSIBLE"<<endl;
				return;
	}

	if(t1 >= t+EPS && t2 >= t+EPS)
		{
			cout<<"IMPOSSIBLE"<<endl;
					return;
		}


	if(abs(t1-t2)<=EPS && abs(t1 - t) > EPS)
	{
		cout<<"IMPOSSIBLE"<<endl;
				return;
	}
	else if(abs(t1-t2)<=EPS)
	{
		double rr=r[1] + r[0];
		printf("%0.9lf\n",(v/rr));
		return ;

	}


	x2 =( v*(t - t1))/(t2-t1);
	x1 = v-x2;

	if(x1>= v + EPS || x2>= v+EPS)
	{
		cout<<"IMPOSSIBLE"<<endl;
						return;
	}

	double ans = x2/r[1],ans2 = x1/r[0];




	if(ans>ans2)printf("%0.9lf\n",ans);
	else printf("%0.9lf\n",ans2);
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
