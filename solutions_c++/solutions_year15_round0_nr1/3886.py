#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdio>

#define N 1005

using namespace std;

char s[N];

int main(){
	
	int nc, caso = 1;
	scanf("%d", &nc);
	
	while(nc--){
		
		int n;
		scanf("%d", &n);
		
		scanf("%s", s);
		
		int ans = 0, tot = 0;
		
		for(int i = 0; i < n + 1; i++){
			ans = max(ans, max(0, i - tot));
			tot += (s[i] - '0');
		}
		
		printf("Case #%d: %d\n", caso, ans);
		caso++;
	}
	
	return 0;
}
