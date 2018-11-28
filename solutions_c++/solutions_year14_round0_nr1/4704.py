#include <cstdio>
const int Len = 16;
int A[Len+5][2];
int a, b;
int main()
{
	//freopen("E:\\My Code\\GCJ\\QR\\A-small-attempt0.in", "r", stdin);
	//freopen("E:\\My Code\\GCJ\\QR\\A-small-attempt0.out", "w", stdout);
	int T;
	int Case = 1;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &a);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				int num;
				scanf("%d", &num);
				A[num][0] = i+1;
			}
		scanf("%d", &b);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				int num;
				scanf("%d", &num);
				A[num][1] = i+1;
			}
		int ans = -1;
		for (int i = 1; i <= 16; ++i)
			if (A[i][0] == a && A[i][1] == b)
			{
				if (ans == -1) ans = i;
				else ans = 17;
			}
			printf("Case #%d: ", Case++);
		if (ans == -1) puts("Volunteer cheated!");
		else if (ans < 17) printf("%d\n", ans);
		else puts("Bad magician!");
	}
	return 0;
}