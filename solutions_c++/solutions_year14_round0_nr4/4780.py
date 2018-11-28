#include <cstdio>
#include <algorithm>

#define MAXN 11

using namespace std;

int t, T, N;
int nao[MAXN], ken[MAXN];

#define FULL ((1<<N)-1)

int willWin(int a, int b){
	for (int i = 0; i < N; i++)
		if ((b & (1<<i)) && nao[a] < ken[i])
			return false;
	return true;
}

int readThing(){
	char c;
	int cnt = 0, ret = 0;

	while ((c = getchar()) != '0');
	getchar();

	for (c = getchar(); isdigit(c); c = getchar(), cnt++)
		ret = ret * 10 + c - '0';

	for (; cnt < 5; cnt++)
		ret *= 10;

	return ret;
}

int nplay[1<<MAXN][1<<MAXN], kplay[1<<MAXN][1<<MAXN];

int war(int n, int k){
	static int vis[1<<MAXN][1<<MAXN];
	static int dp[1<<MAXN][1<<MAXN];
	int i, j;

	if (!n) return 0;

	if (vis[n][k] == t) return dp[n][k];

	vis[n][k] = t;
	dp[n][k] = -1;

	for (i = 0; i < N; i++){
		if (n & (1<<i)){
			int tmp = 1<<30, tp;
			for (j = 0; j < N; j++)
				if (k & (1<<j))
					if (tmp > war(n ^ (1<<i), k ^ (1<<j)) + (nao[i] > ken[j])){
						tp = j;
						tmp = war(n ^ (1<<i), k ^ (1<<j)) + (nao[i] > ken[j]);
					}

			if (tmp > dp[n][k]){
				nplay[n][k] = i;
				kplay[n][k] = tp;
				dp[n][k] = tmp;
			}
			/*
			for (j = 0; j < N; j++)
				if (k & (1<<j))
					tmp = min(tmp, war(n ^ (1<<i), k ^ (1<<j)) + (nao[i] > ken[j]));
			dp[n][k] = max(dp[n][k], tmp);
			*/
		}
	}

	return dp[n][k];
}

int deceit(int n, int k){
	static int vis[1<<MAXN][1<<MAXN];
	static int dp[1<<MAXN][1<<MAXN];
	int i, j;

	if (!n) return 0;

	if (vis[n][k] == t) return dp[n][k];

	vis[n][k] = t;
	dp[n][k] = -1;

	for (i = 0; i < N; i++)
		if (n & (1<<i)){
			for (j = 0; j < N; j++)
				if (k & (1<<j))
					break;

			if (nao[i] > ken[j])
				dp[n][k] = max(dp[n][k], deceit(n ^ (1<<i), k ^ (1<<j)) + 1);
			
			int tmp = 1<<30;

			for (j = N-1; j >= 0; j--)
				if ((k & (1<<j)) && nao[i] < ken[j]){
					tmp = min(tmp, deceit(n ^ (1<<i), k ^ (1<<j)));
					dp[n][k] = max(dp[n][k], tmp);
				}
		}

	return dp[n][k];
}

int main(){
	scanf("%d", &T);

	for (t = 1; t <= T; t++){
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			nao[i] = readThing();
		for (int i = 0; i < N; i++)
			ken[i] = readThing();

		sort(nao, nao + N);
		sort(ken, ken + N);

		/*
		for (int i = 0; i < N; i++)
			printf("%d ", nao[i]);
		printf("\n");
		for (int i = 0; i < N; i++)
			printf("%d ", ken[i]);
		printf("\n");
		*/

		printf("Case #%d: %d %d\n", t, deceit(FULL,FULL), war(FULL,FULL));

		/*
		int n = FULL;
		int k = FULL;

		while (n){
			printf("Nao %d %c %d Ken\n", nao[nplay[n][k]], nao[nplay[n][k]] > ken[kplay[n][k]] ? '<' : '>', ken[kplay[n][k]]);
			int t = nplay[n][k], l = kplay[n][k];
			n ^= (1<<t);
			k ^= (1<<l);
		}
		*/
	}
}
