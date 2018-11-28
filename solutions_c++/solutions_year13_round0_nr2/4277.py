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
//evtl noch: mp fuer make_pair, pb fuer push_back

int main() {
	int tc;
	cin >> tc;
	FOR(t, 0, tc) {
		int n, m;
		cin >> n >> m;
		int arr[n][m];
		int rows[n], cols[m];
		FOR(i, 0, m) cols[i] = 0;
		FOR(i, 0, n) {
			rows[i] = 0;
			FOR(j, 0, m) {
				
				cin >> arr[i][j];
				rows[i] = max(rows[i], arr[i][j]);
				cols[j] = max(cols[j], arr[i][j]);
			}
		}
		bool b = true;
		FOR(i, 0, n) {
			FOR(j, 0, m) {
				if (rows[i] > arr[i][j] && cols[j] > arr[i][j]) {
					b = false;
					break;
				}
			}
			if (!b) break;
		}
		if (b) printf("Case #%d: YES\n",t+1);
		else printf("Case #%d: NO\n", t+1);
	}
	return 0;
}



