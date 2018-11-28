#include <bits/stdc++.h>
using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef set<string> ss;
typedef set<pii> spii;

const double pi = 2.0*acos(0.0);

int CASES;

void init() {
	assert(scanf("%d", &CASES) == 1);
}

int dprintf(const char *err, ...) { 
	if (debug) {
		va_list pvar;
		va_start(pvar, err);
		return vfprintf(stderr, err, pvar);
	}
	return 0;
}


string mood;
int best[20010][20010];

int Best(int l, int r) {
	if (l == r) return 0;
	int &ret = best[l][r];
	if (ret == -1) {
		ret = 0;
		for (int m = l+2; m <= r; m += 2) {
			ret = max(ret, Best(l+1, m-1) + (mood[l] == mood[m-1] ? 10 : 5) + Best(m, r));
		}
		//		printf("ret %d %d = %d\n", l, r, ret);
	}
	return ret;
}

void solve(int P) {
	cin >> mood;
	memset(best, -1, sizeof(best));
	if (mood.size() % 2) mood.pop_back();
	//	printf("go\n");
	printf("Case #%d: %d\n", P, Best(0, mood.size()));
}

int main(void) {
	init();
	for (int i = 1; i <= CASES; ++i) {
		solve(i);
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
