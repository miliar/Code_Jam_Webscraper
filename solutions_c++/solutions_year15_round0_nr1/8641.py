#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int digit(char c)
{
	return c - '0';
}

int solve()
{
	int smax;
	string s;
	cin >> smax >> s;
	
	int ret = 0;
	int numClap = 0;
	for(int i = 0; i < s.size(); ++i)
	{
		int d = digit(s[i]);
		if(d > 0)
		{
			int addAudience = max(0, i - numClap);
			numClap += addAudience + d;
			ret += addAudience;
		}
	}
	
	return ret;
}

int main()
{
	int T;
	while(cin >> T)
	{
		for(int i = 0; i < T; ++i)
		{
			printf("Case #%d: %d\n", i + 1, solve());
		}
	}
}