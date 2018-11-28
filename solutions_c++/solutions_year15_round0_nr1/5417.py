#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int j = 1; j <= t; ++j)
	{
		int maxShy;
		cin >> maxShy;
		string shyStr;
		cin >> shyStr;
		int sum = 0, i = 0, ans = 0;
		for(i = 0; i <= maxShy; ++i)
		{
			if(sum < i)
			{
				ans += (i - sum);
				sum = i;
			}
			sum += (shyStr[i] - '0');
		}
		printf("Case #%d: %d\n", j, ans);
	}
	return 0;
}
