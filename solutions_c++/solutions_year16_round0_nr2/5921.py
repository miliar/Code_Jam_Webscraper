#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
using namespace std;
const int N = 110;
int dp[N][N][2];
string s;
int dfs(int left, int right, char goal)
{
	if (right < left)return 0;
	if (left == right)
	{
		return dp[left][right][goal != '+'] = s[left] != goal;
	}
	int next_right = right;
	while(next_right >=0 && s[next_right] == goal)
	{
		next_right --;
	}
	if (next_right < right)
	{
		return dp[left][right][goal] = dfs(left, next_right, goal);
	}else {
		next_right = right;
		while(next_right >= 0 && s[next_right] != goal)	
		{
			next_right --;
		}
		return dp[left][right][goal] = dfs(left, next_right, goal == '+' ? '-' : '+') + 1;
	}

}
int main(){
	int T;
	cin >> T;
	for (int cas = 1;cas <= T;cas ++)
	{
		cin >> s;
		memset(dp, -1,sizeof (dp));
		cout << "Case #" << cas << ": " << dfs(0, s.size() - 1, '+') << endl;

	}
	return 0;
}
