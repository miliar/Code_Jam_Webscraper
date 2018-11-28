#include<stdio.h>
int main()
{
	int T, t = 0;
	scanf("%d", &T);
	while(T--) {
		int n, res = 0, cnt = 0;
		scanf("%d", &n); getchar();
		for(int i = 0; i < n+1; i++) {
			char d = getchar();
			if(cnt < i) { res += i-cnt; cnt += i-cnt; }
			cnt += d-'0';
		} getchar();
		printf("Case #%d: %d\n", ++t, res);
	}
	return 0;
}

