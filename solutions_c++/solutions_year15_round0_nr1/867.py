#include<cstdio>

static bool check(int M,const int *num) {
	int now=0;
	for(int i=0;i<=M;i++) {
		if(num[i]>0) {
			if(now<i)return false;
			now+=num[i];
		}
	}
	return true;
}

int main() {
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		int M; int num[1+1000];
		scanf("%d ",&M);
		int i;
		for(i=0;i<=M;i++)num[i]=getchar()-'0';
		for(i=0;!check(M,num);i++)++*num;
		printf("Case #%d: %d\n",t,i);
	}
	return 0;
}
