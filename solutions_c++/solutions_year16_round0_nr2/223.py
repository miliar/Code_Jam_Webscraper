#include<stdio.h>
#include<string.h>

void flip(bool B[], int n)
{
	for (int i=0, j=n; i<=j; i++, j--) {
		bool tmp = !B[i];
		B[i] = !B[j];
		B[j] = tmp;
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		char S[200];
		bool B[200] = {false};
		int c = 0;
		scanf(" %s", S);
		int N = strlen(S);
		for (int i=0; i<N; i++) {
			if (S[i] == '+') {
				B[i] = true;
			}
		}
		for (int i=0; i<N; i++) {
			if (i == 0 || B[i-1] == B[i]) {
				continue;
			}
			flip(B, i-1);
			c++;
		}
		if (!B[0]) {
			c++;
		}
		printf("Case #%d: %d\n", t, c);
	}
	return 0;
}