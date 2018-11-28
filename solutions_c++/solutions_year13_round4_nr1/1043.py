#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <utility>

using namespace std;

struct route {
	int s, e, p, len;
};

bool operator < (route &a, route &b) {
	return a.len < b.len;
}

const int MAXN = 120;

const int mod = 1000002013;
int t, n, m, snum;
long long oldp, newp;
int d[MAXN][MAXN];
vector < pair<int, int> > v;

long long getPrice(int len) {
	if (len == 0)
		return 0;
	long long sum = (len - 1);
	sum = (sum * len) / 2;
	sum %= mod;
	long long res = len; 
	res = (res * n) % mod;
	return (res - sum + mod) % mod;
}

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &t);

	for (int test = 1; test <= t; test++) {
		scanf("%d %d", &n, &m);
		for (int i = 1; i < MAXN; i++)
			for (int j = 1; j < MAXN; j++) 
				d[i][j] = 0;

		oldp = newp = 0;
		for (int i = 1; i <= m; i++) {
			int s, e, p;
			scanf("%d %d %d", &s, &e, &p);
			d[s][e] += p;
			oldp = (oldp + getPrice(e - s) * p) % mod;
		}

		for (int i = 1; i <= n; i++) 
			for (int j = n; j >= i; j--) 
				if (d[i][j])
					for (int k = 1; k < i; k++)
						for (int l = j - 1; l >= i; l--) 
							if (d[k][l]) {
								int change = min(d[i][j], d[k][l]);
								d[i][j] -= change; d[k][l] -= change;
								d[i][l] += change; d[k][j] += change;
							}

		for (int i = 1; i <= n; i++)
			for (int j = i; j <= n; j++) {
				long long add = d[i][j];
				if (add)
					add = (add * getPrice(j - i)) % mod;
				newp = (newp + add) % mod;
			}

		printf("Case #%d: %I64d\n", test, (oldp - newp + mod) % mod);
	}

	return 0;
}