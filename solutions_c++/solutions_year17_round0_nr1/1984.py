#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

char g_pancakes[1001];

void Reverse(std::string& pancakes, int K, int startIndex)
{
	for (int i = 0; i < K; ++i)
	{
		int index = startIndex + i;
		pancakes[index] = (pancakes[index] == '+') ? '-' : '+';
	}
}

bool IsAllSideUp(std::string& pancakes)
{
	return std::all_of(pancakes.begin(), pancakes.end(), [](char c)
	{
		return c == '+';
	});
}

int Solve(const std::string& pancakes, int K)
{
	std::string copyPancakes(pancakes);
	
	int count = 0;

	for (std::string::size_type i = 0; i < copyPancakes.size() - (K - 1); ++i)
	{
		if (copyPancakes[i] == '-')
		{
			Reverse(copyPancakes, K, i);
			
			++count;
		}
	}
	
	return IsAllSideUp(copyPancakes) ? count : -1;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		int K;
		scanf("%s %d", g_pancakes, &K);

		printf("Case #%d: ", i);
		int ans = Solve(g_pancakes, K);
		if (ans < 0)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n", ans);
		}
	}
	
	return 0;
}