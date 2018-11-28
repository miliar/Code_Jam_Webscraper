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


ll n,l,x;
string lll,data;
char vals[100009];
int flag[100009];
void solve()
{
	cin>>l>>x;
	cin>>lll;
	data="";
	rep(i,x) data = data + lll;

	n = data.size();
	fill(flag,0);

	vals[0] =  data[0];

	int done[3];

	fill(done,0);

	if(vals[0]=='i')
	{
		done[0]=1;
	}

	for(int i=1;i<n;i++)
	{
		int sign=0;

		if(vals[i-1] == '1' && data[i] == 'i')
		{
			vals[i] = 'i';
		}
		else if(vals[i-1] == 'i' && data[i] == 'i')
		{
vals[i]='1';sign=1;
		}
		else if(vals[i-1] == 'j' && data[i] == 'i')
		{
vals[i]='k';sign=1;
		}
		else if(vals[i-1] == 'k' && data[i] == 'i')
		{
vals[i]='j';
		}
		else if(vals[i-1] == '1' && data[i] == 'j')
		{
vals[i]='j';
		}
		else if(vals[i-1] == 'i' && data[i] == 'j')
		{
vals[i]='k';
		}
		else if(vals[i-1] == 'j' && data[i] == 'j')
		{
vals[i]='1';sign=1;

		}
		else if(vals[i-1] == 'k' && data[i] == 'j')
		{
vals[i]='i';sign=1;

		}
		else if(vals[i-1] == '1' && data[i] == 'k')
		{
vals[i]='k';
		}
		else if(vals[i-1] == 'i' && data[i] == 'k')
		{
vals[i]='j';sign=1;
		}
		else if(vals[i-1] == 'j' && data[i] == 'k')
		{
vals[i]='i';

		}
		else if(vals[i-1] == 'k' && data[i] == 'k')
		{
vals[i]='1';sign=1;
		}


		if(flag[i-1]==1 && sign==1)
		{
			flag[i]=0;
		}
		else if(flag[i-1]==1 && sign==0)
			flag[i]=1;
		else if(flag[i-1]==0 && sign==1) flag[i]=1;
		else flag[i]=0;

		if(vals[i]=='i' && flag[i]==0 && done[0]==0)
		{
			done[0]=1;
		}

		if(vals[i]=='k' && flag[i]==0 && done[0]==1 && done[1]==0)
		{
			done[1]=1;
		}

	}

	if(done[0]==1 && done[1]==1 && vals[n-1]=='1' && flag[n-1]==1)
	{
		cout<<"YES"<<endl;
	}
	else cout<<"NO"<<endl;



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
