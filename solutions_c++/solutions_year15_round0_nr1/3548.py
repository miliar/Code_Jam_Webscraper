// ConsoleApplication2.cpp : 定義主控台應用程式的進入點。
//
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>

int T, Sn, sum = 0, add = 0, _data = 0;
char S[1001];

int main() {

	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	std::cin >> T;
	while (T--)
	{
		std::cin >> Sn >> S;

		for (int i = 0; i <= Sn; i++)
		{
			if (i > sum)
			{
				add += i - sum;
				sum += i - sum;
			}
			sum += (int)S[i] - 48;
		}
			
		printf_s("Case #%d: %d\n", ++_data, add);
		
		sum = 0;
		add = 0;
	}
	return 0;
}