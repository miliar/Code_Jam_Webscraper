# include <stdio.h>
# include <math.h>
bool f(int x)
{
	int a=x, sum=0;
	while (a)
	{
		sum=sum*10+a%10;
		a/=10;
	//	printf("%d %d\n", a, sum);
	}
//	printf("%d %d\n", sum, x);
	if (sum==x)
		return true;
	else
		return false;
}
bool s(int i)
{
	int x = sqrt((double)i);
	if (x*x==i&&f(x))
		return true;
	else
		return false;
}
int main()
{
	int n, N, a, b, i, count;
//	printf("%d %d\n",f(121), s(121));
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &n);
	N=1;
	while (n--)
	{
		count = 0;
		scanf("%d%d", &a, &b);
		for (i = a; i<=b; i++)
		{
			if (f(i)&&s(i))
				count++;
		//	printf("i:%d  %d %d\n",i,f(i), s(i));
		}
		printf("Case #%d: %d\n", N++, count);
	}
	return 0;
}