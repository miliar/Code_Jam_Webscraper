#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int m[10010];

int main()
{
	FILE *stream;
	//freopen_s(&stream, "C:\\input.txt", "r", stdin);
	freopen_s(&stream, "C:\\Users\\Mingzhi\\Downloads\\A-large.in", "r", stdin);
	freopen_s(&stream, "C:\\output.txt", "w", stdout);
	int T;
	scanf_s("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int N, s1 = 0, s2 = 0, ma = 0;
		scanf_s("%d", &N);
		scanf_s("%d", &m[0]);
		for (int j = 1; j < N; j++)
		{
			scanf_s("%d", &m[j]);
			int t = m[j - 1] - m[j];
			if (t > 0) s1 += t;
			if (t > ma) ma = t;
		}
		for (int j = 0; j < N - 1; j++)
		{
			if (m[j] > ma) s2 += ma;
			else s2 += m[j];
		}
		printf("Case #%d: %d %d\n", i, s1, s2);
	}
	return 0;
}