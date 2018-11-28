#include <stdio.h>

int main(){

	int tn;
	long long int x, num;
	scanf("%d", &tn);
	for(int t=1;t<=tn;t++){
		scanf("%lld", &num);
		int visit[10] = {0};
		if(num==0){
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		int ans = 0;
		int tmp = 10;
		int find = 0;
		long long int a = 0;
		while(find!=1){
			a += num;
			x = a;
			ans++;
			// printf("%d\n", x);
			while(x > 0){
				if(visit[x%10] == 0){
					tmp--;
					if(tmp == 0){
						find = 1;
						break;
					}
					visit[x%10] = 1;
				}
				x = x/10;
			}
			
		}
		printf("Case #%d: %lld\n", t, a);
	}
	return 0;
}