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
int N, X;

int main() {
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> N >> X;
		vi files (N);
		FOR(i,0,N) cin >> files[i];
		sort(all(files));
		vector<bool> mark(N, false);

		int res = 0;
		int j = N-1;
		FOR(i,0,N) {
			if (mark[i]) continue;
			mark[i] = true;
			while (j >= 0 && (mark[j] || files[j] + files[i] > X)) j--;
			if (j >= 0 && !mark[j]) {
				mark[j] = true;
				j--;
			}
			res++;
		}

		cout << "Case #" << tc << ": " << res << endl;;
	}
}
