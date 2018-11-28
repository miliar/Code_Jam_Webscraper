#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

int n;
int testing;
int can[31][31];
int can2[31][31];
int match[31];
int seen[31];

void read() {
	scanf("%d", &n);
	REP(i,n) REP(j,n) {
		char c;
		scanf(" %c", &c);
		can[i][j] = c-'0';
	}
}

bool bpm(int v) {
	if (seen[v]) return false;
	seen[v] = 1;

	for (int i = 0; i < n; i++) if (can2[v][i] && can2[testing][i]) {
		if (match[i] == -1 || bpm(match[i])) {
			match[i] = v;
			return true;
		}
	}

	return false;
}

bool ok() {
	for (testing = 0; testing < n; testing++) {
		int sz = 0;
		REP(i,n) if (can2[testing][i]) sz++;
		
		int bsz = 0;
		memset(match,-1,sizeof(match));
		REP(i,n) if (i != testing) {
			memset(seen,0,sizeof(seen));
			if (bpm(i)) bsz++;
		}

		//printf("%d %d\n", bsz, sz);
		if (bsz == sz) return false;
	}

	return true;
}

void solve() {
	int nn = n*n;
	int a = n*n;

	for (int i = 0; i < (1<<nn); i++) {
		int d = 0;
		bool good = true;
		
		REP(p,n) REP(q,n) can2[p][q]=0;

		REP(j, n*n) {
			int p = j/n;
			int q = j%n;
			can2[p][q] = !!(i & (1<<j));

			if (!can2[p][q] && can[p][q]) good = false;
			d += (can2[p][q] != can[p][q]);
		}

		if (good && ok()) {
			/*if (d < a) {
				//printf("i=%d is good\n", i);
				REP(p,n) {
					REP(q,n) printf("%d ", can2[p][q]);
					printf("\n");
				}
			}*/
			a = min(a, d);
		}
	}

	printf("%d\n", a);
}


























int myMod = 0;
int howMany = 1;

int main(int argc, char** argv) {
	if (argc > 1) {
		stringstream ss; ss << argv[1]; ss >> myMod;
		ss.str(""); ss.clear();
		ss << argv[2]; ss >> howMany;
	}

	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		read();
		if (i % howMany == myMod) {
			printf("Case #%d: ", i+1);
			solve();
		}
	}
}