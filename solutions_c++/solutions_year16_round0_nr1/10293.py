#include <bits/stdc++.h>
using namespace std;

int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int T;
	scanf("%d", &T);

	int N;
	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		scanf("%d", &N);
		if(N == 0) puts("INSOMNIA");
		else {
			int i = 1;
			int cur = N, tmp = N, used = 0;
			while(used != (1 << 10) - 1){
				tmp = cur = N * (i++);
				while(tmp){ used |= 1 << (tmp % 10); tmp /= 10; }
			}
			printf("%d\n", cur);
		}
	}
}