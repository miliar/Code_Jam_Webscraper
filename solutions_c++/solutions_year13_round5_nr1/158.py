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

//#define DEBUG
#ifdef DEBUG
#define ASSERT(x) assert(x)
#else
#define ASSERT(x)
#endif

// -

int n;
ll b, x[40];
ll r[40];

// -

// input
void init()
{
}

void global_init()
{
}

double go(ll tot)
{
	int i, j;
	FOR(i,1,37) if(x[i]!=x[i-1]) break;
	double t = 0;
	FOR(j,0,i) {
		t += (x[j] - r[j]) * 36;
	}
	t /= i;
	return t - tot;
}

void solve()
{
	init();
	cin>>b>>n;
	int i, j, k;
	int m = 37;
	FOR(i,0,n) cin>>x[i];
	FOR(i,i,m) x[i] = 0;
	sort(x,x+m);
	FOR(i,0,m) r[i] = x[i];
	ll p = 0;
	i = 0;
	while(i<m) {
		i++;
		FOR(i,i,m) if(x[i]!=x[i-1]) break;
		if(i>=36) {
			p += i;
			break;
		}
		p += (x[i] - x[i-1]) * i;
	}
	if(b > p) b = p;
	ll a = 0;
	if(b > m * 2) {
		a = b - m * 2;
		b = m * 2;
	}
	ll tot = a;
	while(true) {
		FOR(i,1,m) if(x[i]!=x[i-1]) break;
		if(a > (x[i] - x[i-1]) * i) {
			a -= (x[i] - x[i-1]) * i;
			FOR(j,0,i) x[j] = x[i];
		} else {
			FOR(j,0,i) x[j] += a/i;
			int k = a % i;
			for(j=i-1;j>=i-k;j--) x[j]++;
			break;
		}
	}
	double ans = go(tot);
	for(i=0;i<b;i++) {
		x[0]++;
		sort(x,x+m);
		tot++;
		ans = max(ans, go(tot));
	}
	printf("%.08lf\n",ans);
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
