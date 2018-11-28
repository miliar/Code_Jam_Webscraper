#include <stdio.h>

int t, k, c, s;

int main(){
	scanf("%d",&t);
	for(int tt=1;tt<=t;++tt){
		printf("Case #%d:",tt);
		scanf("%d %d %d", &k, &c, &s);
		for(int i=0;i<k;++i){
			printf(" %d", i+1);
		}
		puts("");
	}
	return 0;
}
