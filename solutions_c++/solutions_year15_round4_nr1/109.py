#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>

using namespace std;

char s[200][200];

int main()
{
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; k++)
	{
		int r, c;
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; i++)
		{
			scanf("%s", s[i]);
		}
		int all = 0;
		for (int i = 0; i < r; i++)
		{
			for (int ii = 0; ii < c; ii++)
			{
				if (s[i][ii] != '.')
				{
					int k = 2;
					for (int j = 0; j < r; j++)
					{
						if (j != i)
						{
							if (s[j][ii] != '.')
							{
								if (j < i)
								{
									if (s[i][ii] == '^')
									{
										k = 0;
										break;
									}
									else
									{
										k = 1;
									}
								}
								else
								{
									if (s[i][ii] == 'v')
									{
										k = 0;
										break;
									}
									else
									{
										k = 1;
									}
								}
							}
						}
					}
					if (k > 0)
					{
						for (int j = 0; j < c; j++)
						{
							if (j != ii)
							{
								if (s[i][j] != '.')
								{
									if (j < ii)
									{
										if (s[i][ii] == '<')
										{
											k = 0;
											break;
										}
										else
										{
											k = 1;
										}
									}
									else
									{
										if (s[i][ii] == '>')
										{
											k = 0;
											break;
										}
										else
										{
											k = 1;
										}
									}
								}
							}
						}
					}
					if (k == 2)
					{
						all = -1;
						break;
					}
					else
					{
						all += k;
					}
				}
			}
		}
		if (all < 0)
		{
			printf("Case #%d: IMPOSSIBLE\n", k + 1);
		}
		else
		{
			printf("Case #%d: %d\n", k + 1, all);
		}
	}
	return 0;
}
