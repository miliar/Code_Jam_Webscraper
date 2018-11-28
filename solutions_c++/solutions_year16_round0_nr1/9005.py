#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define FILE "test"

void out(int ans)
{
	if (ans == -1)
	{
		printf("INSOMNIA\n");
	}
	else
	{
		printf("%d\n", ans);
	}
}

int main()
{
  freopen(FILE".in", "r", stdin);
  freopen(FILE".out", "w", stdout);
  srand(time(0));
	int t;
	cin >> t;
	int Case = 0;
	while (t--)
	{
		int n;
		scanf("%d", &n);
		int n1 = n;
		printf("Case #%d: ", (++Case));
		vector < bool > used(10, false);
		if (n == 0)
		{
			out(-1);
			continue;
		}
		while (true)
		{
			int x = n;
			while (x > 0)
			{
				used[x % 10] = true;
				x /= 10;
			}
			bool f = true;
			for (int j = 0; j < 10; j++)
				if (!used[j])
					f = false;
			if (f) break;
			n += n1;
		}
		out(n);
	}
}
