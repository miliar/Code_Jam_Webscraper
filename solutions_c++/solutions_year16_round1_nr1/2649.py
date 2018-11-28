#include <bits/stdc++.h>

#define For(i, a, b) for(int i=(a); i<(b); ++i)
#define INF 1000000000
#define MP make_pair

using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

char s[1005];

int main()
{
	//std::ios_base::sync_with_stdio(false);

	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--)
	{
		scanf("%s", s);
		int n = strlen(s);

		deque <char> ans;
		ans.push_back(s[0]);
		For(i, 1, n)
		{
			if (s[i] >= ans[0])
				ans.push_front(s[i]);
			else
				ans.push_back(s[i]);
		}

		printf("Case #%d: ", caso++);
		For(i, 0, (int)ans.size())
			printf("%c", ans[i]);
		printf("\n");
	}

	return 0;
}