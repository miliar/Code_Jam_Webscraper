#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <vector>
#include <stack>
#include <list>
#include <utility>
#include <queue>
#include <set>
#include <map>
using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VP;
typedef vector<string> VS;

#define FOR(i,a,b) for(i=(a);i<(b);i++)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();it++)
#define ALL(x) x.begin(),x.end()
#define CLR(x, v) memset((x),v,sizeof (x))
#define gcd(a, b) __gcd(a, b)
#define PB push_back 
#define MP make_pair
#define INF 0x3f3f3f3f

int toInt(string s){ istringstream sin(s); int t; sin>>t; return t; }
template<class T> string toString(T x){ ostringstream sout; sout<<x; return sout.str(); }
template<class T> inline std::ostream& operator<<(ostream& os, const vector<T>& v) { FORE(it,v) os << *it << " "; return os; }
template<class T> void chmin(T &t, T f) { if (t > f) t = f; }
template<class T> void chmax(T &t, T f) { if (t < f) t = f; }
#define MOD 1000002013
//#define DEBUG
#ifdef DEBUG
#define ASSERT(x) assert(x)
#else
#define ASSERT(x)
#endif
struct Event
{
	Event() {}
	Event(int _n, int _p, int _f) : n(_n), p(_p), f(_f) {}
	int n;
	int p;
	int f;
	bool operator<(const Event &e2) const
	{
		if(n != e2.n) return n < e2.n;
		return f < e2.f;
	}
};
// -
Event event[2500];
VP v;

// -

// input
void init()
{
	v.clear();
}

void global_init()
{
}

ll calc(int n, int k)
{
	ll a = n*2-k+1;
	return a*k/2%MOD;
}

void solve()
{
	init();
	int n, m;
	cin>>n>>m;
	int i, j;
	int k = 0;
	ll p1 = 0, p2 = 0;
	FOR(i,0,m) {
		int o, e, p;
		cin>>o>>e>>p;
		event[k++] = Event(o,p,0);
		event[k++] = Event(e,p,1);
		p1 += calc(n, e-o) * p % MOD;
		p1 %= MOD;
	}
	sort(event, event+k);
	FOR(i,0,k) {
		Event e = event[i];
		if(!e.f) v.PB(MP(e.n,e.p));
		else {
			int l = v.size();
			int cur = e.p;
			for(j=l-1;j>=0;j--) {
				if(v[j].second > cur) {
					p2 += calc(n, e.n-v[j].first) * cur % MOD;
					p2 %= MOD;
					v[j] = MP(v[j].first, v[j].second-cur);
					break;
				} else {
					p2 += calc(n, e.n-v[j].first) * v[j].second % MOD;
					p2 %= MOD;
					cur -= v[j].second;
					v.pop_back();
				}
				if(cur==0) break;
			}
		}
	}
	ASSERT(v.size()==0);
	ll loss = p1 - p2;
	if(loss < 0) loss += MOD;
	cout << loss % MOD << endl;
}

int main()
{
	global_init();
	int T;
	cin>>T;
	for(int cs = 1; cs <= T; cs++) {
		cout << "Case #" << cs << ": ";
		clock_t start, finish;
		start = clock();   
		solve();
		finish = clock();   
		double duration = (double)(finish - start) / CLOCKS_PER_SEC;  
#ifdef DEBUG 
		cout << "Running time: " << duration << endl;
#endif
	}
	return 0;
}
