#include <cstdio>
#include <string>

using namespace std;

char* number[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

int countnum[27];

bool isInclude(int p)
{
	for (int i = 0; i < strlen(number[p]); i++)
	{
		char ch = number[p][i];

		if (countnum[ch - 'A'] == 0)
		{
			return false;
		}
	}
	return true;
}

void modify(int p, int d)
{
	for (int i = 0; i < strlen(number[p]); i++)
	{
		countnum[number[p][i] - 'A'] += d;
	}
}

bool finished()
{
	for (int i = 0; i < 27; i++)
	{
		if (countnum[i] != 0)
		{
			return false;
		}
	}
	return true;
}

string result;

void solve(int what)
{
	if (finished())
	{
		return;
	}
	if (what > 9)
	{
		return;
	}
	for (int i = what; i < 10; i++)
	{
		if (isInclude(i))
		{
			result.push_back(i + '0');
			modify(i, -1);
			solve(i);
			if (finished())
			{
				return;
			}
			modify(i, 1);
			result.pop_back();
		}
		else
		{
			solve(what + 1);
			if (finished())
			{
				return;
			}
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		char str[4000] = { 0, };
		result = "";
		memset(countnum, 0, 27 * sizeof(int));
		scanf("%s", str);
		for (int i = 0; str[i]; i++)
		{
			countnum[str[i] - 'A']++;
		}
		solve(0);
		printf("Case #%d: %s\n", i, result.c_str());
	}
	return 0;
}