#include <stdio.h>
#include <math.h>
int f(int n)
{
	int t=0,m=n;
	while(m)
	{
		t*=10;
		t+=m%10;
		m/=10;
	}
	return t==n;
}
int isSqrt(int n)
{
      for(int i=1;n>0;i+=2) 
             n-=i;
      return 0 == n;
}
int main()
{
	#ifndef CYDONIA_DEBUG
	freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
	#endif
	int t, n, m, i;
	int c=1;
    scanf("%d", &t);
    while (t--)
	{
		scanf("%d%d", &n, &m);
		int a=0;
		for(i=n;i<=m;i++)
			{
			if(f(i) && isSqrt(i) && f(sqrt(i))){
				a++;}
			}
	printf("Case #%d: %d\n",c++,a);
	}
	return 0;
}