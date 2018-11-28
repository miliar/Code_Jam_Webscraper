#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t, ans;
	char s[105];

	scanf("%d", &t);

	for(int x = 1; x <= t; x++)
	{
		ans = 0;

		scanf("%s", s);

		int l = strlen(s);

		int b[l];

		for(int i = 0; i < l; i++)
			b[i] = (s[i] == '+' ? 1 : 0);

		int done = 0;

		while(!done)
		{
			int pos1 = -1, pos2 = -1;

			for(int i = l-1; i >= 0; i--)
			{
				if(!b[i])
				{
					pos1 = i;
					break;
				}
			}

			for(int i = pos1-1; i >= 0; i--)
			{
				if(b[i])
				{
					pos2 = i+1;
					break;
				}
			}

			if(pos1 == -1)
			{
				done = 1;
				continue;
			}

			if(pos1 == 0)
			{
				b[0] = 1;
			}

			if(b[0] == 1)
			{
				for(int i = pos2-1, j = 0; i >= j; i--, j++)
				{
					if(i == j)
					{
						b[i] = 1 - b[i];
					}
					else
					{
						int c = b[i];
						b[i] = b[j];
						b[j] = c;
						b[i] = 1 - b[i];
						b[j] = 1 - b[j];
					}
				}
			}
			else
			{
				if(pos2 == 0)
				{
					for(int i = 0; i <= pos1; i++)
						b[i] = 1;
				}
				else
				{
					for(int i = pos1, j = 0; i >= j; i--, j++)
					{
						if(i == j)
						{
							b[i] = 1 - b[i];
						}
						else
						{
							int c = b[i];
							b[i] = b[j];
							b[j] = c;
							b[i] = 1 - b[i];
							b[j] = 1 - b[j];
						}
					}
				}
			}

			ans++;

			//printf("ans %d\n", ans);
		}

		printf("Case #%d: %d\n", x, ans);
	}

	return 0;
}