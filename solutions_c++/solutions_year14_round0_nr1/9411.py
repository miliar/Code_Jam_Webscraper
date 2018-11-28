#include <ext/algorithm>
#include <algorithm>
#include <iostream>
#include <valarray>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <ctime>
#include <cmath>
#include <queue>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for (int i = (a); i < int(n); ++i)
#define error(x) cout << #x << " = " << (x) << endl;
#define all(n) (n).begin(), (n).end()
#define Size(n) ((int)(n).size())
#define mk make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef complex<double> point;

template <class P, class Q> void smin(P &a, Q b) { if (b < a) a = b; } 
template <class P, class Q> void smax(P &a, Q b) { if (b > a) a = b; } 
template <class P, class Q> bool in(const P &a, const Q &b) { return a.find(b) != a.end(); }

int main() {
	ios_base::sync_with_stdio(false);

	int tc;
	cin >> tc;

	FOR(tn, 1, tc+1) {
		int a1, a2;
		cin >> a1;
		int row1[17];
		FOR(i, 0, 4) FOR(j, 0, 4) {
			int x;
			cin >> x;
			row1[x] = i+1;
		}
		cin >> a2;
		int row2[17];
		FOR(i, 0, 4) FOR(j, 0, 4) {
			int x;
			cin >> x;
			row2[x] = i+1;
		}
		multimap<pii, int> mp;
		FOR(i, 1, 17) mp.insert(make_pair(pii(row1[i], row2[i]), i));
		pii w(a1, a2);
		cout << "Case #" << tn << ": ";
		if (mp.count(w) == 0)
			cout << "Volunteer cheated!" << endl;
		else if (mp.count(w) > 1)
			cout << "Bad magician!" << endl;
		else 
			cout << mp.find(w)->second << endl;
	}

	return 0;
}

