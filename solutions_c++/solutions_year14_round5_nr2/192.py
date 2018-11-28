#include <iostream>
using namespace std;

int cases;
int dp[100001][101]; // number of turns spared, #monsters killed, is it Diana's turn?
int diana, tower, monsters;
int monster[101], gold[101];
int cost[101], reward_c[101], reward_b[101]; // reward with use and reward before use

int find(int turns, int killed) {
	if (turns < 0) return -(1<<28);
	if (killed == monsters) return 0;
	if (dp[turns][killed] == -1) {
		int nokill = 0;
		int withkill = 0;
		nokill = find(turns + reward_b[killed], killed+1);
		withkill = find(turns - cost[killed] + reward_c[killed], killed+1) + gold[killed];


		dp[turns][killed] = max(nokill, withkill);
	}
	return dp[turns][killed];
}

// standard DP. I hope.
int main() {
	cin>>cases;
	for (int c = 1; c <= cases; c++) {
		cin>>diana>>tower>>monsters;
		for (int i = 0; i < monsters; i++) {
			cin>>monster[i]>>gold[i];
		}

		// don't forget to reset
		for (int i = 0; i < monsters; i++) {
			for (int j = 0; j <= 100000; j++) {
				dp[j][i] = -1;
			}
		}

		// precompute
		for (int i = 0; i < monsters; i++) {
			cost[i] = ((monster[i] - 1 + tower)% tower) / diana + 1;
			reward_c[i] = (monster[i] - 1) / tower;
			reward_b[i] = (monster[i] - 1 + tower) / tower;
		}

		// Find DP.
		int ans = 0;
		ans = find(1, 0);
		cout<<"Case #"<<c<<": "<<ans<<"\n";
	}
}