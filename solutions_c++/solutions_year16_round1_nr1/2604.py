/*The Last Word*/

#include<cstdio>
#include<cstring>
#include<string>

using namespace std;

char S[1024];

int main()
{
	int i, length, t, T;
	string ans;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%s", S);
		length = strlen(S);
		ans = S[0];
		for (i = 1; i < length; i++)
		{
			if (S[i] >= ans[0])
				ans = S[i] + ans;
			else
				ans = ans + S[i];
		}
		printf("Case #%d: %s\n", t, ans.c_str());
	}
	return 0;
}