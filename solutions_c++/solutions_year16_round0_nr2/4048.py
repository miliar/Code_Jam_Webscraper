#if 0==0

#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>

using std::vector;
using std::string;

int main()
{
	vector<int> p;

	freopen("B-large.in", "r", stdin);
	freopen("B-large_mine.out", "w", stdout);

	char str[1000];
	char st[1000];

	int n;
	scanf("%d", &n);
	for (int i_case = 1 ; i_case <= n ; i_case++)
	{	
		scanf("%s", &str);

		int d = strlen(str);
		//printf("d=%d\n",d);
		int i_ans = 0;

		for (int i = 0 ; i < d - 1 ; i++)
		{
			strcpy(st, str);

			if (str[i] != str[i+1])
			{
				i_ans++;
				for (int j = 0 ; j <= i ; j++)
				{
					st[j] = ((str[i-j] == '-') ? '+' : '-');
				}
			}

			strcpy(str, st);
		}

		if (str[0] == '-') i_ans++;

		printf("Case #%d: ", i_case);
		printf("%d\n", i_ans);
	}

	return 0;
}

#endif