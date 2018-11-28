#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int mas[701];
	for ( int i = 0; i < 701; i++)
		mas[i] = 0;
	for (int t = 0; t < T; t++)
	{
		int N, X;
		scanf("%d%d", &N, &X);
		for (int i = 0; i < N; i++)
		{
			int c;
			scanf("%d", &c);
			mas[c]++;
		}
		int res = 0;
		while (true)
		{
			int a = -1, b = -1;
			for (int i = 700; i >= 0; i--)
				if (mas[i] > 0)
				{
					a = i;
					mas[i]--;
					break;
				}
			if (a == -1)
				break;
			for (int i = 700; i >= 0; i--)
				if (mas[i] > 0 && i + a <= X)
				{
					b = i;
					mas[i]--;
					break;
				}
			res++;
		}
		printf("Case #%d: %d\n", t+1, res);
		
	}
	
	
	return 0;
}