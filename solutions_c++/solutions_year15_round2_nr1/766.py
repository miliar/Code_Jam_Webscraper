#include <iostream>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

map<int, int> dp;

int reverse(int i)
{
	int result = 0;
	while (i)
	{
		result *= 10;
		result += i % 10;
		i /= 10;
	}
	return result;
}


int main()
{
	//cout << reverse(2300) << endl;
	
	for (int i = 1; i <= 1000 * 1000; ++i)
		dp[i] = i;

	for (int i = 1; i <= 1000 * 1000; ++i)
	{
		dp[i + 1] = min(dp[i] + 1, dp[i + 1]);
		int ri = reverse(i);
		dp[ri] = min(dp[ri], dp[i] + 1);
	}
	
	int n, k;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cin >> k;
		cout << "Case #" << i + 1 << ": " << dp[k] << '\n';
	}

	return 0;
}