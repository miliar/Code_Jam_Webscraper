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
#include <unordered_map>
#include <unordered_set>
#include <tuple>
#include <bitset>
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
#define mp make_pair
#define pb push_back
#define has(c,i) ((c).find(i) != (c).end())
#define DBG(...) { if(1) fprintf(stderr, __VA_ARGS__); }
#define DBGDO(X) { if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; }

int main() {
	int TC; cin >> TC;
	FOR(tc, 1, TC+1) {
		set<int> possible[2];
		FOR(p,0,2) {
			int row; cin >> row;
			FOR(r,1,5) FOR(c,1,5) {
				int tmp; cin >> tmp;
				if (r == row) {
					possible[p].insert(tmp);
				}
			}
		}

		vi res;
		set_intersection(all(possible[0]), all(possible[1]),
			back_inserter(res));

		string answer = sz(res) == 1 ? to_string(res[0])
			          : sz(res) > 1  ? "Bad magician!"
					  :                "Volunteer cheated!";
		
		cout << "Case #" << tc << ": " << answer << endl;
	}
}
