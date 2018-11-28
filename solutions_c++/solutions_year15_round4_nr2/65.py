
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <cassert>
#include <unordered_set>
#include <unordered_map>
#include <fstream>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)

ll getLL(double v){
	return (ll) (v * 10000 + 0.5);
}

ll F[128];
ll T[128];
void calc(){
	int N;
	ll V, AT;
	long double VD, XD;
	cin >> N >> VD >> XD;
	V = getLL(VD);
	AT = getLL(XD);
	vector<pair<ll, ll> > inputs;
	FOR(i,0,N){
		long double a, b;
		cin >> a >> b;
		inputs.pb(mp(getLL(b) - AT, getLL(a)));
	}
	sort(all(inputs));
	ll v_mul_t = 0;
	ll sum_v = 0;
	if(inputs[0].first > 0 || inputs[N-1].first < 0){
		cout << "IMPOSSIBLE\n";
		return;
	}
	FOR(i,0,N){
		v_mul_t += inputs[i].first * inputs[i].second;
		sum_v += inputs[i].second;
	}
	if(v_mul_t > 0){
		v_mul_t *= -1;
		FOR(i,0,N)inputs[i].first *= -1;
	}
	sort(all(inputs));
	FOR(i,0,N){
		if(v_mul_t == 0){
			printf("%.12lf\n" , V / (double) sum_v);
			return;
		}
		assert(inputs[i].first < 0);
		v_mul_t -= inputs[i].first * inputs[i].second;
		sum_v -= inputs[i].second;
		if(v_mul_t > 0){
			double t_cur = inputs[i].first;
			// v_mul_t + v_cur * t_cur = 0
			double v_cur = -v_mul_t / (double)(t_cur);
			assert(-eps < v_cur);
			assert(v_cur <= inputs[i].second + eps);
			printf("%.12lf\n", V / (sum_v + v_cur));
			return;
		}
	}
	assert(false);
}

int main() {
	int TC;
	cin >> TC;
	FOR(tc, 1, TC + 1){
		cout << "Case #" << tc << ": ";
		calc();
	}
	return 0;
}
