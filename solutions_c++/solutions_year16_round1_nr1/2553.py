#include <bits/stdc++.h>

using namespace std;
#define MAX 1100

int t;
char in[MAX];
string s;

int main(void)
{
	scanf("%d",&t);
	for (int cases = 1; cases <= t; ++cases)
	{
		scanf("%s",in);
		s = in;

		deque<char> ans;
		ans.push_back(s[0]);
		for (int i = 1; i < s.size(); ++i)
		{
			if (ans.front() <= s[i])
				ans.push_front(s[i]);
			else
				ans.push_back(s[i]);
		}

		printf("Case #%d: ",cases);
		for (int i = 0; i < ans.size(); ++i)
		{
			printf("%c",ans[i]);
		}
		printf("\n");
	}
	return 0;
}