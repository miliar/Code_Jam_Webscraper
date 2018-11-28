#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long LL;
typedef long double LD;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define y1 y1_gedjcdgfce
#define y0 y0_sadasdasdsa
#define ws ws_sadsadsada
#define left left_asdsadsadsadsa
#define right right_asdasdsadasda
#define hash hash_asdasdasdsad

#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

#define TASK "task"



const int maxn = (int)1e5;
int p[maxn];
long long v[maxn];
long long E, R;
map<int, long long> rem;
map<int, long long> sto;

int cmpv(int o1, int o2) {
	return v[o1] > v[o2];
}

long long add(int obj) {
	//eprintf("add %d\n", obj);
	map<int, long long>::iterator tt = rem.lower_bound(obj);
	tt--;
	//assert(rem.lower_bound(obj) != rem.end());
	pair<int, long long> it = *(tt);
	long long rr = min(it.second + (obj - it.first) * R, E);
	pair<int, long long> jt = *sto.upper_bound(obj);
	long long ss = jt.second - (jt.first - obj) * R;
	//eprintf("rr = %lld, ss = %lld\n", rr, ss);
	//q + R >= ss && q <= rr
	long long q = max(ss, 0LL);
	assert(q <= rr);
	rem[obj] = q;
	sto[obj] = rr;
	return v[obj] * (rr - q);
}

int main(){
	int T; scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		eprintf("test = %d\n", test);
	   	int n;
		scanf("%lld%lld%d", &E, &R, &n);
		long long res = 0;
		rem.clear();
		sto.clear();
		R = min(R, E);
		rem[-1] = E;
		sto[n]  = 0;
		for (int i = 0; i < n; i++) scanf("%lld", &v[i]), p[i] = i;
		sort(p, p + n, cmpv);
		for (int i = 0; i < n; i++) {
			res += add(p[i]);
		}
		printf("Case #%d: %lld\n", test, res);
	}	
	return 0;
}
