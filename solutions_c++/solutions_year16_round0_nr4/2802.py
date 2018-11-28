#include <bits/stdc++.h>
using namespace std;

int T, TC = 1, K, C, S;
void solveSmall(){
	unsigned long long x = 1;
	for(int i = 0; i < C-1; i++) x = x*(unsigned long long)K;
	unsigned long long ans = 1;
	for(int i = 0; i < S; i++){
		printf(" %llu", ans);
		ans = ans+x;
	}
}
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	while(T--){
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d:", TC++);
		solveSmall();
		puts("");
	}
	return 0;
}
