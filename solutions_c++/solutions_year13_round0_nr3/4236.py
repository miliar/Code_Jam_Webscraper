#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<cmath>
#define max 10000000

using namespace std;
typedef long long int LL;
int a[max + 10];
int check(LL x)
{
	LL s[40];
	int i = 0,j;
	while(x)
	{
		s[i++] = x % 10;
		x /= 10;
	}
	for(j=0;j<i/2;j++)
		if(s[j] != s[i-j-1])
			return 0;
	return 1;
}

void calc()
{
	LL i;
	a[0] = 0;
	int count=0;
	for(i=1;i<=max;i++)
	{
		LL x = i * i;
		if(check(i) && check(x))
			count++;
		a[i] = count;
	}
}
int main()
{
	calc();
	int tc,t,j;
	scanf("%d",&tc);
	for(t=1;t<=tc;t++)
	{
		LL x,y;
		scanf("%lld%lld",&x,&y);
		LL e = sqrt(x);
		if(e * e == x)
			e--;
		LL q = sqrt(y);
		printf("Case #%d: %d\n",t,a[q] - a[e]);
	}
	return 0;
}
