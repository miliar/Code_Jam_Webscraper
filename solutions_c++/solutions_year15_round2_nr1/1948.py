#include <bits/stdc++.h>

using namespace std;

#define MAXN 10001000

typedef struct graph{
	vector<int> v;
	bool used;
	int dist;
} graph;

graph g[MAXN];
int reversed[MAXN];
queue<int> myq;

void mountReverse() {
	int v[8];
	for (int i = 1; i <= 9; i++) {
		reversed[i] = i;
		//printf("reversed %d = %d\n", i, reversed[i]);
	}
	for (int i = 10; i < MAXN; i++) {
		int a = i;
		int b = 0;
		while (a) {
			v[b] = a%10;
			a /= 10;
			b++;
		}
		int res = 0;
		for (int j = 0; j < b; j++) {
			res *= 10;
			res += v[j];
		}
		reversed[i] = res;
		//printf("reversed %d = %d\n", i, reversed[i]);
	}
}


void solve() {
	mountReverse();
	myq.push(1);
	g[1].used = true;
	g[1].dist = 1;
	while (!myq.empty()) {
		int p = myq.front();
		myq.pop();
		if (p+1<MAXN && !g[p+1].used) {
			g[p+1].used = true;
			g[p+1].dist = g[p].dist + 1;
			myq.push(p+1);
		}
		if (reversed[p] < MAXN && !g[reversed[p]].used ) {
			g[reversed[p]].used = true;
			g[reversed[p]].dist = g[p].dist + 1;
			myq.push(reversed[p]);
		}
	}
}

int main() {
	int t;
	solve();
	scanf("%d", &t);
	for (int z = 1; z <= t; z++) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", z, g[n].dist);
	}
	return 0;
}
