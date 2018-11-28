#include <iostream>
#include <stdio.h>
#include <cstring>
#include <string>

using namespace std;

char stck[101];
int size;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T;
	scanf("%d", &T);
	int ts = 1;
	while (T--)
	{
		size = 0; 
		scanf("%s", stck);

		for (int i = 0; stck[i] != 0; ++i)
			++size;

		if (size == 1)
		{
			if (stck[0] == '-')
				printf("Case #%d: 1\n", ts++);
			else
				printf("Case #%d: 0\n", ts++);
		}
		else
		{
			long long ans = 0;
			for (int i = 0; i < size-1; ++i)
			{
				if (stck[i] != stck[i + 1])
				{
					++ans;
					if (stck[i] == '-')
						for (int j = 0; j < i + 1; ++j)
							stck[j] = '+';
					else // stck[i] == '+'
						for (int j = 0; j < i + 1; ++j)
							stck[j] = '-';

				}
			}

			if (stck[0] == '-')
				printf("Case #%d: %lld\n", ts++,ans+1);
			else
				printf("Case #%d: %lld\n", ts++,ans);
		}
	}


}