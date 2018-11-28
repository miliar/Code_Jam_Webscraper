#include <stdio.h>
#include <iostream>
#include <queue>

using namespace std;

#define INSOMNIA "INSOMNIA"

int a[105];

void expand(int n, int num, int *a) {
	int t = 1;
	for (int i = 0; i < n; i++) {
		a[i] = (num & t) ? 1 : 0;
		t <<= 1;
	}
}

int collapse(int n, int *a) {
	int t = 0;
	for (int i = 0; i < n; i++) {
		if (a[i]) {
			t |= (1 << i);
		}
	}
	return t;
}

int flip(int n, int num, int k) {
	int a[105];
	int b[105];
	expand(n, num, a);
	for (int i = 0; i < k; i++) {
		b[i] = 1 - a[k - i - 1];
	}
	for (int i = k; i < n; i++) {
		b[i] = a[i];
	}

	return collapse(n, b);
}

queue<int> q;

int dist[100000];

int solve(char *s) {
	int n = strlen(s);

	int a[105];
	for (int i = 0; i < n; i++) {
		a[i] = (s[i] == '-') ? 0 : 1;
	}

	while (!q.empty()) q.pop();
	memset(dist, 0, sizeof(dist));

	int start = collapse(n, a);
	q.push(start);
	dist[start] = 1;

	while (!q.empty()) {
		int u = q.front(); q.pop();

		for (int i = 1; i <= n; i++) {
			int v = flip(n, u, i);
			if (dist[v] == 0) {
				dist[v] = dist[u] + 1;
				q.push(v);
			}
		}
	}

	return dist[(1 << n) - 1] - 1;
}

int main() {
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout);

	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		char s[500];
		scanf("%s", s);

		int res = solve(s);

		cout << "Case #" << (i + 1) << ": " << res << endl;
	}

	return 0;
}
