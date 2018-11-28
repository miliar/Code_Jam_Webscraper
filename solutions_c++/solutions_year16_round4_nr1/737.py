#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin >> T;

	string dp[3][13];
	dp[0][0] = 'P';
	dp[1][0] = 'R';
	dp[2][0] = 'S';

	for(int N = 1; N <= 12; ++N)
	{
		dp[0][N] = min(dp[0][N-1] + dp[1][N-1], dp[1][N-1] + dp[0][N-1]);
		dp[1][N] = min(dp[1][N-1] + dp[2][N-1], dp[2][N-1] + dp[1][N-1]);
		dp[2][N] = min(dp[2][N-1] + dp[0][N-1], dp[0][N-1] + dp[2][N-1]);
	}

	for(int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";

		int N,R,P,S;
		cin >> N >> R >> P >> S;

		string out = "z";
		for(int w = 0; w < 3; ++w)
		{
			int cnt[256] = {};
			for(char c : dp[w][N])
				cnt[c] ++;
			if(cnt['R'] == R && cnt['P'] == P && cnt['S'] == S)
				out = min(out, dp[w][N]);
		}
		
		if(out == "z")
			cout <<"IMPOSSIBLE\n";
		else
			cout << out << "\n";
	}
}
