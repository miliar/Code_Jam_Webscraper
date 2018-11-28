#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#define maxn 110
typedef long long ll;
using namespace std;
int T, K, C, S, sta;
ll bit[maxn], pos;
void solve(int cas)
{
	scanf("%d%d%d", &K, &C, &S);
	printf("Case #%d: ", cas);
	if (S == K){
		for (int i = 1; i <= S; ++ i)
			printf("%d ", i); puts("");
		return;
	}
	if (S * C < K){
		puts("IMPOSSIBLE"); return;
	}
	bit[0] = 1;
	for (int i = 1; i <= C; ++ i) bit[i] = bit[i - 1] * 1ll * K;
	for (int i = 1; i <= S; ++ i){
		pos = 0; sta = (i - 1) * C; if (sta >= K) break;
		for (int i = 0; i < C; ++ i) pos += bit[i] * 1ll * (sta + i) % K;
		++ pos;
		printf("%lld ", pos);
	}
	puts("");
}
int main()
{
	scanf("%d", &T);
	for (int i = 1; i <= T; ++ i) solve(i);
	return 0;
}





