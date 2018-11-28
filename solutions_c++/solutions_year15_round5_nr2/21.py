#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define MOD
#define ADD(X,Y) ((X) = ((X) + (Y)%MOD) % MOD)
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;

int T;
int N, K, S[1010];
int df[1010];

int srMax[1010], srMin[1010], W[1010];

i64 imod(i64 a, int b)
{
	if (a >= 0) return a % b;
	return (b - (-a) % b) % b;
}

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;){
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N - K + 1; ++i) scanf("%d", S + i);

		for (int i = 1; i < N - K + 1; ++i) {
			df[i - 1 + K] = S[i] - S[i - 1];
		}

		for (int i = 0; i < K; ++i) {
			srMax[i] = 0; srMin[i] = 0;
			int cur = 0;
			for (int j = i + K; j < N; j += K) {
				cur += df[j];
				srMax[i] = max(srMax[i], cur);
				srMin[i] = min(srMin[i], cur);
			}
			// printf("%d %d: %d / %d\n", N, i, srMax[i], srMin[i]);
		}

		i64 srs = S[0];
		for (int i = 0; i < K; ++i) {
			// printf("%d %d\n", srMax[i], srMin[i]);
			int width = srMax[i] - srMin[i];
			W[i] = width;

			srs += srMin[i];
		}

		int wMax = 0;
		for (int i = 0; i < K; ++i) wMax = max(wMax, W[i]);

		int ret = wMax;
		int req = (int) imod(srs, K);
		for (int i = 0; i < K; ++i) req -= wMax - W[i];
		if (req > 0) ++ret;

		printf("Case #%d: %d\n", t, ret);
	}

	return 0;
}
