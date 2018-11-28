// Fair and Square.cpp : fichier projet principal.

#include "stdafx.h"

#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <conio.h>

using namespace std;

int main(void)
{
	int T;

	if (NULL == freopen("C-small-attempt0.in", "rt", stdin))
		return EXIT_FAILURE;

	if (NULL == freopen("C-small-attempt0.out", "wt", stdout))
		return EXIT_FAILURE;

	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		long long A, B;
		long count;

		cout << "Case #" << i << ": ";

		cin >> A >> B;

		count = 0;
		for (long long j = A; j <= B; ++j)
		{
			char buffer[100];
			stringstream ss;
			string reversed_str;

			sprintf(buffer, "%lld", j);
			ss << buffer;
			reversed_str = ss.str();
			reverse(reversed_str.begin(), reversed_str.end());
			if (ss.str() == reversed_str)
			{
				long long j1;

				j1 = sqrt(j);
				if (pow(j1, 2LL) == j)
				{
					char buffer1[100];
					stringstream ss1;
					string reversed_str1;

					sprintf(buffer1, "%lld", j1);
					ss1 << buffer1;
					reversed_str1 = ss1.str();
					reverse(reversed_str1.begin(), reversed_str1.end());
					if (ss1.str() == reversed_str1)
						++count;
				}
			}
		}

		cout << count << endl;
	}

    return EXIT_SUCCESS;
}
