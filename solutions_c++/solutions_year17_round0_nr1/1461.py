#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int T, K, L;
char S[1010];

int main() {
	int i, j, res, t=1;
	scanf("%d", &T);
	while (T--) {
		scanf(" %s %d", S, &K);
		L = strlen(S);
		for (i=res=0; i<=L-K; i++) {
			if (S[i] == '-') {
				res++;
				for (j=i; j<i+K; j++) {
					S[j] = (S[j] == '-' ? '+' : '-');
				}
			}
		}
		for (i=L-K; i<L; i++) {
			if (S[i] == '-') res = -1;
		}
		printf("Case #%d: ", t++);
		if (res == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	return 0;
}