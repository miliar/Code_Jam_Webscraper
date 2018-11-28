#include <stdio.h>
#include <queue>

int main(){
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; t++){
		int a, b;
		scanf("%d%d", &a, &b);
		int cnt = 0;
		if(a <= 1 && 1 <= b)
			cnt++;
		if(a <= 4 && 4 <= b)
			cnt++;
		if(a <= 9 && 9 <= b)
			cnt++;
		if(a <= 121 && 121 <= b)
			cnt++;
		if(a <= 484 && 484 <= b)
			cnt++;
		printf("Case #%d: %d\n", t+1, cnt);
	}
	return 0;
}
