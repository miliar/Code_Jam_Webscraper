#include <cstdio>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstringt.h>
#include <string>

using namespace std;

char Buff[2000];

void domain()
{
	string S;
	int K = 0;;

	gets(Buff);

	int bL = strlen(Buff);

	bool hasSpace = false;

	for (int i = 0; i < bL; ++i)
	{
		if (Buff[i] == ' ')
		{
			hasSpace = true;
			continue;
		}

		if (!hasSpace)
		{
			S = S + Buff[i];
		}
		else
		{
			K = K * 10 + Buff[i] - '0';
		}
	}

	int sum = 0;

	for (int i = 0; i + K <= S.length(); ++i)
	{
		if (S[i] == '+')	continue;
		++ sum;
		for (int j = 0; j < K; ++j)
		{
			if (S[i+j] == '+')
			{
				S[i+j] = '-';
			}
			else
			{
				S[i+j] = '+';
			}
		}
	}

	bool flag = true;

	for (int i = 0; i < S.length(); ++i)
	{
		if (S[i] == '-')
		{
			flag = false;
			break;
		}
	}

	if (flag)
	{
		cout << sum << endl;
	}
	else
	{
		cout << "IMPOSSIBLE" << endl;
	}
}

int main()
{
	int T;
	cin.sync_with_stdio(false);
	scanf("%d\n", &T);

	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		domain();
	}

	return 0;
}