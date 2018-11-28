#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

long long T, N[1000000];
bool chars[10];

bool ifcharsempty()
{
	for (int i = 0; i < 10; ++i)
		if (!chars[i])
			return true;
	return false;
}

void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;

	for (int i = 0; i < T; ++i)
		cin >> N[i];

	for (int i = 0; i < T; ++i)
	{
		if (N[i] == 0)
		{
			printf("Case #%d: INSOMNIA\n", i + 1);
			goto a;
		}

		for (int j = 0; j < 10; ++j)
			chars[j] = false;
		
		int k;

		for (k = 1; ifcharsempty(); ++k)
		{
			long long temp = N[i] * k;

			while (temp > 0)
			{
				chars[temp % 10] = true;
				temp = temp / 10;
			}

			if (k > 1000)
			{
				printf("Case #%d: INSOMNIA\n", i + 1);
				goto a;
			}
		}

		printf("Case #%d: %d\n", i + 1, N[i] * (k - 1));

	a:{}
	}



	






}