#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

const int MAX_N = 1e3 + 10;
char S[MAX_N]; int N, K;
int Memo[MAX_N], Cnt;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC; scanf("%d", &TC);
	for(int t=1; t<=TC; t++) {
		scanf("%s", S); N = strlen(S); scanf("%d", &K);
		int ans = 0;
		for(int i=0; i<N; i++) Memo[i] = 0; Cnt = 0;
		for(int i=0; i<N; i++) {
			Cnt -= Memo[i];
			if(Cnt % 2 == 1) S[i] = (int)'-' + '+' - S[i];
			if(i < N-K+1 && S[i] == '-') Cnt++, Memo[i+K]++, ans++, S[i] = '+';
		}
		bool isTrue = true;
		for(int i=0; i<N; i++) if(S[i] == '-') isTrue = false;
		printf("Case #%d: ", t);
		if(!isTrue) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}