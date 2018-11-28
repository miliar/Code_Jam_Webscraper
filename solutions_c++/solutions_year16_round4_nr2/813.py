#include <bits/stdc++.h>
using namespace std;

#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define FOREACH(it, a) for (auto it = a.begin(); it != a.end(); ++it)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) { return (a < b) ? a : b; }
template<class T, class U> inline T tmax(T a, U b) { return (a > b) ? a : b; }
template<class T, class U> inline void amax(T &a, U b) { if (b > a) a = b; }
template<class T, class U> inline void amin(T &a, U b) { if (b < a) a = b; }
template<class T> inline T tabs(T a) { return (a > 0) ? a : -a; }
template<class T> T gcd(T a, T b) { while (b != 0) { T c = a; a = b; b = c % b; } return a; }

const int N = 205;
double p[N], ret;
vector<double> prob;

double best(int n, int k) {
	int comb = (1 << k) - 1;
	double ans = 0.0;
	while (comb < (1 << n)) {
		// process with comb
		double sx = 1.0, sy = 1.0;
		REPU(i, 0, n) {
			if (comb & (1 << i)) sx *= prob[i];
			else sy *= (1 - prob[i]);
		}
		ans += sx * sy;
		int x = comb & -comb, y = comb + x;
		comb = ((comb & ~y) / x >> 1) | y;
	}
	return ans;
}

void generate_subset(int n, int k) {
	int comb = (1 << k) - 1;
	while (comb < (1 << n)) {
		// process with comb
		prob.clear();
		REPU(i, 0, n) if (comb & (1 << i)) {
			prob.push_back(p[i]);
		}
		amax(ret, best(k, k >> 1));
		int x = comb & -comb, y = comb + x;
		comb = ((comb & ~y) / x >> 1) | y;
	}
}

int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	
	int nTest, n, k;

	cin >> nTest;
	REPU(it, 1, nTest + 1) {
		cin >> n >> k;
		REPU(i, 0, n) cin >> p[i];
		ret = 0.0;
		generate_subset(n, k);
		printf("Case #%d: %.9f\n", it, ret);
	}
	
	return 0;
}
