#include <bits/stdc++.h>

using namespace std;

int t;
char s[200];

void swapp(int st, int en)
{
	// printf("swapp (%d,%d)\n",st,en);
	int i = st;
	int j = en;
	while (i <= j)
	{
		if (s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
		if (i != j)
		{
			if (s[j] == '+')
				s[j] = '-';
			else
				s[j] = '+';
		}
		swap(s[i], s[j]);
		i++;
		j--;
	}
	// printf("new s: %s\n",s);
}

int main(void)
{
	scanf("%d",&t);
	for (int cases = 1; cases <= t; ++cases)
	{
		scanf("%s",s);
		int len = strlen(s);
		int oper = 0;
		for (int i = len - 1; i >= 0; --i)
		{
			if (s[i] == '-' && s[0] == '-')
			{
				oper++;
				swapp(0, i);
			}
			else if (s[i] == '-')
			{
				for (int j = i; j >= 0; --j)
				{
					if (s[j] == '+')
					{
						oper += 2;
						swapp(0, j);
						swapp(0, i);
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",cases,oper);
	}
	return 0;
}