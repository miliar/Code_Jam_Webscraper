#include <stdio.h>
#include <algorithm>
#define EPS 1.0e-9
using namespace std;

double naomi[1010], ken[1010];
pair<double, int> all[2010];

int cmp(double a, double b) {
	if (a - b >= -EPS && a - b <= EPS) return 0;
	if (a < b) return -1;
	return 1;
}

int main() {
	int T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		int N;
		scanf(" %d", &N);
		for (int i=0; i < N; i++) {
			scanf(" %lf", &naomi[i]);
			all[i] = make_pair(naomi[i], -1);
		}
		for (int i=0; i < N; i++) {
			scanf(" %lf", &ken[i]);
			all[i + N] = make_pair(ken[i], +1);
		}
		sort(naomi, naomi+N);
		sort(ken, ken+N);
		/*
		for (int i = 0; i < N; i++) {
			printf(" %f", naomi[i]);
		}
		printf("\n");
		for (int i = 0; i < N; i++) {
			printf(" %f", ken[i]);
		}
		printf("\n");
		*/
		int ansD = N;
		for (int i = 0; i < N; i++) {
			bool inv = false;
			for (int j = 0; j < N - i; j++) {
				if (cmp(naomi[i + j], ken[j]) < 0) {
					inv = true;
					break;
				}
			}
			if (!inv) {
				ansD = i;
				break;
			}
		}

		sort(all, all+2*N);
		int ansW = 0, soma = 0;
		for (int i = 0; i < 2*N; i++) {
			soma += all[i].second;
			if (soma > ansW) ansW = soma;
		}


		printf("Case #%d: %d %d\n", _42, N - ansD, ansW);
	}
	return 0;
}