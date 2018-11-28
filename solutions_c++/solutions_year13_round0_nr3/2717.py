#include <stdio.h>
#include <math.h>

bool is_palindrome(long long x)
{
	char str[64], len = 0;
	while(x)
	{
		str[len++] = x % 10;
		x /= 10;
	}
	int l = 0, h = len - 1;
	while(l < h)
	{
		if(str[l] != str[h])
		{
			return false;
		}
		l++;
		h--;
	}
	return true;
}

int main()
{
	int T, t;
	long long low, high, root, num, cnt = 0;
	scanf("%d", &T);
	for(t = 0; t < T; t++)
	{
		scanf("%lld %lld", &low, &high);
		cnt = 0;
		root = sqrt((double)low);
		while(root * root < low) root++;
		while(true)
		{
			num = root * root;
			if(num > high) break;
			if(is_palindrome(root) && is_palindrome(num)) cnt++;
			root++;
		}
		printf("Case #%d: %d\n", t + 1, cnt);
	}

	return 0;
}