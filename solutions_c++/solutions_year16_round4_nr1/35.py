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
int poss[13][4097][4097];

void init() {
	assert(scanf("%d", &CASES) == 1);
	memset(poss, -1, sizeof(poss));
}

int dprintf(const char *err, ...) { 
	if (debug) {
		va_list pvar;
		va_start(pvar, err);
		return vfprintf(stderr, err, pvar);
	}
	return 0;
}

int Poss(int N, int P, int R, int S) {
	if (!N) return true;
	assert(P+R+S == (1<<N));
	int &res = poss[N][P][R];
	if (res == -1) {
		// PS = P-PR, RS = R-PR
		// PS+RS = S
		// => P+R-S = 2*PR
		int PR = (P+R-S)/2;
		int PS = P-PR;
		int RS = R-PR;
		if (PR < 0 || PS < 0 || RS < 0) return false;
		res = Poss(N-1, PR, RS, PS);
	}
	return res;
}

void solve(int Case) {
	int N, R, P, S;
	scanf("%d%d%d%d", &N, &R, &P, &S);
	if (!Poss(N, R, P, S)) {
		printf("Case #%d: IMPOSSIBLE\n", Case);
		return;
	}
	assert(P+R+S == (1<<N));
	assert((P+R-S) % 2 == 0);
	vector<string> pools[3];
	for (int i = 0; i < P; ++i)
		pools[0].push_back("P");
	for (int i = 0; i < R; ++i)
		pools[1].push_back("R");
	for (int i = 0; i < S; ++i)
		pools[2].push_back("S");
	while (N--) {
		int PR = (P+R-S)/2;
		int PS = P-PR;
		int RS = R-PR;
		vector<string> npools[3];
		for (int i = 0; i < 3; ++i)
			sort(pools[i].begin(), pools[i].end(), greater<string>());

		P = R = S = 0;
		int vals[3] = {RS, PS, PR}, tot = PR+PS+RS;
		dprintf("go tot %d\n", tot);
		while (tot--) {
			int bi = -1;
			string best = "X";
			for (int i = 0; i < 3; ++i) {
				dprintf("%d %d %d\n", vals[i], pools[(i+1)%3].empty(), pools[(i+2)%3].empty());
				if (vals[i] > 0 && !pools[(i+1)%3].empty() && !pools[(i+2)%3].empty()) {
					string x = pools[(i+1)%3].back();
					string y = pools[(i+2)%3].back();
					if (x > y) swap(x, y);
					x += y;
					dprintf("i %d cand %s\n", i, x.c_str());
					if (x < best) {
						bi = i;
						best = x;
					}
				}
			}
			assert(best != "X");
			--vals[bi];
			npools[(bi+1)%3].push_back(best);
		}
		
		for (int i =0 ; i< 3; ++i) pools[i] = npools[i];
		P = PR;
		R = RS;
		S = PS;
	}
	string ret;
	for (int i = 0; i < 3; ++i)
		if (!pools[i].empty()) ret = pools[i].front();
	printf("Case #%d: %s\n", Case, ret.c_str());
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
