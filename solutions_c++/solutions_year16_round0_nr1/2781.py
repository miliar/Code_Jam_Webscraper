#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>

using namespace std;

int main()
{
	char U[20];
	int num[15];
	while(~scanf("%s", U))
	{
		int _U = strlen(U);
		memset(num, 0, sizeof(num));
		int pos = -1;
		for(int i = 0; i < _U; i++)
		{
			int u = U[i] - '0';
			num[u] ++;
			if(num[u] == 3)
			{
				pos = i;
				break;
			}
		}
		if(pos == -1)
		{
			printf("%s\n", U);
			continue;
		}
		for(int i = pos; i >= 0; i--)
		{
			int k = -1;
			for(int j = 0; j < (U[i] - '0'); j++)
			{
				if(num[j] < 2) k = j;
			}
			num[U[i] - '0']--;
			if(~k)
			{
				U[i] = '0' + k;
				num[k]++;
				pos = i + 1;
				break;
			}
		}
		int x = 9;
		for(int i = pos; i < _U; i++)
		{
			while(num[x] == 2) x--;
			U[i] = '0' + x;
			num[x]++;
		}
		int s = 0;
		while(s < _U - 1 && U[s] == '0') s++;
		printf("%s\n", U + s);
	}
    return 0;
}

