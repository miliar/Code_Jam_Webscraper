#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

void solve(int p[], int n, int total)
{
	int maxP1, maxP2, pi;

	while (total>0) {
		maxP1 = 0;
		maxP2 = -1;

		for (pi = 0; pi < n; ++pi) {
			if (p[pi] > p[maxP1])
				maxP1 = pi;
		}
		p[maxP1]--;

		if (total != 3) {
			maxP2 = 0;
			for (pi = 0; pi < n; ++pi) {
				if (p[pi] > p[maxP2])
					maxP2 = pi;
			}
		}

		printf("%c", 'A' + maxP1);
		total--;

		if (maxP2 != -1 && p[maxP2] != 0) {
			printf("%c", 'A' + maxP2);
			total--;
			p[maxP2]--;
		}
		printf(" ");
	}
	printf("\n");
}

int main()
{
	int i, j, total;
	int tcase;
	int n;
	int p[26];

	scanf("%d", &tcase);
	for(i=1; i<=tcase; ++i) {
		scanf("%d", &n);

		total = 0;
		for(j=0; j<n; ++j) {
			scanf("%d", &p[j]);
			total += p[j];
		}

		printf("Case #%d: ", i);
		solve(p, n, total);
	}
	return 0;
}
