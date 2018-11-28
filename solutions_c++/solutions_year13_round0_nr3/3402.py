#include<stdio.h>
int palindromes[100];
int isPalindrome(int num)
{
	char str[20] = {0};
	int site = 0;
	int i, half;

	while(num != 0)
	{
		str[site ++] = num%10 + 48;
		num /= 10;
	}
	site -- ;
	half = site/2;
	for(i = 0; i <= half; i ++)
	{
		if( str[i] != str[site-i])
			return 0;
	}
	return 1;
}
int main()
{
	int n, i, j, k, l;
	int size = 0;
	for(i = 1; i <= 1000; i ++)
	{
		if(isPalindrome(i) && isPalindrome(i*i) == 1)
		{
			palindromes[size ++] = i*i;
		}
	}
	int a, b;
	scanf("%d", &n);
	for(i = 1; i <= n; i ++)
	{
		scanf("%d %d", &a, &b);
		for(j = 0; j < size && palindromes[j] < a; j ++)
		{
		}
		j --;
		for(k = size-1; k >= j && palindromes[k] > b; k --)
		{
		}
		k ++;
		if( k-j > 1)
			printf("Case #%d: %d\n", i, k - j - 1);
		else
			printf("Case #%d: 0\n", i);
	}
	return 0;
}