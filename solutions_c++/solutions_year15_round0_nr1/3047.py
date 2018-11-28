#include <stdio.h>
#include <algorithm>

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int n, sum = 0;
		int ans = 0;
		scanf("%d",&n);
		for(int i=0;i<=n;++i){
			int tmp;
			scanf("%1d", &tmp);
			if( tmp ){
				ans = std::max( ans, i-sum );
			}
			sum += tmp;
		}
		printf("Case #%d: %d\n", t, ans );

	}
	return 0;
}