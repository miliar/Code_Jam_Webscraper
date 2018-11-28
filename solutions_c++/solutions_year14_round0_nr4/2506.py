#include<cstdio>
#include<algorithm>

using namespace std;

double a[1000], b[1000];

int main()
{
	int t, n, i, j, ca;
	int ra, rb;
	scanf("%d", &t);
	for (ca = 1; ca <= t; ca++)
	{
		scanf("%d", &n);
		for (i = 0; i < n; i++) scanf("%lf", a + i);
		for (i = 0; i < n; i++) scanf("%lf", b + i);
		sort(a, a + n);
		sort(b, b + n);
		/*
		for (i = 0; i < n; i++)
		{
			printf("%.5lf ", a[i]);
		}
		putchar('\n');
		for (i = 0; i < n; i++)
		{
			printf("%.5lf ", b[i]);
		}
		putchar('\n');
		*/
		i = j = 0;
		rb = 0;
		while (i < n&&j < n)
		{
			while (j<n&&b[j]<a[i]) j++;
			if (j < n)
			{
				rb++;
				j++;
			}
			i++;
		}
		i = 0;
		j = n - 1;
		ra = 0;
		/*
		int x = n - 1;
		while (true)
		{
			int t = x;
			while (t > i && a[t] > b[j]) t--;
			//x-t must score
			ra += (x - t);
			x = t;
			if (a[i] > b[j]) 
			{
				ra++;
			}
			i++; 
			j--;
			if (i > t) break;
		}
		*/
		int t = 0;
		while (i < n)
		{
			if (a[i] > b[t])
			{
				t++;
				ra++;
			}
			i++;
		}
		printf("Case #%d: %d %d\n", ca, ra, n - rb);
	}
}