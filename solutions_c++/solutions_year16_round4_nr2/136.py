#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

int n, k;
double prob[210];
double pf[210][210];
double sf[210][210];

void read() {
	scanf("%d %d", &n, &k);
	REP(i,n) scanf("%lf", &prob[i]);
}

void solve() {
	sort(prob,prob+n);

	pf[0][0] = 1;
	sf[0][0] = 1;
	
	for (int i = 0; i < n; i++) {
		for (int pick = n; pick >= 0; pick--) {
			pf[i+1][pick] = pf[i][pick] * (1-prob[i]);
			if (pick != 0) pf[i+1][pick] += pf[i][pick-1] * prob[i];

			sf[i+1][pick] = sf[i][pick] * (1-prob[n-1-i]);
			if (pick != 0) sf[i+1][pick] += sf[i][pick-1] * prob[n-1-i];
		}
	}

	double b = 0;
	for (int p = 0; p <= k; p++) {
		double th = 0;
		for (int ppick = 0; ppick <= k/2; ppick++) {
			th += pf[p][ppick] * sf[k-p][k/2 - ppick];
		}
		b = max(b,th);
	}

	printf("%.15f\n", b);
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