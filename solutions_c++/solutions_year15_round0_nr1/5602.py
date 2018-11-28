#include<bits/stdc++.h>
using namespace std;

int main(){
	int T, N, c, ans, v, cas = 0 ;
	string S;
	
	scanf("%d", &T);
	while(T--){
		printf("Case #%d: ",++cas);
		scanf("%d", &N);
		cin >> S;
		c = 0; ans = 0;
		for(int i = 0; i <= N; i++){
			v = S[i] - '0';
			if(c < i && v > 0){
				ans += (i - c);
				c += (i - c);
			}
			c += v;
		}
		printf("%d\n", ans);
	}
	return 0;
}
