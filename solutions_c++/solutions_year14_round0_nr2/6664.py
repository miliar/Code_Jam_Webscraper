#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>
#include <deque>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define sqr(x) ((x) * (x))
#define len(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define endl '\n'

#ifdef CUTEBMAING
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) ({})
#endif

using namespace std;

typedef long long int64;
typedef unsigned long long lint;
typedef long double ld;

const int inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);

int main(){
	int T; cin >> T;
	for (int t = 0; t < T; t++){
		printf("Case #%d: ", t + 1);
		ld c, f, x; cin >> c >> f >> x;
		c /= 2, f /= 2, x /= 2;
		ld ans = INFINITY, curTime = 0, curCount = 0, curSpeed = 1;
		for (int count = 0; curTime < ans; count++){
			ans = min(ans, curTime + max((ld) 0, x - curCount) / curSpeed);
			ld timeShift = max((ld) 0, c - curCount) / curSpeed;
			curTime += timeShift;
			curCount += timeShift * curSpeed - c;
			curSpeed += f;
		}
		printf("%.7lf\n", (double) ans);
		eprintf("Case #%d: OK!\n");
	}
    return 0;
}
