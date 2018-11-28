#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

char buffer[1005];
char ans[3000];

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out3.txt", "w", stdout);
	int t;
	
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cin >> buffer;
		for (int j = 0; j < 3000; j++)
		{
			ans[j] = '\0';
		}

		cout << "Case #" << i + 1 << ": ";

		int r = 1500;
		int l = 1500;
		ans[r] = buffer[0];

		for (int j = 1; j < strlen(buffer); j++)
		{
			if (buffer[j] >= ans[l])
			{
				l--;
				ans[l] = buffer[j];
			}
			else
			{
				r++;
				ans[r] = buffer[j];
			}
		}
		cout << (ans + l);

		cout << endl;
	}

	return 0;
}