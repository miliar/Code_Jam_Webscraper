#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>

#define ADD(X,Y) ((X) = ((X) % MOD + (Y) % MOD) % MOD)

using namespace std;
typedef long long i64;
const int MOD = 1000000007;

i64 C[1010][1010], frac[1010];

void precalc()
{
	for(int i = 0; i < 1010; i++) C[0][i] = 0;
	C[0][0] = 1;

	for(int i = 1; i < 1010; i++) {
		C[i][0] = 1;
		for(int j = 1; j < 1010; j++) C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD;
	}

	frac[0] = 1;
	for(int i = 1; i < 1010; i++) frac[i] = (frac[i-1] * i) % MOD;
}

struct node
{
	node* child[26];
	int w;
	bool str;
};

int M, N;
char in[1010][110];
node pool[100100]; int pLast;
node *top;
node *alloc()
{
	node *ret = &(pool[pLast++]);

	for(int i = 0; i < 26; i++) ret->child[i] = NULL;

	ret->str = false;
	ret->w = 0;

	return ret;
}

void append(node *nd, char* str)
{
	for(int i = 0; str[i]; i++) {
		int v = str[i] - 'A';

		if(!nd->child[v]) nd->child[v] = alloc();

		nd = nd->child[v];
	}

	nd->str = true;
}

int calc_weight(node *nd)
{
	if(!nd) return 0;

	int ret = (nd->str ? 1 : 0);
	for(int i = 0; i < 26; i++) ret += calc_weight(nd->child[i]);

	nd->w = ret;
	return ret;
}

i64 dp[30][210];

i64 count(node *nd)
{
	if(!nd) return 1;

	if(nd->w <= N) return frac[nd->w];

	i64 ret = 1;
	for(int i = 0; i < 26; i++) ret = (ret * count(nd->child[i])) % MOD;

	vector<int> cnt;
	bool large = false;
	for(int i = 0; i < 26; i++) if(nd->child[i]) {
		cnt.push_back(nd->child[i]->w);
		if(nd->child[i]->w >= N) large = true;
	}

	if (large) {
		for(int i = 0; i < cnt.size(); i++) {
			if(cnt[i] < N) ret = (ret * C[N][cnt[i]]) % MOD;
		}

		if(nd->str) ret = (ret * N) % MOD;

		return ret;
	}

	if(nd->str) cnt.push_back(1);

	for(int k = 0; k <= cnt.size(); k++) 
		for(int i = 0; i <= N; i++) dp[k][i] = 0;
	dp[0][0] = 1;

	for(int i = 0; i < cnt.size(); i++) {
		for(int j = 0; j <= N; j++) if(dp[i][j]) {
			for(int k = 0; k <= cnt[i]; k++) {
				if(j + k > N) continue;

				// newly use: k
				i64 tmp = (C[j][cnt[i] - k] * C[N-j][k]) % MOD;

				ADD(dp[i+1][j+k], dp[i][j] * tmp);
			}
		}
	}

	ret = (ret * dp[cnt.size()][N]) % MOD;

	return ret;
}

int main()
{
	precalc();

	int T;
	scanf("%d", &T);

	for(int t = 0; t++ < T; ) {
		scanf("%d%d", &M, &N);

		for(int i = 0; i < M; i++) {
			scanf("%s", in[i]);
		}

		pLast = 0;

		top = alloc();
		for(int i = 0; i < M; i++) append(top, in[i]);

		calc_weight(top);

		int X = 0;
		for(int i = 0; i < pLast; i++) {
			X += min(N, pool[i].w);
		}

		int Y = (int)count(top);

		printf("Case #%d: %d %d\n", t, X, Y);
	}

	return 0;
}
