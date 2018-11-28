#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <list>
#include <map>
#include <functional>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	int t;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	scanf("%d", &t);
	for (int z = 0;z < t;z++)
	{
		string s;
		cin >> s;
		int c = 0;
		int sl = s.length();
		while(1)
		{
			int idx = 1;

			for (;idx < sl; idx++)
			{
				if (s[idx] != s[idx - 1])
					break;
			}
			
			if (idx == sl && s[0] == '+')
				break;

			for (int i = 0;i < idx;i++)
			{
				if (s[i] == '-')
					s[i] = '+';
				else
					s[i] = '-';
			}
			c++;
		}
		printf("Case #%d: ", z + 1);
		printf("%d", c);
		printf("\n");
	}
	return 0;
}