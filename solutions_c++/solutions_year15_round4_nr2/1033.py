#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>

double R[150], C[150];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N;
		double V, X;
		scanf("%d %lf %lf", &N, &V, &X);
		for (int i=0; i<N; i++) {
			scanf("%lf %lf", &R[i], &C[i]);
		}
		for (int i=0; i<N; i++) {
			for (int j=i; j<N; j++) {
				if (C[i] > C[j]) {
					double temp = C[i];
					C[i] = C[j];
					C[j] = temp;
					temp = R[i];
					R[i] = R[j];
					R[j] = temp;
				}
			}
		}
		double Cmax = X;
		double Cmin = X;
		for (int i=0; i<N; i++) {
			Cmin = std::min(C[i], Cmin);
			Cmax = std::max(C[i], Cmax);
		}
		X -= Cmin;
		if (Cmax > Cmin) {
			X /= Cmax - Cmin;
		}
		for (int i=0; i<N; i++) {
			C[i] -= Cmin;
			if (Cmax > Cmin) {
				C[i] /= Cmax - Cmin;
			}
		}
		double Y = X * V;
		double sy = 0, sr = 0;
		for (int i=0; i<N; i++) {
			sy += C[i] * R[i];
			sr += R[i];
		}

		const double TMAX = 99999999999.;
		const double EPS = 0.00000001;
		double res = TMAX;

		bool up = false, down = false;
		for (int i=0; i<N; i++) {
			if (X >= C[i]) {
				up = true;
			}
			if (X <= C[i]) {
				down = true;
			}
		}
		if (!up || !down) {
			;
		} else {

			for (int i=0; i<N; i++) {
				double mr = 0, my = 0;
				if (sy * V / sr > Y) {
					for (int j=0; j<i; j++) {
						my += C[j] * R[j];
						mr += R[j];
					}
				} else {
					for (int j=0; j<i; j++) {
						my += C[N-j-1] * R[N-j-1];
						mr += R[N-j-1];
					}
				}
				double a, b;
				if (my*sr - mr*sy > -EPS && my*sr - mr*sy < EPS) {
					b = 0;
				} else {
					b = (Y*sr - V*sy) / (my*sr - mr*sy);
				}
				a = (V - mr*b) / sr;
				if (a < -EPS || b < -EPS || b == 0 && (a*sy-EPS > Y || a*sy+EPS < Y)) {
					;
				} else {
					res = std::min(a+b, res);
				}
			}
		}
		if (res == TMAX) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		} else {
			printf("Case #%d: %f\n", t, res);
		}
	}
	return 0;
}
