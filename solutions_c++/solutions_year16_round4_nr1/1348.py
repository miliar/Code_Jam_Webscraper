#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
static const double PI2 = 8.0 * atan(1.0);

#define REP(i,n)	for(int i=0;i<(int)n;++i)
#define ALL(c)		(c).begin(),(c).end()
#define CLEAR(v)	memset(v,0,sizeof(v))
#define MP(a,b)		make_pair((a),(b))
#define ABS(a)		((a)>0?(a):-(a))
#define FOR(i,s,n)	for(int i=s;i<(int)n;++i)

void solve() {
	int N, R, P, S;
	cin >> N >> R >> P >> S;
	int n2 = (1 << N);
	REP(i, 3) {
		string l;
		switch (i) {
		case 0: l = "R"; break;
		case 1: l = "P"; break;
		case 2: l = "S"; break;
		}
		int li = 0;
		REP(j, N) {
			string b = l;
			l = "";
			REP(k, b.size()) {
				switch (b[k]) {
				case 'R': l += "RS"; break;
				case 'P': l += "PR"; break;
				case 'S': l += "PS"; break;
				}
			}
		}
		int r = 0, p = 0, s = 0;
		REP(j, l.size()) {
			switch (l[j]) {
			case 'R': ++r; break;
			case 'P': ++p; break;
			case 'S': ++s; break;
			}
		}
		if (r == R && p == P && s == S) {
			vector<string> res;
			res.assign(l.size(), ".");
			REP(j, l.size()) res[j][0] = l[j];
			int w = 2;
			REP(j, N) {
				for (int k = 0; k < n2; k += w) {
					if (res[k] < res[k + w / 2]) res[k] = res[k] + res[k + w / 2];
					else res[k] = res[k + w / 2] + res[k];
				}
				w *= 2;
			}
			cout << res[0] << endl;
			break;
		}
		if (i == 2) {
			cout << "IMPOSSIBLE" << endl;
			break;
		}
	}
}

int main(int argc, char **argv) {
	int T;
	cin >> T;
	REP(i, T) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
	return 0;
}
