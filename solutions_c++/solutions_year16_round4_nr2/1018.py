#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
using namespace std;
int n, m;
double a[1009];
double d[1009][1009];
double b[1009];
double res = 0;
double rb[1009];
void process()
{
	int i, j, k;
	for (i = 0; i <= m; i++)
		for (j = 0; j <= m; j++)
			d[i][j] = 0;
	d[0][0] = 1;
	for (i = 0; i < 2 * m; i++)
	{
		for (j = 0; j <= m; j++)
		{
			k = i + 1 - j;
			if (k >= 0 && k <= m)
			{
				if (j > 0)
					d[j][k] += d[j - 1][k] * (1-b[i]);
				if (k > 0)
					d[j][k] += d[j][k - 1] * b[i];
			}
		}
	}
	if (res < d[m][m])
	{
		res = d[m][m];
		for (i = 0; i < 2 * m; i++)
			rb[i] = b[i];
	}
}
int main()
{
	int t, tv;
	tv = 0;
	freopen("B-small-attempt2.in","rt",stdin);
	freopen("B-small-attempt2.out","wt",stdout);
	//freopen("A-large.in","rt",stdin);
	//freopen("A-large.out","wt",stdout);

	scanf("%d", &t);
	while (t--)
	{
		scanf("%d %d", &n,&m);
		int i, j, k;
		for (i = 0; i < n; i++)
			scanf("%lf", &a[i]);

		sort(a, a + n);
		for (j = 0; j < n; j++)
		{
			if (a[j] >= 0.5)
				break;
		}
		for (k = n - 1; k >= 0; k--)
			if (a[k] <= 0.5)
				break;
		m /= 2;
		int cnt = 0;
		res = -1;
		for (i = 0; i < (1 << n); i++)
		{
			j = 0;
			for (k = 0; k < n; k++)
				if (i&(1 << k))
					j++;
			if (j == m*2)
			{
				cnt = 0;
				for (k = 0; k < n; k++)
					if (i&(1 << k))
						b[cnt++] = a[k];
				process();
			}
		}
		tv++;
		printf("Case #%d: ", tv);
		printf("%.9lf\n",res);
		for (i = 0; i < 2*m; i++)
		{
//			printf("%lf ", rb[i]);
		}
//		printf("\n");
	}
}