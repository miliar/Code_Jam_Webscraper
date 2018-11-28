#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int N, M;
int a[100][100];
int b[100][100];

int maxH(int i)
{
	int h = -1;
	for (int j = 0; j < M; ++j) {
		if (a[i][j] > h) h = a[i][j];
	}
	return h;
}

int maxV(int j)
{
	int h = -1;
	for (int i = 0; i < N; ++i) {
		if (a[i][j] > h) h = a[i][j];
	}
	return h;
}

bool check()
{
	for (int i = 0; i < N; ++i) {
		int h = maxH(i);
		for (int j = 0; j < M; ++j) {
			if (a[i][j] == h) b[i][j] = 1;
		}
	}

	for (int j = 0; j < M; ++j) {
		int h = maxV(j);
		for (int i = 0; i < N; ++i) {
			if (a[i][j] == h) b[i][j] = 1;
		}
	}

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (b[i][j] == 0 && a[i][j] != 100) return false;
		}
	}

	return true;
}

int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		scanf("%d %d", &N, &M);

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				scanf("%d", &a[i][j]);
				b[i][j] = 0;
			}
		}

		printf("Case #%d: %s\n", Ti, check() ? "YES" : "NO");
	}
	return 0;
}
