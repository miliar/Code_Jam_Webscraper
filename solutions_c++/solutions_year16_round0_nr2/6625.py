#include <iostream>
#include <cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
using namespace std;
typedef long long ll;

char S[105];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		int ans = 0;
		scanf("%s", S);
		int L = strlen(S);
		if (L == 1)
		{
			if (S[0] == '-')
				ans = 1;
		}
		else
		{

			for (int i = 1; i < L; ++i)
			{
				if (S[i] != S[i - 1])
					ans++;

			}
			if (S[L - 1] == '-')
				ans++;
		}
		
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}