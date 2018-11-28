#include <bits/stdc++.h>

using namespace std;

const int MAXL = 1E3 + 10;

char s[MAXL];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);
		int K;
		scanf("%s%d", s, &K);
		int n = strlen(s);
		for (int i = 0; i < n; ++i)
			s[i] = s[i] == '-';

		int cnt = 0;
		for (int i = 0; i <= n - K; ++i)
			if (s[i])
				++cnt, transform(s + i, s + i + K, s + i, logical_not<char>());

		if (accumulate(s, s + n, 0))
			puts("IMPOSSIBLE");
		else
			printf("%d\n", cnt);
	}
	return 0;
}
