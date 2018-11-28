#include <cstdio>
#define MAX 1010
int main()
{
	int T, Max;
	char tmp;
	int num[MAX];
	int ans, count;
	scanf("%d", &T);
	for(int k = 1; k <= T; k++){
		scanf("%d", &Max);
		ans = 0;
		for(int i = 0; i <= Max; i++){
			scanf(" %c", &tmp);
			num[i] = tmp - '0';
		}
		count = num[0];
		for(int i = 1; i <= Max; i++){
			if(num[i] != 0 && (count < i)){
				ans += i - count;
				count += i - count;
			}
			count += num[i];
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}
