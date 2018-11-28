#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int Test, N, M;
int P[511], S[511];
vector<pair<double, double> > L, R;
double F[511][511], Y;

double calc()
{
	N = L.size();
	M = R.size();
	if (N == 0 || M == 0) {
		double Ret = 0;
		for (int i = 0; i < N; i ++) {
			Ret = max(Ret, L[i].second / (Y - L[i].first));
		}
		for (int i = 0; i < M; i ++) {
			Ret = max(Ret, R[i].second / (Y - R[i].first));
		}
		return Ret;
	}
	for (int i = 0; i <= N; i ++) {
		for (int j = 0; j <= M; j ++) {
			F[i][j] = 1e99;
		}
	}
	sort(L.begin(), L.end());
	reverse(L.begin(), L.end());
	sort(R.begin(), R.end());
	reverse(R.begin(), R.end());
	F[0][0] = 0;
	/*
	printf("N = %d, M = %d\n", N, M);
	for (int i = 0; i < N; i ++) {
		printf("%lf %lf\n", L[i].first, -L[i].second);
	}
	for (int i = 0; i < M; i ++) {
		printf("%lf %lf\n", R[i].first, R[i].second);
	}*/
	for (int i = 0; i <= N; i ++) {
		for (int j = 0; j <= M; j ++)
		if (F[i][j] < 1e90) {
			double t = 0;
			for (int k = i; k < N; k ++) {
				t = max(t, (L[k].first * F[i][j] + L[k].second) / (Y - L[k].first));
				F[k + 1][j] = min(F[k + 1][j], F[i][j] + t * 2.0);
			}
			t = 0;
			for (int k = j; k < M; k ++) {
				t = max(t, (R[k].first * F[i][j] + R[k].second) / (Y - R[k].first));
				F[i][k + 1] = min(F[i][k + 1], F[i][j] + t * 2.0);
			}
		}
	}
	double Ret = 1e99;
	for (int i = 0; i <= N; i ++) {
		double Res = 0.0;
		for (int j = i; j < N; j ++) {
			Res = max(Res, (L[j].first * F[i][M] + L[j].second) / (Y - L[j].first));
		}
		Ret = min(Ret, F[i][M] + Res);
	}
	for (int i = 0; i <= M; i ++) {
		double Res = 0.0;
		for (int j = i; j < M; j ++) {
			Res = max(Res, (R[j].first * F[N][i] + R[j].second) / (Y - R[j].first));
		}
		Ret = min(Ret, F[N][i] + Res);
	}
	return Ret;
}

int main(int argc, char **argv)
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
		scanf("%lf%d", &Y, &N);
		L.clear();
		R.clear();
		for (int i = 0; i < N; i ++) {
			scanf("%d", &P[i]);
		}
		for (int i = 0; i < N; i ++) {
			scanf("%d", &S[i]);
		}
		for (int i = 0; i < N; i ++) {
			if (P[i] < 0) {
				L.push_back(make_pair(S[i], -P[i]));
			} else {
				R.push_back(make_pair(S[i], P[i]));
			}
		}
		printf("Case #%d: %.12lf\n", Case, calc());
		/*
		int NM = N + M;
		if (NM <= 12) {
			int A[100];
			for (int i = 0; i < NM; i ++) {
				A[i] = i;
			}
			double Ret = 1e99;
			do {
				double now = 0.0;
				double t = 0.0;
				for (int k = 0; k < NM; k ++) {
					int i = A[k];
					double p = P[i];
					if (P[i] < 0) p -= S[i] * t;
						else p += S[i] * t;
					double d = fabs(now - p) / (Y - S[i]);
					t += d;
					if (P[i] < 0) now = P[i] - S[i] * t;
						else now = P[i] + S[i] * t;
				//	printf("%.2lf ", now);
				}
			//	printf("\n");
				Ret = min(Ret, t);
			} while (next_permutation(A, A + NM));
			printf("%.12lf\n", Ret);
			cerr << Case << " " << calc() << " " << Ret << endl;
		}
		 */
	}
	return 0;
}
