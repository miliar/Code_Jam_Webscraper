#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <deque>
#include <set>


using namespace std;

#define MAXN 1024*1024
#define n first
#define p second
#define mp make_pair
#define pb insert_back
#define sz(a) (int)(a.size())
#define all(a) a.begin(), a.end()
#define R(a) ((a)%mod)

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PI;
typedef vector<PI> VPI;
typedef vector<VPI> VVPI;
typedef vector<VVPI> VVVPI;
typedef vector<VVI> VVVI;

int T, N, M, s, e;
ll A, cost, B, mod = 1000002013, p;
multiset< pair< int, long long > > pq, E;
multiset< pair< int, long long > >::iterator it;
pair< int, long long > u, ed;

struct data
{
	int s, e;
	ll p;
	
	data(){}
	
	bool operator < ( const data &d ) const
	{
		return s < d.s;
	}
};
vector <data> v;

long long f ( int n )
{
	if (n&1)
		return R( R((ll)n)*R((ll)((2*N-n+1)/2)) );
	else
		return R( R((ll)(n/2))*R((ll)((2*N-n+1))) );	
}
int last;
int main (int argc, char const* argv[])
{
	cin >> T;
	
	for (int cs = 1; cs <= T; cs += 1)
	{
		cin >> N >> M;
		
		E.clear();
		pq.clear();
		A = 0;
		B = 0;
		v = vector<data>(M);
		last = 0;
		for (int i = 0; i < M; i += 1)
		{
			cin >> v[i].s >> v[i].e >> v[i].p;
		}
		
		sort(all(v));
		
		for (int j = 0; j < M; j += 1)
		{	
			if (v[j].s > last)
			{
				while (!E.empty() && !pq.empty())
				{
					it = pq.begin();
					u = *it;
					pq.erase(it);
					it = E.begin();
					ed = *it;
					E.erase(it);
					p = min(ed.p, u.p);
					cost = R(p*f(-ed.n-u.n));
					A = R(A+cost);
					u.p -= p;
					if ( u.p )
						pq.insert(u);
					ed.p -= p;
					if(ed.p)
						E.insert(ed);
				}
			}
			pq.insert(mp(v[j].s, v[j].p));
			E.insert(mp(-v[j].e, v[j].p));
			last = v[j].e;
			
			cost = R(v[j].p*f(v[j].e-v[j].s));
			B = R(B+cost); 
		}
		
		while (!E.empty() && !pq.empty())
		{
			it = pq.begin();
			u = *it;
			pq.erase(it);
			it = E.begin();
			ed = *it;
			E.erase(it);
			p = min(ed.p, u.p);
			cost = R(p*f(-ed.n-u.n));
			A = R(A+cost);
			u.p -= p;
			if ( u.p )
				pq.insert(u);
			ed.p -= p;
			if(ed.p)
				E.insert(ed);
		}
		cout << "Case #" << cs << ": " << B-A << '\n';
	}
	
	return 0;
}















