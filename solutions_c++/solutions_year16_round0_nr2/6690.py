#include <cstdio>
#include <cstring>

int process(char S[]) {
	int res = 1;
	for (int i = 1; i < strlen(S); i++) {
		if (S[i] != S[i-1])
			res++;
	}
	if (S[strlen(S)-1] == '+')
		res--;
	return res;
}

int main() {
	int T;
	scanf("%d",&T);
	for (int tc = 1; tc <= T; tc++) {
		char S[105];
		scanf("%s",S);
		printf("Case #%d: %d\n",tc,process(S));
	}
	return 0;
}