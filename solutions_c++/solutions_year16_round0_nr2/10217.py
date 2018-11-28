#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

long long T;
string N[1000000];
bool chars[10];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;

	for (int i = 0; i < T; ++i)
		cin >> N[i];

	for (int i = 0; i < T; ++i)
	{
		int c = 0;
		char a = N[i][0];

		for (int j = 0; j < N[i].size(); ++j)
		{
			if (a != N[i][j])
				++c;

			a = N[i][j];
		}

		if (N[i].back() == '-')
			++c;
		

		printf("Case #%d: %d\n", i + 1, c);

	}


	return 0;
	






}