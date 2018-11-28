#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("r1A-large (1).in", "r", stdin);
	freopen("r1A-large (1).out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int N;
		scanf("%d", &N);
		int p[1001];
		for (int i = 0; i < N; i++)
			scanf("%d", &p[i]);
		int firstmethod = 0;
		for (int i = 0; i < N - 1; i++) {
			if (p[i] > p[i + 1])
				firstmethod += p[i] - p[i + 1];
		}
		int minrate = 0;
		for (int i = 0; i < N - 1; i++) {
			if (p[i] > p[i + 1])
				minrate = max(minrate, p[i] - p[i + 1]);
		}
		int secondmethod = 0;
		for (int i = 0; i < N - 1; i++) {
			if (p[i] < minrate)
				secondmethod += p[i];
			else
				secondmethod += minrate;
		}
		printf("Case #%d: %d %d\n", t + 1, firstmethod, secondmethod);
	}
	return 0;
}