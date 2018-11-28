#include <iostream>
#include <stdio.h>
#include <list>

using namespace std;

list<char> str;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		char S[1000 + 1];
		cin >> S;
		int n = strlen(S);

		str.clear();
		str.push_back(S[0]);

		for (int i = 1; i < n; i++)
		{
			if (*str.begin() <= S[i])
			{
				str.push_front(S[i]);
			}
			else
			{
				str.push_back(S[i]);
			}
		}

		printf("Case #%d: ", t);
		for (auto i : str)
		{
			printf("%c", i);
		}
		printf("\n");
	}

	return 0;
}
