#include <stdio.h>
#include <memory.h>
#include <algorithm>

using namespace std;
int T;
int dp[10000010];
bool visited[10000010];
int N;

int reverse(int num) {
	int n = 0;
	int help = num;
	int result = 0;
	while(help > 0 ) {
		result = result*10 + help%10;
		help/=10;
	}
	return result;
}

int solve(int cur) {
	if(cur >= 10*N) return 9999999;
	if(cur == N) return 0;
	if(dp[cur] != -1) return dp[cur];
	if(visited[cur]) return 9999999;
	visited[cur] = true;
	int rev = reverse(cur);
	if(rev != cur) dp[cur] = min(solve(cur+1)+1, solve(rev)+1);
	else dp[cur] = solve(cur+1)+1;
	
	return dp[cur];
	
}


int main()  {
	scanf("%d",&T);
	
	for(int i = 0; i<= 10000000;i++) dp[i] = 9999999;
	dp[1] = 1;
	for(int j = 0; j < 1000;j++) {
		for(int i = 1; i <= 1000000;i++) {
			int rev = reverse(i);
				
			dp[i+1] = min(dp[i+1],dp[i]+1);
			dp[rev] = min(dp[rev],dp[i]+1);
			
		}
		
	}
	
	memset(visited, 0, sizeof(visited));
	
	for(int t = 1; t<= T;t++) {
		scanf("%d",&N);
		
		int result = dp[N];
		
		printf("Case #%d: %d\n",t,result);
	}
	
	
	return 0;
}
