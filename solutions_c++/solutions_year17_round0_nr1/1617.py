#include <cstdio>

int T;
char list[9999];
int main() {
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++) {
		scanf("%s",list);
		int N=0;
		while(list[N]!='\0') N++;
		int K;
		scanf("%d",&K);
		int sol=0;
		for(int i=0;i<N-K+1;i++) {
			if(list[i]=='-') {
				sol++;
				for(int j=0;j<K;j++) {
					if(list[i+j]=='+') {
						list[i+j]='-';
					} else {
						list[i+j]='+';
					}
				}
			}
		}
		for(int i=0;i<N;i++) if(list[i]=='-') sol=-1;
		if(sol<0) {
			printf("Case #%d: IMPOSSIBLE\n",cases);
		} else {
			printf("Case #%d: %d\n",cases,sol);
		}
	}
	return 0;
}
