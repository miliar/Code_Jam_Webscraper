#include <cstdio>
int main (){
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	int T, N;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d", &N);
		if (N == 0)
			printf("Case #%d: INSOMNIA\n");
		else {
			bool YN = false;
			bool digit[10] = {0};
			int cnt = 0;
			while (!YN){
				cnt += N;
				int temp = cnt;
				while (temp){
					digit [temp % 10] = true;
					temp /= 10;
				}
				YN = true;
				for (int j = 0; j < 10; j++)
					YN = YN && digit[j];
			}
			printf("Case #%d: %d\n", i, cnt);
		}
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
