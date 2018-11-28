//Aleksander Łukasiewicz
#include<bits/stdc++.h>
using namespace std;

int check(int x, int mask){
	while(x){
		mask |= (1<<(x%10));
		x/=10;
	}
	
	return mask;
}

int main(){
	int t;
	scanf("%d", &t);
	for(int pp=1; pp<=t; pp++){
		int n, ans = 0, M = 0;
		scanf("%d", &n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n", pp);
			continue;
		}
		while(M != ((1<<10)-1)){
			ans+=n;
			M = check(ans, M);
		}
		printf("Case #%d: %d\n", pp, ans);
	}

return 0;
}