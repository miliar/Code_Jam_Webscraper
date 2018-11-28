#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int64_t getMinSteps(const std::string str)
{
	int dp[100];
	memset(dp, 0, sizeof(dp));
	if(str[1] == '-')
		dp[1] = 1;
	for(size_t i = 2; i < str.size(); ++i)
	{
		if(str[i] == '-')
		{
			if(str[i - 1] == '-')
				dp[i] = dp[i - 1];
			else
				dp[i] = dp[i - 1] + 2;
		}
		else
		{
			dp[i] = dp[i - 1];
		}
	}
	return dp[str.size() - 1];
}

int main()
{
	int T;
	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	while(cin >> T)
	{
		for(int i = 1;i <= T; ++i)
		{
			string str;
			cin >> str;
			str = string("0") + str;
			cout << "Case #" << i << ": " << getMinSteps(str) << endl;
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
