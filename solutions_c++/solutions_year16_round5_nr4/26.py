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


void solve(int P) {
	int N, L;
	cin >> N >> L;
	vector<string> G(N);
	string B;
	for (int i = 0; i < N; ++i) {
		cin >> G[i];
	}
	cin >> B;
	printf("Case #%d: ", P);
	int p = -1;
	for (int j = 0; j < N; ++j) {
		if (G[j] == B)  {
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	string P1, P2;
	for (int i = 0; i < L; ++i) {
		P1 += "0?";
		if (i)
			P2 += "1";
	}
	if (L == 1)
		P2 = "0";
	assert(P1.length() + P2.length() <= 200);
	printf("%s %s\n", P1.c_str(), P2.c_str());
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
