#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

bool isPalindrome(long long int n)
{
	char num[100+10];
	int i = 0, j = 0;

	while(n != 0)
	{
		num[i++] = n%10 + '0';
		n /= 10;
	}

	--i;
	while(i > j)
	{
		if(num[i] != num[j])
			return 0;
		--i; ++j;
	}
	
	return 1;
}

int main()
{
	int t, a, b, count;
	long long int n;
	
	scanf("%d", &t);
	for(int test=1; test<=t; ++test)
	{
		count = 0;
		scanf("%d %d", &a, &b);
		for(int i=ceil(sqrt(a)); i<=floor(sqrt(b)); ++i)
		{
			n = i*i;
			if(isPalindrome(i) && isPalindrome(n))
				++count;
		}
		
		printf("Case #%d: %d\n", test, count);
	}
	
	return 0;
}