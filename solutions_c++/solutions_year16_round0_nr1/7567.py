#include <iostream>
#include <cstdio>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS

int T, N;

bool allSeen(bool* seenDigits)
{
	for (int i = 0; i < 10; i++)
	{
		if (seenDigits[i] == false)
		{
			return false;
		}
	}
	return true;
}

long long int iterate(long long int originalNumber, int index, bool* seenDigits)
{
	long long int result = originalNumber * index;
	long long int resultCopy = result;
	while (resultCopy > 0)
	{
		seenDigits[resultCopy % 10] = true;
		resultCopy = resultCopy / 10;
	}
	return result;
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
		long long int result = 0;
		scanf_s("%d", &N);
		long long int curNum = N;
		bool seenDigits[10];
		for (int j = 0; j < 10; j++)
		{
			seenDigits[j] = false;
		}
		
		if (N == 0)
		{
			printf("Case #%d: INSOMNIA\n", i + 1);
		}
		else
		{
			int iterationCount = 1;
			while (!allSeen(seenDigits))
			{
				result = iterate(N, iterationCount, seenDigits);
				iterationCount++;
			}


			printf("Case #%d: %lld\n", i + 1, result);
		}
	}
	return 0;
}