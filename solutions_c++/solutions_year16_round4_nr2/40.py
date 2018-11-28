#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <tuple>
using namespace std;
typedef long long LL;
typedef function<int(int)> VALF;

#define pb push_back
#define mt make_tuple
#define SZ(V) ((int)((V).size()))

const double ep = 1.0e-8;
double P[200];

double R[401], nR[401], tR[401], mR[401];
const int ZERO = 200;
bool used[401];
void go(double p) {
	for (int k = 0; k <= 400; k++) nR[k] = 0.0;
	for (int k = 1; k < 400; k++) {
		nR[k + 1] += R[k] * p;
		nR[k - 1] += R[k] * (1 - p);
	}
	for (int k = 0; k <= 400; k++) {
		if (nR[k] > 1.0) {
			k = k;
		}
		R[k] = nR[k];
	}
}
void rev(double p) {
	for (int k = 0; k <= 400; k++) {
		tR[k] = 0.0;
		mR[k] = 0.0;
	}
	if (1 - p > ep) {
		for (int k = 0; k < 399; k++) {
			if (1 - p > ep) {
				tR[k + 1] += (R[k] - mR[k]) / (1 - p);
			}
			if (p > ep) {
				mR[k + 2] += tR[k + 1] * p;
			}
		}
	}
	else {
		for (int k = 1; k <= 400; k++) {
			tR[k - 1] = R[k];
		}
	}
	for (int k = 0; k <= 400; k++) {
		if (R[k] > 1.0) {
			k = k;
		}
		R[k] = tR[k];
	}
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out.2", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, K;
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; i++) {
			scanf("%lf", &P[i]);
//			used[i] = false;
		}
		sort(P, P + N);
		
		double sol = 0.0;
		for (int i = 0; i <= K; i++) {
			for (int k = 0; k <= 400; k++) R[k] = 0.0;
			R[ZERO] = 1.0;
			for (int j = 0; j < i; j++) {
				go(P[j]);
			}
			for (int j = 0; j < K - i; j++) {
				go(P[N-1-j]);
			}
			sol = max(sol, R[ZERO]);
		}
		/*
		int soli = 0;
		for (int i = 0; i < (1<<N); i++) {
			vector<double> pr;
			for (int j = 0; j < N; j++) {
				if (i & (1 << j)) pr.push_back(P[j]);
			}
			if (pr.size() == K) {
				for (int k = 0; k <= ZERO*2; k++) R[k] = 0.0;
				R[ZERO] = 1.0;
				for (int j = 0; j < K; j++) {
					for (int k = 0; k <= ZERO*2; k++) nR[k] = 0.0;
					for (int k = 1; k < ZERO*2; k++) {
						nR[k - 1] += R[k] * pr[j];
						nR[k + 1] += R[k] * (1-pr[j]);
					}
					for (int k = 0; k <= ZERO*2; k++) R[k] = nR[k];
				}
				if (sol <= R[ZERO]) {
					sol = max(sol, R[ZERO]);
					soli = i;
				}
			}
		}
		*/
		/*
		for (int k = 0; k < K;k+=2) {
			double mx = -1.0;
			int mxi, mxj;
			mxi = mxj = -1;
			for (int i = 0; i < N; i++) {
				for (int j = i+1; j < N; j++) {
					if (used[i] || used[j]) continue;
					double p = P[i];
					double q = P[j];
					double cand = R[ZERO - 2] * p*q +
						R[ZERO] * (p*(1 - q) + q*(1 - p)) +
						R[ZERO + 2] * (1 - p)*(1 - q);
					if (cand > mx) {
						mx = cand;
						mxi = i;
						mxj = j;
					}
				}
			}
			used[mxi] = used[mxj] = true;
			double p = P[mxi];
			double q = P[mxj];
			for (int i = 0; i <= 400; i++) nR[i] = 0.0;
			for (int i = 2; i < 399; i++) {
				nR[i + 2] += R[i] * p * q;
				nR[i] += R[i] * (p*(1 - q) + q*(1 - p));
				nR[i - 2] += R[i] * (1 - p)*(1 - q);
			}
			for (int i = 0; i <= 400; i++) R[i] = nR[i];
		}
		while (1) {
			bool found = false;
			for (int i = 0; i < N; i++) {
				if (used[i]) {
					for (int j = 0; j < N; j++) {
						if (!used[j]) {
							double p = P[i];
							double q = P[j];
							for (int k = 0; k <= 400; k++) {
								tR[k] = 0.0;
								mR[k] = 0.0;
								nR[k] = 0.0;
							}
							for (int k = 0; k < 399; k++) {
								if (1-p > ep) {
									tR[k + 1] += (R[k] - mR[k]) / (1-p);
								}
								if (p > ep) {
									mR[k + 2] += tR[k + 1] * p;
								}
							}
							for (int k = 1; k < 400; k++) {
								nR[k + 1] += tR[k] * q;
								nR[k - 1] += tR[k] * (1-q);
							}
							if (nR[ZERO] > R[ZERO] + ep) {
								if (nR[ZERO] > 1.0 + ep) {
									i = i;
								}
								for (int k = 0; k <= 400; k++) R[k] = nR[k];
								used[i] = false;
								used[j] = true;
								found = true;
								break;
							}
						}
					}
					if (found) break;
				}
			}
			if (!found) break;
		}
		*/
		printf("Case #%d: %.16f\n", tc, sol);
		/*
		for (int i = 0; i < N; i++) {
			if (soli & (1 << i)) printf("1");
			else printf("0");
		}
		printf("\n");
		*/
	}
	return 0;
}