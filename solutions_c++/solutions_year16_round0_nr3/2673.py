#include <stdio.h>
#include <math.h>

int T, N, J;
long long arr[10];
int cnt;
long long s, e;

long long calc(int n) //s to base n
{
	long long from = s;
	long long to = 0;

	for(int i = 0; from != 0; i++)
	{
		if((from & 1) == 1)
		{
			to += pow((double)n, i);
		}
		from = from >> 1;
	}

	return to;
}

bool check(int n) //n base
{
	long long num = s;
	if(n != 2)
	{
		num = calc(n);
	}

	if(num % 2 == 0)
	{
		arr[n-1] = 2;
		return true;
	}
	for(int i = 3; i <= sqrt((double)num); i+=2)
	{
		if(num % i == 0)
		{
			arr[n-1] = i;
			return true; 
		}
	}

	return false;
}

long long toBinary(long long n)
{
	long long from = n;
	long long to = 0;
	for(int i = 0; from != 0; i++)
	{
		if((from & (long long)1) == 1)
		{
			to += (long long)pow(10.0, i);
		}
		from = from >> (long long)1;
	}
	return to;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for(int cs = 1; cs <= T; cs++)
	{
		scanf("%d %d", &N, &J);
		printf("Case #%d:\n", cs);
		s = pow(2.0, N-1) + 1;
		e = pow(2.0, N) - 1;
		while(s <= e)
		{
			bool status = true;
			for(int i = 2; i <= 10; i++)
			{
				status &= check(i);
				if(status == false)
				{
					break;
				}
			}
			if(status == true)
			{
				arr[0] = toBinary(s);
				for(int j = 0; j < 10; j++)
				{
					printf("%lld ", arr[j]);
				}
				printf("\n");
				cnt++;
				if(cnt == J)
				{
					break;
				}
			}
			s += 2;
		}
	}
	
	return 0;
}