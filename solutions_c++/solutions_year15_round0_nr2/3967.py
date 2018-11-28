#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int P[5000000];

bool compare(int a, int b)
{
	return a > b;
}

int main()
{
	FILE *stream;
	freopen_s(&stream, "C:\\Users\\Mingzhi\\Downloads\\B-large.in", "r", stdin);
	freopen_s(&stream, "C:\\output.txt", "w", stdout);
	int T;
	scanf_s("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int D, Time = 0;
		scanf_s("%d", &D);
		for (int j = 0; j < D; j++)
			scanf_s("%d", &P[j]);
		sort(P, P + D, compare);
		int mi = P[0], ma = P[0];
		for (int j = 2; j < ma; j++)
		{
			Time = j;
			for (int k = 0; k < D; k++)
			{
				Time += P[k] / j;
				if (P[k] % j == 0) Time--;
			}
			if (mi > Time) mi = Time;
		}
		printf("Case #%d: %d\n", i, mi);
	}
	return 0;
}