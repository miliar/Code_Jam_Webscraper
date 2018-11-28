#include<bits/stdc++.h>
using namespace std;
main() {
	int T,N,i,j;
	scanf("%d",&T);
	for(j=1;j<=T;j++) {
		scanf("%d",&N);
		char S[N+1];
		scanf("%s",S);
		int sum=S[0]-'0';
		int extra=0;
		for(i=1;i<=N;i++) {
			if(sum<i) {
				extra+=(i-sum);
				sum=i;
			}
			sum+=(S[i]-'0');
		}
		cout << "Case #" << j << ": " << extra << endl;
	}
}
