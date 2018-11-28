// Problem C. Dijkstra
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

static char s[11000];
int M[4][4] = {
	{1,  2,  3,  4},
	{2, -1,  4, -3},
	{3, -4, -1,  2},
	{4,  3, -2, -1},
};

static int vkc[11000], skc[11000];

int main(int argc, char *argv[])
{
	int T;
	scanf("%d\n", &T);
	for (int ti = 1; ti <= T; ti++) {
		bool yes = false;
		long long l, x, n;
		scanf("%lld %lld %s", &l, &x, s);
		for (long long i = 0; i < l; i++) s[i] = s[i] - 'i' + 2;
		for (long long i = 1; i < x; i++)
			for (long long j = 0; j < l; j++) s[i * l + j] = s[j];
		s[l * x] = '\0';
		n = l * x;
		int vi = 1, si = 1;
		memset(vkc, 0, sizeof(vkc));
		for (long long i = 0; i < n - 2; i++) {
			int r = M[vi - 1][s[i] - 1];
			if (r < 0) si = -si;
			vi = abs(r);
			if (vi != 2 || si < 0) continue;
			int vj = 1, sj = 1;
			for (long long j = i + 1; j < n - 1; j++) {
				int r = M[vj - 1][s[j] - 1];
				if (r < 0) sj = -sj;
				vj = abs(r);
				if (vj != 3 || sj < 0) continue;
				long long kk = j + 1;
				int vk = 1, sk = 1;
				if (vkc[kk] == 0) {
					for (long long k = j + 1; k < n; k++) {
						int r = M[vk - 1][s[k] - 1];
						if (r < 0) sk = -sk;
						vk = abs(r);
					}
					vkc[kk] = vk;
					skc[kk] = sk;
				} else {
					vk = vkc[kk];
					sk = skc[kk];
				}
				if (vk == 4 && sk > 0) yes = true;
				if (yes) break;
			}
			if (yes) break;
		}
		printf("Case #%d: %s\n", ti, yes ? "YES" : "NO");
	}
	return 0;
}
