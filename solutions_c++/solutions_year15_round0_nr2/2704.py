#include <bits/stdc++.h>
using namespace std;
int TC,N,P[1010];
int main(){
	scanf("%d",&TC);
	for (int tc=1; tc<=TC; tc++){
		scanf("%d",&N);
		int pmax=1, ans=10000000;
		for (int i=0; i<N; i++){
		   scanf("%d",&P[i]);
		   pmax = max(pmax,P[i]);
		}
		for (int p=1; p<=pmax; p++) {
			int t=p;
			for (int i=0; i<N; i++){
				t += (P[i]-1)/p;
			}
			ans = min(ans, t);
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}
