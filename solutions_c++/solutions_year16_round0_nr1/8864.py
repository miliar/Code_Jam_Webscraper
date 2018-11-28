#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

int main()
{
	int n;
	scanf("%d", &n);

	for(int i = 0; i < n; i++){
		long long int x;
		scanf("%lld", &x);
		int name[MAX] = {0};
		memset(name, 0, sizeof(name));
		int cnt = 0;
		int s = 0;
		if(x == 0){
			printf("Case #%d: INSOMNIA\n", i+1);
			continue;
		}
		while(cnt != 10){
			s++;
			long long int T = x*s;
			while(T > 0){
				if(name[T%10] == 0){
					name[T%10] = 1;
					cnt++;
				}
				T /= 10;
			}
		}
		printf("Case #%d: %lld\n", i+1, x*s);
	}
	return 0;
}
