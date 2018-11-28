#include <cstdio>
int main(){
	int T, tt = 1;
	char inp[1010];
	int fri[1010];
	scanf("%d", &T);
	while(T--){
		int lev;
		scanf("%d %s", &lev, inp);
		for(int i = 0 ; i <= lev ; i++){
			fri[i] = inp[i]-'0';
		}
		int now = 0, add = 0;
		for(int i = 0 ; i <= lev ; i++){
			if(now < i && fri[i] != 0){
				add += i-now;
				now += add;
			}
			now += fri[i];
			//printf("now %d\n", now);
		}
		printf("Case #%d: %d\n", tt++, add);
	}
	return 0;
}