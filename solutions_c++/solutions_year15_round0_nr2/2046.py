#include <cstdio>
#include <algorithm>
#include <queue>
#include <functional>
using namespace std;

int testCase()
{
	int n;
	scanf("%d", &n);

	vector<int> data;

	for (int i = 0; i < n; i++)
	{
		int input;
		scanf("%d", &input);
		data.push_back(input);
	}

	sort(data.begin(), data.end());

	long long answer = numeric_limits<long long>::max();
	for (int t = 1; t <= data.back(); t++)
	{
		long long result = 0;
		for (int i = 0; i < data.size(); i++)
		{
			result += (data[i] / t) - 1;
			result += !!(data[i] % t);
		}
		result += t;
		answer = min(answer, result);
	}
	return answer;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		printf("%d", testCase());
		printf("\n");
	}
	return 0;
}