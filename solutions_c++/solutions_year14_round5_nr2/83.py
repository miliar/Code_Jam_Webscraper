#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
#include <map>
#include <cstdio>

using namespace std;

int N;
int G[100];
int H[100];
int P;
int Q;
map< vector<int>, int > mp;

int solveSmall(int turn){
	vector<int> key(N+1); key[N] = turn;
	for(int i=0;i<N;i++) key[i] = max(0, H[i]);
	if(mp.count(key)) return mp[key];
	int res = 0;
	bool end = true;
	for(int i=0;i<N;i++){
		if(H[i] > 0) end = false;
	}
	if(end) return mp[key] = 0;
	if(turn == 0){
		res = max(res, solveSmall(1));
		for(int i=0;i<N;i++){
			if(H[i] > 0){
				H[i] -= P;
				res = max(res, (H[i] <= 0 ? G[i] : 0)+solveSmall(1));
				H[i] += P;
			}
		}
	} else {
		for(int i=0;i<N;i++){
			if(H[i] > 0){
				H[i] -= Q;
				res = max(res, solveSmall(0));
				H[i] += Q;
				break;
			}
		}
	}
	return mp[key] = res;
}

int solveLarge(){
	int dp[2][2][2001];
	memset(dp, -1, sizeof(dp));
	dp[0][1][0] = 0;
	for(int i=0;i<N;i++){
		int cur = i%2, next = 1-cur;
		memset(dp[next], -1, sizeof(dp[next]));
		for(int j=0;j<2;j++){
			for(int k=0;k<=2000;k++){
				if(dp[cur][j][k] == -1) continue;
				{
					int add = (H[i]+Q-1)/Q+j-1;
					dp[next][1][k+add] = max(dp[next][1][k+add], dp[cur][j][k]);
				}
				for(int enemyAttack=0; ;enemyAttack++){
					if(enemyAttack*Q >= H[i]) break;
					int myAttack = (H[i]-enemyAttack*Q+P-1)/P;
					int chance = enemyAttack + j;
					if(myAttack > chance){
						if(k < myAttack-chance) continue;
						dp[next][0][k-(myAttack-chance)] = max(dp[next][0][k-(myAttack-chance)], dp[cur][j][k]+G[i]);
					} else {
						dp[next][0][k+chance-myAttack] = max(dp[next][0][k+chance-myAttack], dp[cur][j][k]+G[i]);
					}
				}
			}
		}
	}
	int res = 0;
	for(int i=0;i<2;i++){
		for(int j=0;j<=2000;j++){
			res = max(res, dp[N%2][i][j]);
		}
	}
	return res;
}

int main(){
	int T; cin >> T;
	for(int test=1;test<=T;test++){
		cin >> P >> Q >> N;
		for(int i=0;i<N;i++) cin >> H[i] >> G[i];
		printf("Case #%d: %d\n", test, solveLarge());
	}
}
