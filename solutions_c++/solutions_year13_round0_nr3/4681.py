#include "stdio.h"
#define MAX 10000010
bool palindrome(long long a)
{
	long long b,c;
	c=a;
	b=0;
	while(c>0)
	{
		b = b*10 + c%10;
		c/=10;
	}
	return b==a;
}

int main(int argc, char const *argv[])
{
	long long int a1 ,b1;
	long long int numbers[100];
	int totalnos=0;
	int count=0;
	for(a1=1;a1<MAX;a1++)
	{
		if(palindrome(a1))
		{
			b1 =a1*a1;
			if(palindrome(b1))
			{
				numbers[totalnos]=b1;
				totalnos++;
			}
		}
	}
	int t;
	long long int a,b;
	scanf("%d",&t);
	for (int i = 1; i <= t; ++i)
	{
		count=0;
		scanf("%lld %lld",&a,&b);
		for (int j = 0; j < totalnos; ++j)
		{
			if(numbers[j]<=b&&numbers[j]>=a) count++;
		}
		printf("Case #%d: %d\n",i,count );
	}
	return 0;
}