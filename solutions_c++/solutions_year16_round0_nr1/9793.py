#include <cstdio>

int main(){
	int numTC, TC = 1, N, bm, target = (1<<10)-1, tmp, num;
	scanf("%d", &numTC);
	while(numTC--){
		scanf("%d", &N); bm = 0; num = 0;
		if(!N){ printf("Case #%d: INSOMNIA\n", TC++); continue; }
		do{
			num+=N; tmp = num;
			while(tmp){ bm|=(1<<(tmp%10)); tmp/=10; }
		} while(bm!=target);
		printf("Case #%d: %d\n", TC++, num);
	}
	return 0;
};