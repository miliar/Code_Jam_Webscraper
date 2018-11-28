#include <fstream>
#include <deque>
using namespace std;

//i 105 j106 k107
int tran[4][4] = {
	1, 105, 106, 107,
	105, -1, 107, -106,
	106, -107, -1, 105,
	107, 106, -105, -1 };

	char ss[10005];
	int dp[10005][10005];

bool panduan(int lenth)
{
	for (int w = 0; w<lenth; ++w)//´Ów³ö·¢
	{
		dp[w][w] = ss[w];
		for (int j = w + 1; j<lenth; ++j)
		{
			if (dp[w][j - 1]<0)
			{
				if (dp[w][j - 1] == -1)
					dp[w][j] = -ss[j];
				else
					dp[w][j] = -tran[-dp[w][j - 1] - 'i' + 1][ss[j]-'i'+1];
			}
			else
			{
				if (dp[w][j - 1]>1)
					dp[w][j] = tran[dp[w][j - 1] - 'i' + 1][ss[j] - 'i' + 1];
				else
					dp[w][j] = ss[j];
			}
		}
	}
	for (int r = 0; r<lenth; ++r)
	{
		if (abs(dp[0][r]) == 105)
		{
			for (int s = r + 1; s<lenth; ++s)
			{
				if (abs(dp[r + 1][s]) == 106)
				{
					if (abs(dp[s + 1][lenth - 1]) == 107)
						if(dp[0][r]*dp[r + 1][s]*dp[s + 1][lenth - 1]>0)
							return true;
				}
			}
		}
	}
	return false;
}

int main()
{
	int t;
	ifstream infile("F:\\C-small-attempt3.in");
	ofstream outfile("F:\\C-small-attempt3.out");
	infile >> t;
	for (int i = 1; i <= t; i++)
	{
		int l, x;
		infile >> l >> x;
		char temp[10005];
		ss[0] = '\0';
		infile >> temp;
		for (int pp = 1; pp <= x; pp++)
			strcat_s(ss, temp);
		int lenth = l*x;
		if (panduan(lenth))
			outfile << "Case #" << i << ": YES" << endl;
		else
			outfile << "Case #" << i << ": NO" << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}