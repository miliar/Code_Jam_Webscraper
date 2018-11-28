#define _CRT_SECURE_NO_WARNINGS

#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int main(int argc, char* argv[])
{
	freopen("in.txt", "rb", stdin);
	freopen("out.txt", "wb", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);

		const int MAX_S_LENGTH = 100;
		char S[MAX_S_LENGTH + 1];

		scanf("%s", S);

		int cnt = 0;
		int i = 1;
		
		while (S[i] != '\0')
		{
			if (S[i - 1] != S[i])
			{
				cnt++;
			}

			i++;
		}

		if (S[i - 1] == '-')
		{
			cnt++;
		}

		printf("%d\n", cnt);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
