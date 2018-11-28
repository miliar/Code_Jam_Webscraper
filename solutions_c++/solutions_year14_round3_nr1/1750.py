#include<stdio.h>

int gcd(int a, int b)
{
	return b == 0 ? a : gcd(b, a%b);
}

int main()
{
	int p, q, t, ca, r;
	scanf("%d", &t);
	for (ca = 1; ca <= t; ca++)
	{
		scanf("%d/%d", &p, &q);
		bool err = false;
		r = gcd(p, q);
		p /= r;
		q /= r;
		if ((q&(q - 1)) != 0)
			err = true;
		else
		{
			r = 0;
			while (q > p)
			{
				r++;
				q /= 2;
			}
		}
		printf("Case #%d: ", ca);
		if (err)
		{
			puts("impossible");
		}
		else
		{
			printf("%d\n", r);
		}
	}
	return 0;
}