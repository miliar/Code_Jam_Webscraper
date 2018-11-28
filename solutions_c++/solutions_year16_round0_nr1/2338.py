#include <cstdio>
#include <cstring>
using namespace std;

int t, n;
bool isVisited[10];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a_large_output.txt", "w+", stdout);
	scanf("%d", &t);
	int tc = 1;
	while (t--)
	{
		scanf("%d", &n);
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", tc++);
			continue;
		}
		memset(isVisited, false, sizeof(isVisited));
		int i = 1;
		int nCnt = 0;
		while (1)
		{
			int nTmp = n * i;
			while (nTmp)
			{
				int nRest = nTmp % 10;
				if (!isVisited[nRest])
				{
					isVisited[nRest] = true;
					nCnt++;
				}
				nTmp /= 10;
			}
			if (nCnt == 10)
			{
				printf("Case #%d: %d\n", tc++, n * i);
				break;
			}
			i++;
		}
	}
}