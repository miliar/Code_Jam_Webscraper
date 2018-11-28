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
#define pb push_back

bool isPal(int i) {
	char c[100];
	snprintf(c, 100, "%d", i);
	FOR(i, 0, strlen(c) / 2) if (c[i] != c[strlen(c)-i-1]) return false;
	return true;
}

bool is(int i) {
	return isPal(i) && ((int) sqrt(i)) * ((int) sqrt(i)) == i && isPal((int) sqrt(i));
}

int main() {
	int tc;
	cin >> tc;
	int list[1000];
	int pos = 0;
	FOR(i, 1, 1000) {
		if (is(i)) list[pos++] = i;
	}
	FOR(t, 0, tc) {
		int a, b;
		cin >> a >> b;
		printf("Case #%d: %ld\n", t+1, upper_bound(list, list + pos, b) - lower_bound(list, list + pos, a));
	}
	return 0;
}



