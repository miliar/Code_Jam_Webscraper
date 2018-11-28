#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
//#include <unordered_set>
//#include <unordered_map>

using namespace std;

int n, k;
double P[201], SEL[201];

double F[201][201];

int main(){
	int T;
	scanf("%d", &T);
	for(int CC=1;CC<=T;++CC) {
		scanf("%d%d", &n, &k);
		for(int i=1;i<=n;i++)
			scanf("%lf", &P[i]);
		double *link = P+1;
		sort(link, link+n);
		double best = 0.0;
		for(int i=0;i<=k;i++) {
			int m = 0;
			for(int j=1;j<=i;j++)
				SEL[++m] = P[j];
			for(int j=1;j<=k-i;j++)
				SEL[++m] = P[n-j+1];
			F[0][0] = 1.0;
			for(int i=1;i<=k;i++)
				for(int j=0;j<=i;j++) {
					F[i][j] = 0.0;
					if (j>=1)
						F[i][j] += F[i-1][j-1] * SEL[i];
					F[i][j] += F[i-1][j] * (1.0 - SEL[i]);
				}
			best = max(best, F[k][k/2]);
		}
		printf("Case #%d: %lf\n", CC, best);
	}
	return 0;
}

