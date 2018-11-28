#include <cstdio>
#include <cstring>
#include <algorithm>


#define N 1000

using namespace std;

int p[N + 5];

int C, caso, n;

void doCase(){
	scanf("%d", &n);
		
		
	int maximun = 0;
		
	for(int i = 0; i < n; i++)scanf("%d", p + i);

	for(int i = 0; i < n; i++)maximun = max(maximun, p[i]);
		
	int ans = maximun;
		
	for(int i = 1; i <= maximun; ++i){
			
		int aux = 0;
			
		for(int j = 0; j < n; ++j){
				
			if(i >= p[j]) continue;
				
			aux += (p[j] - 1) / i;
		}
			
		ans = min(ans, aux + i);
	}
		
	printf("Case #%d: %d\n", ++caso, ans);
}

int main(){
	caso = 0;
	scanf("%d", &C);

	for(int i = 0; i < C; ++i)doCase();
	
	return 0;
}
