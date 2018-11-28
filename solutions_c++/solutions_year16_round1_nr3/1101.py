#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;


int N;
int F[2000];
int adj[2000][2000];
int degree[2000];
int marked[2000];

void read() {
	scanf("%d", &N);
	
	memset(degree, 0, sizeof(degree));

	for (int i = 1; i <= N; i++) {
		scanf("%d", &F[i]);
		adj[F[i]][degree[F[i]]++] = i;
	}
}

int go(int node, int parent) {
	int longest = 0;
	for (int i = 0; i < degree[node]; i++) {
		if (adj[node][i] != parent) {
			longest = max(longest, go(adj[node][i], node));
		}
	}
	return longest + 1;
}

void process() {
	int best = 0;
	memset(marked, 0, sizeof(marked));

	for (int i = 1; i <= N; i++) {
		if (marked[i] == 0) {
			int j = i;
			while (!marked[j]) {
				marked[j] = i;
				j = F[j];
			}

			if (marked[j] == i) {
				int k = j;
				int size_cycle = 0;
				do {
					size_cycle++;
					k = F[k];
				} while (k != j);

				if (best < size_cycle) {
					best = size_cycle;
				}	
			}		
		}
	}

	int total = 0;
	for (int i = 1; i <= N; i++) {
		if (i < F[i] && F[F[i]] == i) {
			total += go(i, F[i]) + go(F[i], i);
		}
	}
	if (total > best) {
		best = total;
	}
	printf("%d\n", best);
}

int main() {
	
	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);

		read();
		process();
	}

	return 0;
}
