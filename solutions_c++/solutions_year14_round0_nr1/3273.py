#include <cstdio>
#include <cstring>

int cases, N, M;
int flag[20];

int main(){
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx){
		scanf("%d", &N);
		--N;
		int x;
		memset(flag, 0, sizeof(flag));
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j){
				scanf("%d", &x);
				if(i == N) flag[x]++;
			}
		int cnt = 0, ans;
		scanf("%d", &M);
		--M;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j){
				scanf("%d", &x);
				if(i == M){
					if(flag[x]){
						cnt++;
						ans = x;
					}
				}
			}
		printf("Case #%d: ", xx);
		if(cnt == 0){
			puts("Volunteer cheated!");
		} else if(cnt > 1){
			puts("Bad magician!");
		} else {
			printf("%d\n", ans);
		}
	}
}
