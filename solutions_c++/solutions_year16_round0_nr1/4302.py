#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int hadd(int *, int *, int);
	char aa[1000];
	int a[1000],b[1000], n;
	scanf("%d", &n);
	for (int kk = 0;kk<n;kk++)
	{
		bool have[10];
		int j = 1000, con = 0;
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(have, 0, sizeof(have));
		scanf("%s", aa);
		int len = strlen(aa);
		for (int i = 0;i < len;i++)
		{
			a[i] = aa[len - i - 1] - '0';
			b[i] = a[i];
			if (!have[a[i]])
			{
				have[a[i]] = 1;
				con++;
			}
		}
		while (con != 10 && --j>0)
		{
			len = len + hadd(a, b, len);
			for (int i = len - 1;i >= 0;i--)
				if (!have[a[i]])
				{
					have[a[i]] = 1;
					con++;
				}

		}
		if (con == 10)
		{
			printf("Case #%d: ", kk + 1);
			for (int i = len - 1;i >= 0;i--)
				printf("%d", a[i]);
			printf("\n");
		}
		else
			printf("Case #%d: INSOMNIA\n", kk + 1);
	}
	return 0;
}

int hadd(int *re, int *dq, int len)
{
	int jw = 0, i, retu = 0;

	for (i = 0;i <= len;i++)
	{
		if (i == len&&jw != 0) retu = 1;
		re[i] = dq[i] + re[i] + jw;
		jw = re[i] / 10;
		re[i] = re[i] % 10;
	}
	return retu;
}

