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


const int maxn = 2000;
const long long mode = 1000002013;

long long add(long long a, long long b) {
	return ( a % mode + b % mode ) % mode;
}

long long mult(long long a, long long b) {
	return ((a % mode) * (b % mode)) % mode;

}

long long T, N;
int cmpT(pair<long long, long long> a, pair<long long, long long> b) {
	return 
		N * (T - a.first) - (a.first) * (a.first - 1) / 2LL + a.first * (T - a.first)
	<
		N * (T - b.first) - (b.first) * (b.first - 1) / 2LL + b.first * (T - b.first);
}
void solve(int test) {
	int n, m;
	scanf("%d%d", &n, &m);
	N = n;
	map<long long, long long> _add, _sub;
	vector<long long> event;
	long long res = 0;
	for (int i = 0; i < m; i++) {
		long long p, s, o;
		cin >> s >> o >> p;
		_add[s] += p;
		_sub[o] += p;
		long long q = n * (o - s);
		q += o * (o - 1) / 2LL;
		q -= s * (s - 1) / 2LL;
		q += s * (o - s);
		res = add(res, mult(p, q));
		event.pb(s);
		event.pb(o);
	}	
	//eprintf("res = %lld\n", res);
	long long res0 = 0;
	sort(all(event));
	event.resize(unique(all(event)) - event.begin());
	vector<pair<long long, long long> > mans;
	for (int i = 0; i < sz(event); i++) {
		mans.pb(mp(event[i], _add[event[i]]));
		T = event[i];
		sort(all(mans), cmpT);
		for (int j = 0; j < sz(mans) && _sub[T] >= 0; j++) {
		   long long cnt = min(mans[j].second, _sub[T]);	
		   long long qq = n * (T - mans[j].first);
		   qq += T * (T - 1) / 2LL;
		   qq -= mans[j].first * (mans[j].first - 1) / 2LL;
		   qq += mans[j].first * (T - mans[j].first);
		   mans[j].second -= cnt;
		   _sub[T] -= cnt;
		   res0 = add(res0, mult(cnt, qq));
		}
	}
	//eprintf("res0 = %lld\n", res0);
	printf("Case #%d: %lld\n", test, add(res, mode - res0)); 
}

int main(){
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		solve(test);
	}	
	return 0;
}
