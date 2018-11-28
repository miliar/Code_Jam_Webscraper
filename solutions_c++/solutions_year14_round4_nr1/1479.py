#include <stdio.h>
#include <algorithm>
using namespace std;
int T;
int N, X;
int S[20202];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for(int i=1; i<=T; i++) {
		scanf("%d %d", &N, &X);
		for(int j=1; j<=N; j++) scanf("%d", &S[j]);
		sort(S+1, S+N+1);
		int r=1, f=N, cnt=0;
		while(r<=f) {
			if(S[r]+S[f]<=X) {
				cnt++;
				r++;
				f--;
				continue;
			}else{
				cnt++;
				f--;
				continue;
			}
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}
