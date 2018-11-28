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

int TC;
int M_str, N_srv;
int nodes, cnt;

void brute(vector<vi> & buckets, const vs &str, int p) {
	if (p == M_str) {
		FOR(s,0,N_srv) if (sz(buckets[s]) < 1) return;
		int nd = N_srv;
		FOR(s,0,N_srv) {
			vs data;
			data.reserve(sz(buckets[s]));
			for (int i : buckets[s]) data.pb(str[i]);
			sort(all(data));
			nd += sz(data[0]);
			FOR(i,1,sz(data)) {
				int same = 0;
				int ma = max(sz(data[i-1]), sz(data[i]));
				while (same < ma && data[i-1][same] == data[i][same]) same++;
				nd += sz(data[i]) - same;
			}
		}
		if (nd > nodes) {
			nodes = nd;
			cnt = 1;
		} else if (nd == nodes) {
			cnt++;
		}
		return;
	}
	FOR(i,0,N_srv) {
		buckets[i].pb(p);
		brute(buckets, str, p+1);
		buckets[i].pop_back();
	}
}

int main() {
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> M_str >> N_srv;
		vs str (M_str);
		FOR(m,0,M_str) cin >> str[m];
		nodes = 0;
		cnt = 0;

		vector<vi> buckets (N_srv);
		brute(buckets, str, 0);

		cout << "Case #" << tc << ": " << nodes << " " << cnt << endl;
	}
}
