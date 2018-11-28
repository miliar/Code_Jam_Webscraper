#include <bits/stdc++.h>
using namespace std;
int main(){
	int TC;
	scanf("%d",&TC);
	for (int tc=1; tc<=TC; tc++){
		int N,ans=0,cur=0; char S;
		scanf("\n%d ",&N);
		for (int i=0; i<=N; i++){
			scanf("%c",&S);
			S-='0';
			if (cur<i){
				ans += i-cur;
				cur = i;
			}
			cur+=S;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}

