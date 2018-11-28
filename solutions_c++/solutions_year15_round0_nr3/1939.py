#include <cstdio>
const int maxn = 160005;
const int v[4][4] = {{0, 1, 2, 3}, {1, 0, 3, 2}, {2, 3, 0, 1}, {3, 2, 1, 0}};
const int sgn[4][4] = {{0, 0, 0, 0}, {0, 1, 0, 1}, {0, 1, 1, 0}, {0, 0, 1, 1}};
long long l, x;
char buf[maxn];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%I64d%I64d%s", &l, &x, buf);
		printf("Case #%d: ", tt);
		if (l * x <= 160000)
		{
			for (int i = l; i < l * x; i++)
				buf[i] = buf[i % l];
			int nowv = 0, nows = 0, p1 = -1, p2 = -1;
			for (int i = 0; i < l * x; i++)
			{
				if (buf[i] == 'i')
					buf[i] = 1;
				else if (buf[i] == 'j')
					buf[i] = 2;
				else if (buf[i] == 'k')
					buf[i] = 3;
				int tv = v[nowv][buf[i]], ts = nows ^ sgn[nowv][buf[i]];
				if (tv == 1 && ts == 0)
				{
					p1 = i;
					break;
				}
				nowv = tv;
				nows = ts;
			}
			nowv = 0, nows = 0;
			for (int i = l * x - 1; i >= 0; i--)
			{
				if (buf[i] == 'i')
					buf[i] = 1;
				else if (buf[i] == 'j')
					buf[i] = 2;
				else if (buf[i] == 'k')
					buf[i] = 3;
				int tv = v[buf[i]][nowv], ts = nows ^ sgn[buf[i]][nowv];
				if (tv == 3 && ts == 0)
				{
					p2 = i;
					break;
				}
				nowv = tv;
				nows = ts;
			}
			if (p1 == -1 || p2 == -1)
			{
				printf("NO\n");
				continue;
			}
			nowv = 0, nows = 0;
			for (int i = p1 + 1; i < p2; i++)
			{
				if (buf[i] == 'i')
					buf[i] = 1;
				else if (buf[i] == 'j')
					buf[i] = 2;
				else if (buf[i] == 'k')
					buf[i] = 3;
				int tv = v[nowv][buf[i]], ts = nows ^ sgn[nowv][buf[i]];
				nowv = tv;
				nows = ts;
			}
			if (nowv == 2 && nows == 0)
				printf("YES\n");
			else
				printf("NO\n");
		}
	}
	return 0;
}
