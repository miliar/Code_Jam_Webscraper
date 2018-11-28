#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;
int d[10] = { 0, 2, 4, 6, 8, 1, 3, 5, 7, 9 };
char digits[][10] = { "ZERO", "TWO", "FOUR", "SIX", "EIGHT", "ONE", "THREE", "FIVE", "SEVEN", "NINE" };
int n;
char s[2010];
int c[30] = { 0 };


int mincount(char* digit)
{
	int min = 20000;
	int len = strlen(digit);

	for (int i = 0; i < len; i++)
	{
		if (c[digit[i] - 'A'] < min)
			min = c[digit[i] - 'A'];
	}
	for (int i = 0; i < len; i++)
	{
		c[digit[i] - 'A'] -= min;
	}
	return min;
}

int main()
{
	
	scanf("%d", &n);
	for (int x = 0; x < n; x++)
	{
		vector<int> res;
		scanf("%s", s);
		int len = strlen(s);
		for (int i = 0; i < len; i++)
			c[s[i] - 'A']++;
		printf("Case #%d: ", x+1);
		for (int i = 0; i < 10; i++)
		{
			int min = mincount(digits[i]);
			for (int j = 0; j < min; j++)
				res.push_back(d[i]);
		}
		sort(res.begin(), res.end());
		for (int j = 0; j < res.size(); j++)
			printf("%d", res[j]);
			printf("\n");
	}
	return 0;
}