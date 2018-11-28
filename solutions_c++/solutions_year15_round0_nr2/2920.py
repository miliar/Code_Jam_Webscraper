#include <stdio.h>

int p[1000];

int calc(int n, int max){
	int cnt = 0;
	for(int i=0;i<n;++i)
		cnt += (p[i]-1) / max;
	return cnt;
}

int main(){
	int T;
	scanf("%d",&T);

	for(int t=1;t<=T;++t){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%d", &p[i]);
		int ans = 2147483647;
		for(int i=1;i<=1000;++i){
			int ret =  i + calc(n, i);
			if( ret < ans ) ans = ret;
		}
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}
