#include <cstdio>
#include <cmath>

int acts[10000];
int E, R, N;

int solution = 0;

int bestsofar[10000] = {0};

void dfs (int currentN, int currentE, int Gtotal)
{
	if (currentN == N) {
		if (Gtotal > solution)
			solution = Gtotal;
		return;
	}

	if (currentE > E)
		currentE = E;

	//if (Gtotal < bestsofar[currentN])
	//	return;

	bestsofar[currentN] = Gtotal;

	dfs(currentN+1, R, Gtotal + currentE*acts[currentN]); // spend all of current on this
	dfs(currentN+1, currentE + R, Gtotal); // spend none on this
	
	// dfs(currentN+1, currentE, Gtotal + R*acts[currentN]); // spend so that regain is more than spent
	
	
	for (int spend = 1; spend < currentE; spend++)
		dfs(currentN+1, currentE - spend + R, Gtotal + spend*acts[currentN]);
}

int main()
{
	freopen("B-small-attempt4.in", "r", stdin);
	freopen("p2.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		scanf("%d %d %d", &E, &R, &N);
		solution = 0;
		for (int n = 0; n < N; n++)
			scanf("%d", &acts[n]);

		for (int i = 0; i < N; i++)
			bestsofar[i] = 0;

		dfs(0, E, 0);
		printf("Case #%d: %d\n", t, solution);
	}

	return 0;
}