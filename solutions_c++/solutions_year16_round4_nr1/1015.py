#include<cstdio>
void rc(int i, int ps, int q)
{
	rc(i+1, ps*2, (q!=2)?1:);
	rc(i+1, ps*2+1);
}
int main()
{
	scanf("%d", &T);
	ms[0] = 1;
	for (int i = 1; i <= 12; ++i)
		ms[i] = ms[i-1] * 2;
	for (int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		scanf("%d", &n);
		scanf("%d%d%d", &r[n], &p[n], &s[n]);
		int flag = (r[n]+p[n]+s[n] != ms[n]);
		for (int i = n; i > 0; --i)
		{
			r[i-1] = (r[i]+s[i]-p[i])/2; // z
			s[i-1] = (s[i]+p[i]-r[i])/2; // s
			p[i-1] = (r[i]+p[i]-s[i])/2; // b
			if (r[i-1] < 0 || s[i-1] < 0 || p[i-1] < 0)
			{
				flag = 1;
				break;
			}
		}
		if (flag)
			puts("IMPOSSIBLE");
		else
		{
			int q = (s[0]?0:(p[0]?1:2));
			rc(0, 0, q);
			puts("");
		}
	}
	return 0;
}