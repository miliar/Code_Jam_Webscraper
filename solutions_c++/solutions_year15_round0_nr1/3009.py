#include<cstdio>

int main(void){
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d: ", i);
		int now, ans;
		int S;
		char cnt[1010];
		scanf("%d%s", &S, cnt);
		
		now = ans = 0;
		for(int j = 0; j <= S; j++){
			if(j <= now)
				now += (cnt[j]-'0');
			else if(cnt[j]-'0'){
				ans += j-now;
				now += j-now;
				now += (cnt[j]-'0');
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}