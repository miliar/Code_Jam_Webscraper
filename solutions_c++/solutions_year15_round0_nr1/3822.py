#include <bits/stdc++.h>

#define For(i, a, b) for(int i=(a); i<(b); ++i)
#define INF 1000000000
#define MP make_pair

using namespace std;

typedef pair <int, int> ii;
typedef long long ll;

char a[1005];

int main()
{
	//std::ios_base::sync_with_stdio(false);

	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--)
	{
		int n;
		scanf("%d %s", &n, a);

		int ppl = 0, ans = 0;
		For(i, 0, n+1)
		{
			if (a[i]-'0')
			{
				if (ppl < i)
				{
					ans += i-ppl;
					ppl = i + a[i]-'0';
				}
				else
					ppl += a[i]-'0';
			}
		}

		printf("Case #%d: %d\n", caso++, ans);
			
	}

	return 0;
}