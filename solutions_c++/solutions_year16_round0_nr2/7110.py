#include<stdio.h>
#include<string.h>

char A[105], B[105];
int ans, T, t;

int main(){
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
	scanf("%d ", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		scanf("%s", A);
		int N = strlen(A);
		ans = 0;
		for (int i = N - 1; i >= 0; i--){
			if (A[i] == '+')continue;
			ans++;
			if (A[0] == '+'){
				ans++;
				for (int j = 0; j < i&&A[j] == '+'; j++)A[j] = '-';
			}
			strcpy(B, A);
			for (int j = 0; j <= i; j++){
				if (B[j] == '+')A[i - j] = '-';
				else A[i - j] = '+';
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}