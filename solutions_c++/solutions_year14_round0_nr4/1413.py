#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("D-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	double a[1010], b[1010];
	int T, N;
	scanf("%d", &T);
	for(int Case = 1; Case <= T; Case++)
	{
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
		{
			scanf("%lf", &a[i]);
		}
		for(int i = 0; i < N; i++)
		{
			scanf("%lf", &b[i]);
		}
		sort(a, a + N);
		sort(b, b + N);
		printf("Case #%d:", Case);
		int la, ra, lb, rb;
		la = lb = 0;
		ra = rb = N - 1;
		int ans = 0;
		while(la <= ra)
		{
			if(a[ra] > b[rb])
			{
				ans++;
				ra--;
				rb--;
			}
			else
			{
				la++;
				rb--;
			}
		}
		printf(" %d", ans);
		ans = 0;
		lb = 0;
		rb = N - 1;
		for(int i = 0; i < N; i++)
		{
			if(a[i] > b[rb])	
			{
				//printf("%lf %lf\n", a[i], b[lb]);
				ans++;
				lb++;
			}
			else
			{
				for(int j = lb; j <= rb; j++)
				{
					if(a[i] < b[j])
					{
						for(int k = j; k < rb; k++)
						{
							b[k] = b[k + 1];
						}
						rb--;
						break;
					}
				}
			}
			//for(int j = lb; j <= rb; j++) printf("%lf ", b[j]);
			//printf("\n");
		}
		printf(" %d\n", ans);
	}
	return 0;
}
