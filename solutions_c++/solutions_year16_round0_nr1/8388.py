#include<bits/stdc++.h>
using namespace std;
int getCnt(int N){
	if(N == 0){
		return -1;
	}
	int mask = 0;
	int requiredMask = (1 << 10) - 1;
	int cnt = 0;
	while(mask != requiredMask){
		++cnt;
		int num = cnt * N;
		while(num > 0){
			int r = num % 10;
			mask |= (1 << r);
			num /= 10;
		}
	}
	return cnt*N;
}
int main(){
	int t;
	scanf("%d", &t);
	for(int tc = 1;tc <= t;++tc){
		int N;
		scanf("%d", &N);
		printf("Case #%d: ", tc);
		int ans = getCnt(N);
		if(ans == -1){
			printf("INSOMNIA\n");
		} else{
			printf("%d\n", getCnt(N));
		}
	}
	return 0;
}