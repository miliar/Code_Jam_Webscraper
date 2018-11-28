#include <bits/stdc++.h>
using namespace std;
bool panc[2000];

int t, s, k, ans;
char in[2000];
int main()
{
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		ans = 0;
		scanf(" %s", in);
		scanf("%d", &k);
		s = strlen(in);
		for (int i = 0; i < s; i++)
		{
			if (in[i] == '+') panc[i] = true;
			else panc[i] = false;
		}
		
		for (int i = 0; i + k <= s; i++)
		{	
			if (!panc[i])
			{
				for (int j = i; j < i+k; j++) panc[j] = !panc[j];
				ans++;
			}
		}
		bool works = true;
		for (int i = 0; i < s; i++)
		{
			if (!panc[i]) works = false;
		}
		printf("Case #%d: ", i);
		if (works) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
}