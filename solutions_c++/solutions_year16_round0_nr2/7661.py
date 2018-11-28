#include <iostream>
#include <cstdio>
using namespace std;

int T;

void flip(char* S, int index)
{
	for (int i = 0; i <= index; i++)
	{
		if (S[i] == '+')
		{
			S[i] = '-';
		}
		else
		{
			S[i] = '+';
		}
	}
}

int main()
{
	FILE* file;
	freopen_s(&file, "input.txt", "r", stdin);
	FILE* file_2;
	freopen_s(&file_2, "output.txt", "w", stdout);
	scanf_s("%d", &T);
	for (int i = 0; i < T; i++)
	{
		char S[100];
		scanf(" %s", S);
		int result = 0;

		int curIndex = strlen(S) - 1;
		while (1)
		{
			int firstNegative = curIndex;
			while (firstNegative >= 0 && S[firstNegative] != '-')
			{
				firstNegative--;
			}
			if (firstNegative < 0)
			{
				break;
			}

			flip(S, firstNegative);
			result++;
			curIndex = firstNegative;
		}

		printf("Case #%d: %d\n", i + 1, result);
	}
	return 0;
}