#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;

void solutionB(string a, int num){
	int len = a.length();
	vector<vector<int> > dp(2, vector<int>(len, INT_MAX));	//'+' ->1, '-' ->0
	if (a[0] == '+'){
		dp[0][0] = 1;
		dp[1][0] = 0;
	}
	else{
		dp[0][0] = 0;
		dp[1][0] = 1;
	}
	for (int i = 1; i < len; i++){
		if (a[i] == '+'){
			dp[0][i] = min(dp[0][i - 1] + 2, dp[1][i - 1] + 1);
			dp[1][i] = min(dp[0][i - 1] + 1, dp[1][i - 1]);
		}
		else{
			dp[0][i] = min(dp[0][i - 1], dp[1][i - 1] + 1);
			dp[1][i] = min(dp[0][i - 1] + 1, dp[1][i - 1] + 2);
		}
	}
	cout << "Case #" << num << ": " << dp[1][len - 1] << endl;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	string a;
	int num = 1;
	while (cin >> a){
		solutionB(a, num);
		num++;
	}
	return 1;
}
