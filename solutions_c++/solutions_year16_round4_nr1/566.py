#include <fstream>
#include <string>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");

int T, N, R, P, S;
int dp[20][3][3] = {0};
bool dped[20][3] = {false};
string cht[3] = {"P", "R", "S"};
string dpa[20][3];
 
void DP(int level, int ch)
{
	if (dped[level][ch]) return;
	dped[level][ch] = true;
	if (level == 0)
	{
		dp[level][ch][ch] = 1;
		return;
	}
	DP (level - 1, ch);
	DP (level - 1, (ch + 1) % 3);
	dp[level][ch][0] = dp[level - 1][ch][0] + dp[level - 1][(ch + 1) % 3][0];
	dp[level][ch][1] = dp[level - 1][ch][1] + dp[level - 1][(ch + 1) % 3][1];
	dp[level][ch][2] = dp[level - 1][ch][2] + dp[level - 1][(ch + 1) % 3][2];
	return;
}

string Arrange (int level, int ch)
{
	if (dpa[level][ch].size () != 0) return dpa[level][ch];
	if (level == 0)
	{
		dpa[level][ch] = cht[ch];
		return dpa[level][ch];
	}
	string a = Arrange (level - 1, ch) + Arrange (level - 1, (ch + 1) % 3);
	string b = Arrange (level - 1, (ch + 1) % 3) + Arrange (level - 1, ch);
	if (a < b) dpa[level][ch] = a;
	else dpa[level][ch] = b;
	return dpa[level][ch];
}

int main ()
{
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> N >> R >> P >> S;
		string ans;
		DP (N, 0); DP (N, 1); DP (N, 2);
		if (dp[N][0][0] == P && dp[N][0][1] == R && dp[N][0][2] == S)
			if (ans.size () == 0 || ans > Arrange (N, 0)) ans = Arrange (N, 0);
		if (dp[N][1][0] == P && dp[N][1][1] == R && dp[N][1][2] == S)
			if (ans.size () == 0 || ans > Arrange (N, 1)) ans = Arrange (N, 1);
		if (dp[N][2][0] == P && dp[N][2][1] == R && dp[N][2][2] == S)
			if (ans.size () == 0 || ans > Arrange (N, 2)) ans = Arrange (N, 2);
		if (ans.size () > 0)
			fout << "Case #" << t << ": " << ans << endl;
		else
			fout << "Case #" << t << ": IMPOSSIBLE" << endl;
	}
}

