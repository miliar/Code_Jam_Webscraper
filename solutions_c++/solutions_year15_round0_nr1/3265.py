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
#define FORIT(i,c) for(__typeof__((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back

int main() {
	int tc;
	cin >> tc;
	FOR(i, 0, tc) {
		int smax;
		cin >> smax;
		string s;
		cin >> s;
		int add = 0, cur = 0;
		FOR(j, 0, smax+1) {
			if (cur >= j) {
			} else {
				if (s[j] > '0') {
					add += (j - cur);
					cur += (j - cur);
				} else {
				}
			}
			cur += s[j]-'0';
		}
		cout << "Case #" << i+1 << ": " << add << endl;
	}

	return 0;
}
