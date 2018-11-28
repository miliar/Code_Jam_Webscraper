#include<functional>
#include<algorithm>
//#include<iostream>
#include<numeric>
#include<cassert>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
//#include<cmath>
#include<set>
#include<map>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b);i>=(e);--i)
#define FOReach(it,V) for(__typeof((V).begin()) it=(V).begin();it!=(V).end();++it)

#define PB push_back
#define ALL(V) (V).begin(),(V).end()
#define SIZE(V) ((int)(V).size())

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
	#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
	#define debug(...)
#endif

int stmp;
#define scanf stmp=scanf


const int MAX = 100000;
const int INF = 1000000001;
const int MOD = 1000002013;

map<int,LL> in, out;
set<int> S;
int n, m;
LL res;

int main(int argc, char *argv[]) {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d %d", &n, &m);
		res = 0;
		in.clear();
		out.clear();
		S.clear();
		while(m--)
		{
			LL a, b, p;
			scanf("%lld %lld %lld", &a, &b, &p);
			LL c = (LL)(n+(n-(b-a)+1))*(b-a)/2;
			c %= MOD;
			res = (res + c*p) % MOD;
			in[a] += p;
			out[b] += p;
			S.insert(a);
			S.insert(b);
		}
		LL r = 0;
		vector< pair<int,LL> > now;
		FOReach(s,S)
		{
			int i = in[*s];
			int o = out[*s];
			if(i > o) now.PB(MP(*s, i-o));
			if(i < o) {
				LL left = o-i;
				sort(ALL(now));
				reverse(ALL(now));
				REP(k,SIZE(now))
					if(now[k].ND > 0) {
						LL t = min(left, now[k].ND);
						now[k].ND -= t;
						left -= t;
						LL c = (LL)(n+(n-(*s-now[k].ST)+1))*(*s-now[k].ST)/2;
						c %= MOD;
						r = (r + c*t) % MOD;
					}
			}
		}
		printf("%lld\n", (res-r+MOD) % MOD);
	}
	return 0;
}

