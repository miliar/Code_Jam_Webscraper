#include <stdlib.h>
#include <stdio.h>
#include <queue>
#include <algorithm>



using std::priority_queue;

int D;
priority_queue<int, std::vector<int>, std::less<int>> plates;


int f(int n){
	int resDoNothing = plates.top();
	
	if(resDoNothing <= 1) return resDoNothing;
	if(resDoNothing <= n) return resDoNothing;
	
	plates.pop();
	plates.push(resDoNothing / 2);
	plates.push(resDoNothing / 2 + resDoNothing % 2);
	
	return std::min(resDoNothing, f(n + 1) + 1);
}

int numPancakes[1111];

int main(){
	int T, t;
	scanf("%d", &T);
	
	for(t = 1; t <= T; ++t){
		int i;
		
		D = 30;
		scanf("%d", &D);
		for(i = 0; i < D; ++i){
			scanf("%d", &numPancakes[i]);
		}
		
		
		plates = std::move(priority_queue<int, std::vector<int>, std::less<int>>(
			&numPancakes[0], &numPancakes[D]
		));
		
		printf("Case #%d: %d\n", t, f(0));
		
	}
	
	return 0;
}
