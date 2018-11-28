#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long Int64;

const int maxm = 100000;
const int mod = 1000002013;
const int inf = 0x7fffffff;

int xar[maxm];
int segments[maxm][3];
int sum[maxm];
int N, M, lx;

int Cost(int D) {
	return ((Int64)N * D - ((Int64)D * D - D) / 2) % mod;
}

int Form(int v) {
	v = v % mod;
	if (v < 0) v += mod;
	return v;
}

int Locate(int x) {
	return lower_bound(xar, xar + lx, x) - xar;
}

void Init() {
	scanf("%d %d", &N, &M);
	lx = 0;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < 3; j++)
			scanf("%d", &segments[i][j]);
		xar[lx++] = segments[i][0];
		xar[lx++] = segments[i][1];
	}
	sort(xar, xar + lx);
	lx = unique(xar, xar + lx) - xar;
	for (int i = 0; i < lx - 1; i++)
		sum[i] = 0;
	//printf("lx = %d\n", lx);
	for (int i = 0; i < M; i++) {
		int left = Locate(segments[i][0]);
		int right = Locate(segments[i][1]);
		for (int j = left; j < right; j++)
			sum[j] += segments[i][2];
	}
	//printf("here\n");
}

int Calc(int head, int tail, int base) {
	if (head >= tail) return 0;
	int m = inf, pos = -1;
	for (int i = head; i < tail; i++)
		if (sum[i] < m) {
			m = sum[i];
			pos = i;
		}
	int cnt = m - base;
	int cost = (Int64)Cost(xar[tail] - xar[head]) * cnt % mod;
	int left = Calc(head, pos, m);
	int right = Calc(pos + 1, tail, m);
	return Form(Form(left + cost) + right);
}

void Work() {
	int original = 0;
	for (int i = 0; i < M; i++) {
		int dist = segments[i][1] - segments[i][0];
		int cost = (Int64)Cost(dist) * segments[i][2] % mod;
		original = Form(original + cost);
	}
	printf("%d\n", Form(original - Calc(0, lx - 1, 0)));
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		Init();
		Work();
	}
	return 0;
}