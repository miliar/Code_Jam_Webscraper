#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
	FILE *stream;
	freopen_s(&stream, "C:\\//Users\\Mingzhi\\Downloads\\A-small-attempt0.in", "r", stdin);
	freopen_s(&stream, "C:\\output.txt", "w", stdout);
	int T;
	scanf_s("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int S, b[1001]; char a[1001];
		scanf_s("%d", &S); scanf_s("%s", &a, 1001);
		for (int j = 0; j <= S; j++)
			b[j] = a[j] - 48;
		int f = b[0], cnt = 0;
		for (int j = 1; j <= S; j++)
		{
			if (f < j)
			{
				cnt += j - f;
				f = j;
			}
			f += b[j];
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}