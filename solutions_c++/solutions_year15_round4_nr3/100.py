#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;

#define INF 1000000000
#define min(x, y) ((x) < (y) ? (x) : (y))
int T, n, len, ll, s, t;
int till[11000], kk[11000], go[110000], next[110000], D[11000], n1[110000], f[110000];
bool cc[11000];
string sss[11000];

void add(int x, int y, int z) {
	next[++len] = till[x];
	till[x] = len;
	go[len] = y;
	f[len] = z;
}

void Ad(int x, int y, int z) {
	add(x, y, z);
	add(y, x, 0);
}

bool bfs() {
	int q, h, i;
	memset(D, 0, sizeof D);
	memset(cc, 1, sizeof cc);
	for (D[n1[q = h = 1] = s] = 1; q <= h; q++)
		for (i = till[n1[q]]; i; i = next[i])
			if (f[i] && !D[go[i]])	D[n1[++h] = go[i]] = D[n1[q]] + 1;
	return D[t];
}

int dfs(int k, int mi) {
	if (k == t)	return mi;
	int i, tmp, sum = 0;
	for (i = till[k]; i && mi; i = next[i])
		if (f[i] && D[go[i]] == D[k] + 1 && cc[go[i]]) {
			tmp = dfs(go[i], min(mi, f[i]));
			sum += tmp;
			mi -= tmp;
			f[i] -= tmp;
			f[i ^ 1] += tmp;
		}
	if (!sum)	cc[k] = true;
	return sum;
}

int maxFlow() {
	int sum = 0;
	while (bfs())	sum += dfs(s, INF);
	return sum;
}

int main() {
	scanf("%d", &T);
	for (int xx = 1; xx <= T; xx++) {
		scanf("%d", &n);
		len = 1;
		memset(till, 0, sizeof till);
		s = 0; t = 1;
		ll = 0;
		getchar();
		for (int i = 1; i <= n; i++) {
			string S = "";
			bool f = false;
			int h = 0;
			while (!f) {
				char k;
				S = "";
				for (k = getchar(); ; k = getchar()) {
					if (k == ' ') break;
					if (k < 'a' && k != ' ') {
						f = true;
						break;
					}
					S += k;
				}
				// cout << S << endl;
				// printf("?? %d\n", f);
				int tt = 0;
				for (int j = 1; j <= ll; j++)
					if (sss[j] == S) tt = j;
				if (!tt) sss[++ll] = S, tt = ll;
				kk[++h] = tt;
			}
			if (i == 1) {
				for (int j = 1; j <= h; j++)
					Ad(s, kk[j] * 2, INF);
			}else if (i == 2) {
				for (int j = 1; j <= h; j++)
					Ad(kk[j] * 2 + 1, t, INF);
			}else {
				for (int j = 1; j <= h; j++)
					for (int k = 1; k <= h; k++)
						Ad(kk[j] * 2 + 1, kk[k] * 2, INF);
			}
		}
		for (int i = 1; i <= ll; i++)
			Ad(i * 2, i * 2 + 1, 1);
		printf("Case #%d: %d\n", xx, maxFlow());
	}
}
