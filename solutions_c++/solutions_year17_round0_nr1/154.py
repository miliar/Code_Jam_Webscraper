#include <bits/stdc++.h>
using namespace std;

#define MAXN 1004

int T, N, K;
char S[MAXN];

int main()
{
	for (scanf("%d", &T);T--;){
		scanf("%s%d", S+1, &K); N = strlen(S+1);
		int ans = 0;
		for (int i=1;i<=N-K+1;i++) if (S[i] == '-'){
			ans++;
			for (int j=0;j<K;j++){
				if (S[i+j] == '+') S[i+j] = '-';
				else S[i+j] = '+';
			}
		}
		bool yes = 1;
		for (int i=1;i<=N;i++) if (S[i] == '-') yes = 0;
		static int ts = 0;
		printf("Case #%d: ", ++ts);
		if (yes) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
}