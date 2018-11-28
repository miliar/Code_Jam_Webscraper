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

#ifdef DEBUG
#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}
#else
#define eprintf(...) {}
#endif

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

#define TASK "task"


void solve(int test) {
	long long r, t;
	scanf("%lld%lld", &r, &t);
	// 2 (r + 2 * i) + 1
	// 2r + 4 * i + 1
	// 2r * k + k + 2k(k - 1)
	long long left = 1;
	long long right = (long long)1e10;
	while (left + 1 < right) {
		long long ave = (left + right) >> 1;
		long double q = (long double)2 * r * ave + ave + 2 * (long double)ave * (ave - 1);
		if (q > t) {
			right = ave;
		} else {
			left = ave;
		}
	}
	printf("Case #%d: %lld\n", test, left);
}
int main(){
	// 2 * d + 1
	int T; scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		solve(test);
	}
	return 0;
}
