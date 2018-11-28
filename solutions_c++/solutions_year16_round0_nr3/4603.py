#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;

vector<pair<string, vector<int>>> ans;

long long divisor(long long n)
{
	for (int i = 2; i * 1ll * i <= n; i++)
	{
		if (n % i == 0)
			return i;
	}
	return 1;
}

void updateForCurrent(string s)
{
	vector<int> nums(9);
	bool b = true;
	for (int base = 2; base <= 10 && b; base++)
	{
		long long num = 0;
		long long st = 1;
		for (int i = 0; i < s.length(); i++)
		{
			num += (st * (s[i] - '0'));
			st *= base;
		}
		int d = divisor(num);
		if (d != 1)
			nums[base - 2] = d;
		else
			b = false;
	}

	if (b)
	{
		reverse(s.begin(), s.end());
		ans.push_back(make_pair(s, nums));
	}
}

int main()
{
	freopen("output.txt", "w", stdout);
	int N = 16;
	int J = 50;
	for (int i = (1 << (N - 1)) + 1; i < (1 << N) && ans.size() < J; i += 2)
	{
		string s = "";
		int tmp = i;
		while (tmp)
		{
			s += ('0' + (tmp & 1));
			tmp >>= 1;
		}
		updateForCurrent(s);
	}

	printf("Case #1:\n");
	for (int i = 0; i < ans.size(); i++)
	{
		printf("%s ", ans[i].first.c_str());
		for (int j = 0; j < 9; j++)
		{
			printf("%d ", ans[i].second[j]);
		}
		printf("\n");
	}

	return 0;
}