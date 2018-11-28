//Author: net12k44
#include <bits/stdc++.h>
using namespace std;

void solveEqual(int K){
	for(int i = 1; i <= K; ++i)
		printf("%d ", i);
	printf("\n");
}

void solve(){	
	int K,C,S;
	scanf("%d%d%d",&K,&C,&S);
	if (K==S){
		solveEqual(K);
		return;
	}
	printf("IMPOSSIBLE\n");
}

int main(){
	freopen("file.out","w",stdout);
	int test; scanf("%d\n",&test);	
	for(int t = 1; t <= test; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}