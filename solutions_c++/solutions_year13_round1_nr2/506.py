#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

int v[10];

int T, E, R, N;

bool vis[10][10];
int dp[10][10];

int solve(int pos, int e){
	if(pos == N)
		return 0;
	
	if(vis[pos][e])
		return dp[pos][e];
		
	vis[pos][e] = true;
	
	dp[pos][e] = 0;
	for(int i = 0; i <= e; i++){
		dp[pos][e] = max(dp[pos][e], i * v[pos] + solve(pos + 1, min(e - i + R, E)));
	}
	
	return dp[pos][e];
}

int main(){
	cin >> T;
	
	for(int t = 1; t <= T; t++){
		cin >> E >> R >> N;
		for(int i = 0; i < N; i++){
			cin >> v[i];
		}
		memset(vis, false, sizeof(vis));	
		cout << "Case #" << t << ": " << solve(0, E) << "\n";
	}
}
