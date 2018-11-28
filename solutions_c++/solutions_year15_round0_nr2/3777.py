#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdio>

#define N 1005

using namespace std;

int p[N];

int main(){
	
	int nc, caso = 1;
	scanf("%d", &nc);
	
	while(nc--){
		
		int n;
		scanf("%d", &n);
		
		
		int max_value = 0;
		
		for(int i = 0; i < n; i++){
			scanf("%d", p + i);
			
			max_value = max(max_value, p[i]);
		}
		
		int ans = max_value;
		
		for(int j = 1; j <= max_value; j++){
			
			int aux = 0;
			
			for(int i = 0; i < n; i++){
				
				if(j >= p[i]) continue;
				
				aux += (p[i] - 1) / j;
			}
			
			ans = min(ans, aux + j);
		}
		
		printf("Case #%d: %d\n", caso, ans);
		caso++;
	}
	
	return 0;
}
