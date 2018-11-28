#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
	FILE *stream;
	freopen_s(&stream, "C:\\Users\\Mingzhi\\Downloads\\D-small-attempt0.in", "r", stdin);
	freopen_s(&stream, "C:\\new\\Doutput.txt", "w", stdout);
	int T;
	scanf_s("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int K, C, S;
		scanf_s("%d%d%d", &K, &C, &S);
		printf("Case #%d:", i);
		if (K > C*S) printf(" IMPOSSIBLE");
		else for (int j = 1;j <= K;j++)
			printf(" %d", j);
		printf("\n");
	}
	return 0;
}