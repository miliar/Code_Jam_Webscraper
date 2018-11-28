#include <iostream>
#include <stdio.h>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

char arr[1002];
int size;
int arp[30];
char str[3000];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T;
	scanf("%d", &T);
	int ts = 1;
	while (T--)
	{
		scanf("%s", arr);
		size = 0;
		memset(arp, 0, sizeof(arp));
		for (int i = 0; arr[i] != 0; ++i)
		{
			++size;
			++arp[arr[i] - 'A'];
		}

		printf("Case #%d: ", ts++);
		int initPoint = 1500, endPoint = 1501;
		char current = 'A';
		for (int i = 0; i < size; ++i)
		{
			if (current <= arr[i])
			{
				str[initPoint--] = arr[i];
				current = arr[i];
			}
			else
			{
				str[endPoint++] = arr[i];
			}
		}

		for (int i = initPoint + 1; i < endPoint; ++i)
			printf("%c", str[i]);
		printf("\n");
	}

}