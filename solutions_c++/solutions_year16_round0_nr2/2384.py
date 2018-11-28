#include <cstdio>
#include <cstring>
using namespace std;

int t;
char s[105];
char sTmp[105];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b_large_output.txt", "w+", stdout);
	scanf("%d", &t);
	int tc = 1;
	while (t--)
	{
		scanf("%s", s);
		int nSize = strlen(s);
		int nRes = 0;
		while (1)
		{
			int nStart = 0;
			int nEnd = nSize - 1;
			int nCnt = 0;
			for (int i = 0; i < nSize; ++i)
			{
				if (s[i] == '+')
					nCnt++;
				sTmp[i] = s[i];
			}
			if (nCnt == nSize)
			{
				printf("Case #%d: %d\n", tc++, nRes);
				break;
			}

			while (nEnd >= 0 && s[nEnd] == '+')
				nEnd--;

			bool bFlag = false;
			while (nStart < nSize && s[nStart] == '+')
			{
				sTmp[nStart] = '-';
				nStart++;
				bFlag = true;
			}
			if (bFlag)
				nRes++;

			for (int i = 0; i <= nEnd; ++i)
			{
				if (sTmp[nEnd - i] == '+')
					s[i] = '-';
				else
					s[i] = '+';
			}
			nRes++;
		}
	}
}