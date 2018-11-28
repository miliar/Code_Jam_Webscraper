#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

string input = "A-small-attempt0.in";
string output = "A-small-attempt0.out";

int main () {
    freopen(input.data(), "r", stdin);
    freopen(output.data(), "w", stdout);
#ifdef LocalHost

#endif
    int T;
    cin >> T;
    REP (test, T) {
	int q;
	cin >> q;
	--q;
	vector<int> a(16);
	REP (i, 4) {
	    REP (j, 4) {
		int x;
		cin >> x;
		if (i == q) a[x-1]++;
	    }
	}

	int w;
	cin >> w;
	--w;
	REP (i, 4) {
	    REP (j, 4) {
		int x;
		cin >> x;
		if (i == w) a[x-1]++;
	    }
	}
	vector<int> res;
	REP (i, 16)
	    if (a[i] == 2) {
		res.pb(i+1);
	    }

	cout << "Case #" << (test + 1) << ": ";
	if (!sz(res)) {
	    cout << "Volunteer cheated!\n";
	} else if (sz(res) > 1) {
	    cout << "Bad magician!\n";
	} else {
	    cout << res.back() << endl;
	}
    }
    return 0;
}
