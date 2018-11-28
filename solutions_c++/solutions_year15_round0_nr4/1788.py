#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
	FILE *stream;
	freopen_s(&stream, "C:\\Users\\Mingzhi\\Downloads\\D-small-attempt1.in", "r", stdin);
	freopen_s(&stream, "C:\\output.txt", "w", stdout);
	int T;
	scanf_s("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int X, R, C;
		scanf_s("%d%d%d", &X, &R, &C);
		if (X == 1) printf("Case #%d: GABRIEL\n", i);
		else if (X == 2)
		{
			if (R*C % 2 == 0) printf("Case #%d: GABRIEL\n", i);
			else printf("Case #%d: RICHARD\n", i);
		}
		else if (X == 3)
		{
			if ((R==3 && C>1) || (R>1 && C==3)) printf("Case #%d: GABRIEL\n", i);
			else printf("Case #%d: RICHARD\n", i);
		}
		else if (X == 4)
		{
			if ((R == 4 && C > 2) || (R > 2 && C == 4)) printf("Case #%d: GABRIEL\n", i);
			else printf("Case #%d: RICHARD\n", i);
		}
	}
	return 0;
}