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

int hw(ll x) { return x ? (x&1)+hw(x/2) : 0; }

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


double pr[200];
int choice[200];
double phit[200][100];

double PHit(int n, int t) {
	if (!n || t > n) return t == 0;
	double &p = phit[n][t];
	if (p == 0) {
		p = pr[choice[n-1]]*PHit(n-1, t-1) + (1-pr[choice[n-1]])*PHit(n-1, t) + 1;
	}
	return p-1;
}

void solve(int P) {
	int N, K;
	scanf("%d%d", &N, &K);
	for (int i = 0; i < N; ++i)
		scanf("%lf", pr+i);
	double bpr = 0.0;
	sort(pr, pr+N);

	for (int i = 0; i <= K; ++i) {
		for (int k = 0; k < K; ++k)
			choice[k] = k < i ? k : N-K+k;
		memset(phit, 0, sizeof(phit));
		bpr = max(bpr, PHit(K, K/2));
	}
	printf("Case #%d: %.9lf\n", P, bpr, N, K);
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
