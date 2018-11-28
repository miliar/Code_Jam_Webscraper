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

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (auto i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back

int main() {
	int tc;
	cin >> tc;
	FOR(t, 0, tc) {
		int n, s;
		cin >> n >> s;
		vector<int> v(n);
		FOR(i, 0, n) {
			int p;
			cin >> p;
			v[i] = p;
		}
		sort(all(v), std::greater<int>());
		int l = 0, r = n-1;
		int num = 0;
		while (l < r) {
			num++;
			if (v[l] + v[r] <= s) r--;
			l++;
		}
		if (l == r) num++;
		cout << "Case #" << t+1 << ": " << num << endl;
	}
}


