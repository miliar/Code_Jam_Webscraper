#include <bits/stdc++.h>

using namespace std;

int n,r,s,p,t;
vector<char> ans;
bool cmp(char a, char b)
{
	if (a == 'P' && b == 'R')
		return true;
	if (a == 'S' && b == 'P')
		return true;
	if (a == 'R' && b == 'S')
		return true;
	return false;
}
bool solve(vector<char> ans)
{
	// for (int i = 0; i < ans.size(); ++i)
	// {
	// 	printf("%c ",ans[i]);
	// }
	// printf("\n");
	while (ans.size() > 1)
	{
		vector<char> tmp;
		for (int i = 0; i < ans.size(); i += 2)
		{
			if (cmp(ans[i], ans[i + 1]))
			{
				tmp.push_back(ans[i]);
			}
			else if (cmp(ans[i + 1], ans[i]))
			{
				tmp.push_back(ans[i + 1]);
			}
			else
			{
				return false;
			}
		}
		ans = tmp;
	}
	return true;
}
int main(void)
{
	scanf("%d",&t);
	for (int cases = 1; cases <= t; ++cases)
	{
		scanf("%d%d%d%d",&n,&r,&p,&s);
		vector<char> tmp;

		for (int i = 0; i < r; ++i)
		{
			tmp.push_back('R');
		}

		for (int i = 0; i < p; ++i)
		{
			tmp.push_back('P');
		}

		for (int i = 0; i < s; ++i)
		{
			tmp.push_back('S');
		}

		ans.clear();
		sort(tmp.begin(), tmp.end());
		do
		{
			if (solve(tmp))
			{
				ans = tmp;
				break;
			}
		}while(next_permutation(tmp.begin(), tmp.end()));

		printf("Case #%d: ",cases);
		if (ans.size() == 0)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			for (int i = 0; i < ans.size(); i ++)
			{
				printf("%c",ans[i]);
			}
			printf("\n");
		}
	}

	return 0;
}