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
 
int R, N, M, K;


int next(vector<int> &p) {
	for (int i = sz(p) - 1; i >= 0; i--) {
		if (p[i] < M) {
			p[i]++;
			for (int j = i + 1; j < sz(p); j++) p[j] = p[i];
			return 1;
		}
	}
	return 0;
}

long double calc(vector<int> &p, int ind, int prod, int target) {
	if (ind == sz(p)) {
		return prod == target;
	}
	long double res = 0.;
	res += 0.5 * calc(p, ind + 1, prod, target);
	res += 0.5 * calc(p, ind + 1, prod * p[ind], target);
	return res;
}

int main(){
	int T; scanf("%d", &T);
	scanf("%d%d%d%d", &R, &N, &M, &K);
	printf("Case #1:\n");
	for (int test = 1; test <= R; test++) {
		vector<int> res(3, 1);
		long double res0 = 0.;
		vector<int> prod(K);
		for (int i = 0; i < K; i++) scanf("%d", &prod[i]); 
		vector<int> p(3, 1);
		do {
//			for (int i = 0; i < sz(p); i++) printf("%d%c", p[i], " \n"[i == 2]);
			long double cnt0 = 1.;
			for (int i = 0; i < K; i++) {
				cnt0 *= calc(p, 0, 1, prod[i]);
			}
			if (cnt0 > res0) {
				res = p;
			}
		} while (next(p));
		for (int i = 0; i < N; i++) printf("%d", res[i]);
		printf("\n");
	}
	return 0;
}
