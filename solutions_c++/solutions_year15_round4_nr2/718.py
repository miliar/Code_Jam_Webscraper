//*
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
#include <map>
#include <set>
#include <time.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <char, char> pcc;
typedef pair <int, char> pic;
typedef pair <int, ll> pil;
typedef pair <ll, int> pli;

const int IT_MAX = 32768;
const int MOD = 1000000007;
const int INF = 2034567891;
const ll LL_INF = 1234567890123456789ll;

pair <double, double> in[105];
bool isEqual(double x, double y) {
	if (abs(x - y) <= 1E-8) return true;
	else return false;
}

bool isLarger(double x, double y) {
	if (x - y > 1E-8) return true;
	else return false;
}
int main() {
	freopen("B-small-attempt5.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		int i, j, N;
		double V, X;
		scanf("%d %lf %lf", &N, &V, &X);
		for(i = 0; i < N; i++) scanf("%lf %lf", &in[i].second, &in[i].first);
		sort(in, in + N);

		if (N == 1) {
			if (isEqual(X, in[0].first)) printf("%lf", V / in[0].second);
			else printf("IMPOSSIBLE");
			printf("\n");
			continue;
		}

		if (isEqual(in[0].first, in[1].first)) {
			if (isEqual(X, in[0].first)) printf("%lf", V / (in[0].second + in[1].second));
			else printf("IMPOSSIBLE");
			printf("\n");
			continue;
		}

		if (isLarger(in[0].first, X) || isLarger(X, in[N - 1].first)) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		
		if (isEqual(in[0].first, X)) {
			printf("%lf\n", V / in[0].second);
			continue;
		}

		if (isEqual(in[1].first, X)) {
			printf("%lf\n", V / in[1].second);
			continue;
		}

		double V0 = (in[1].first - X) * V / (in[1].first - in[0].first);
		double V1 = (X - in[0].first) * V / (in[1].first - in[0].first);

		printf("%.20lf\n", max(V0 / in[0].second, V1 / in[1].second));
	}
	return 0;
}
//*/

