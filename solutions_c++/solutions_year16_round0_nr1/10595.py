#include <cstdio>
#include <cstring>
int T, n;
bool digit[11];
int main()
{
	int num, cnt, k;
	scanf("%d", &T);
	for(int kase = 1; kase <= T; kase++) {
		scanf("%d", &n);
		memset(digit, 0, sizeof(digit));
		k = 1;
		while(true) {
			if(k == 100) break;
			num = cnt = n*k;
			while(cnt) {
				digit[cnt%10] = true;
				cnt /= 10;
			}
			bool flag = false;
			for(int i = 0; i < 10; i++) {
				if(!digit[i]) {
					flag = true;
					break;
				}
			}
			if(!flag) break;
			k++;
		}
		printf("Case #%d: ", kase);
		if(k == 100) {
			puts("INSOMNIA");
		}
		else {
			printf("%d\n", num);
		}
	}
	return 0;
}
