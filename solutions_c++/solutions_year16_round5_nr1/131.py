#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
int main()
{
	freopen("a-large.in", "r", stdin);
	freopen("large.txt", "w", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		string s;
		cin >> s;
		int c1 = 0, c2 = 0, j1 = 0, j2 = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (i % 2 == 0)
			{
				if (s[i] == 'C')c1++;
				else j1++;
			}
			else
			{
				if (s[i] == 'C')c2++;
				else j2++;
			}
		}
		printf("Case #%d: %d\n", p, min(c1, c2) * 10 + min(j1, j2) * 10 + (max(c1, c2) - min(c1, c2)) * 5);
	}
}