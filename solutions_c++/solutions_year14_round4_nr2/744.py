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
#include <iomanip>
#include <cassert>
#include <unordered_set>
#include <unordered_map>
#include <tuple>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define has(c,i) ((c).find(i) != (c).end())
#define DBG(...) do { if(1) fprintf(stderr, __VA_ARGS__); } while(0)
#define DBGDO(X) do { if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; } while(0)

const int maxN = 1000;
int TC;
int N;

int bit[maxN+2];

void init() {
	fill_n(bit, N+2, 0);
}

void add(int i, int v) {
	for (++i; i <= N+1; i += i & -i) bit[i] += v;
}
int get_cumu(int i) {
	int res = 0;
	for (++i; i; i -= i & -i) res += bit[i];
	return res;
}
int get_interv(int a, int b) {
	return get_cumu(b) - get_cumu(a-1);
}


int main() {
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> N;
		vi input (N);
		FOR(i,0,N) cin >> input[i];

		vi sorted_in = input;
		sort(all(sorted_in));
		map<int,int> compr;
		FOR(i,0,N) compr[sorted_in[i]] = i;
		FOR(i,0,N) input[i] = compr[input[i]];

		vi pos(N);
		FOR(i,0,N) pos[input[i]] = i;

		FOR(i,0,N) add(i,1);

		int res = 0;
		FOR(v,0,N) {
			add(pos[v], -1);
			res += min(get_interv(0, pos[v]), get_interv(pos[v], N-1));
		}

		cout << "Case #" << tc << ": " << res << endl;
	}
}
