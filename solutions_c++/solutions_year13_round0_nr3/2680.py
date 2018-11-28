#include <cstdio>
#include <cmath>
int n;
int d[10];
double eps =1e-6;
bool ispal(int a)
{
	int temp = a, i  = 0, j;
	while (temp > 0)
	{
		d[i++] = temp%10;
		temp/=10;
	}
	for (j = 0; j < i/2; j++)
	{
		if (d[j] != d[i-1-j]) return false;
	}
	return true;
}
int main()
{
	int i, a, b, ra, rb, t, sum;
	double la, lb;
	scanf("%d", &n);
	for (t = 1; t <= n; t++)
	{
		scanf("%d %d", &a, &b);
		la = sqrt(double(a));
		lb = sqrt(double(b));
		ra = int(la);
		rb = int(lb);
		if (fabs(la-ra) > 1e-6) ra++;
		sum = 0;
		for (i = ra; i <= rb; i++)
		{
			if (ispal(i) && ispal(i*i)) 
			{
				//printf("%d %d\n", i, i*i);
				sum++; 
			}
		}
		printf("Case #%d: %d\n", t, sum);
	}
}
