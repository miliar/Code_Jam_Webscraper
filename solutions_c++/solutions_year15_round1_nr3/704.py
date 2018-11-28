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

int n;

map<pair<int,int> ,int> m;

struct PT
{
	long long int x, y,idx;
	PT() {}
	PT(long long int x, long long int y) : x(x), y(y) {}
	PT(const PT &p) : x(p.x), y(p.y)    {}
	PT operator + (const PT &p)  const { return PT(x+p.x, y+p.y); }
	PT operator - (const PT &p)  const { return PT(x-p.x, y-p.y); }
	PT operator * (long long int c)     const { return PT(x*c,   y*c  ); }
	PT operator / (long long int c)     const { return PT(x/c,   y/c  ); }
};

double  dot(PT p, PT q)     { return p.x*q.x+p.y*q.y; }
double dist2(PT p, PT q)   { return dot(p-q,p-q); }
double cross(PT p, PT q)   { return p.x*q.y-p.y*q.x; }

PT lower_left;
bool sorter(const PT &p, const PT &q)
{
	long long int cpq = cross(p-lower_left, q-lower_left);
	if(cpq == 0)
		return dist2(p, lower_left) < dist2(q, lower_left);
	return cpq>0;
}
ll mini[16],  bitmapy[16];
vector<PT> f;
//size of A should at least be three
vector<int> hull_size(vector <PT> &A)
						{
	vector <PT> hull;

	for (int i = 1; i < A.size(); ++i)
	{
		if(A[i].y < A[0].y || (A[i].y <= A[0].y && A[i].x < A[0].x))
		{
			swap(A[0],A[i]);
		}
	}
	lower_left = A[0];


	sort(A.begin()+1, A.end(),  sorter);
	hull.clear();
	hull.push_back(A[0]);

	hull.push_back(A[1]);

	int hull_sz=2;
	for (int i = 2; i < A.size(); ++i)
	{
		while(hull_sz > 1 && cross(hull[hull_sz-1]-hull[hull_sz-2], A[i]-hull[hull_sz-1]) <= 0)
		{
			hull.pop_back();
			// ans.pop_back();
			hull_sz--;
		}
		hull.push_back(A[i]);
		// ans.push_back(A[i].idx);
		hull_sz++;
	}
	vector<int>ans;
	int len=hull.size();
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<len;j++)
		{
			PT A1=hull[j];
			PT B1=hull[(j+1)%len];
			PT C1=f[i];

			double dist=cross(B1-A1,C1-B1)/sqrt(dist2(A1,B1));

			int dot1=dot(B1-A1,C1-B1);
			if(dot1 > 0)
				dist=sqrt(dist2(A1,B1));
			int dot2=dot(A1-B1,C1-A1);
			if(dot2 > 0)
				dist=sqrt(dist2(A1,C1));
			if(dist < EPS)
			{
				ans.pb(i);
				break;
			}

		}
	}

	return ans;
						}

void solve();
ll x[16],  y[16];


void init()
{
	m.clear();
	f.clear();


	cin >> n;
	f.resize(n);
	for(int i=0;i<n;i++)
	{
		cin >> x[i] >> y[i];
		m[mp(x[i],y[i])]=i;
		f[i].x=x[i];
		f[i].y=y[i];
	}


	for(int i=0;i<16;i++)
		mini[i]= INF;
}

void outp()
{
	rep(i,n)
	{
		cout<<mini[i]<<endl;
	}
}



int main()
{
	int t;
	s(t);

	for(int cno=1;cno<=t;cno++)
	{
		cout<<"Case #"<<cno<<":"<<endl;

		solve();

	}
}

int val, cnt=0,one=0,len;
vector<int> ret;
void solve()
{

	init();
	for(int i=1;i<(1<<n);i++)
	{
		cnt=one=0;
		fill(bitmapy,0);
val=i;
		while(val > 0)
		{
			bitmapy[cnt++]=val&1;
			if(val&1)
				one++;
			val=val/2;
		}
		if(one <= 2)
		{
			rep(j,cnt)
			{
				if(bitmapy[j] == 1)
				{
					mini[j] = min(mini[j],(ll)n-one);
				}
			}
			continue;
		}
		len=one;

		vector <PT> A(len);
		int p1=0;
		for(int j=0;j<cnt;j++)
		{
			if(bitmapy[j] == 1)
			{
				A[p1].x=x[j];
				A[p1].y= y[j];
				p1++;
			}
		}

		ret=hull_size(A);
		rep(j,ret.size())
		{
			int idx=ret[j];
			mini[idx]=min(mini[idx],(ll)n-len);
		}
	}


	outp();
}
