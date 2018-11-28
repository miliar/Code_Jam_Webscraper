#include<cstdio>

int num[30], N;

char findMax(void);

int main(){
	int T;
	int cnt = 0;
	scanf("%d", &T);
	while(T--){
		int total = 0;
		scanf("%d", &N);
		for(int i = 0; i < N; i++){
			scanf("%d", &num[i]);
			total += num[i];
		}

		printf("Case #%d:", ++cnt);
		while(total > 2){
			printf(" %c", findMax());
			total--;
			for(int i = 0; i < N; i++){
				if(num[i] > total/2){
					printf("%c", i+'A');
					num[i]--;
					total--;
				}
			}
		}
		printf(" %c%c\n", findMax(), findMax());
	}
	return 0;
}

char findMax(void){
	int mmax = 0, ans;
	for(int i = 0; i < N; i++){
		if(num[i] > mmax){
			mmax = num[i];
			ans = i;
		}
	}
	num[ans]--;
	return ans+'A';
}
