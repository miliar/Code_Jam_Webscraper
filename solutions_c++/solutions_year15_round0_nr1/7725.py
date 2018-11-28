#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
//#define getchar getchar_unlocked

int fast_integer()
{
    int set = 0, minus = 1;
    register char c = getchar();
    while(c < '0' || c >'9') 
	{
		if(c=='-')
		minus = -1;
		c = getchar();
	}
    while(c>='0' && c<='9')
    {
    	set = (set<<3) + (set<<1)+c-'0';
    	c = getchar();
    }
    return minus*set;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long int T, Smax, current, i, count = 0, ans = 0, quer = 1;
	T = fast_integer();
	while(T--)
	{
		Smax = fast_integer();
		count = 0; ans = 0;
		for(i = 0; i <= Smax; i++)
		{
			current = getchar() - '0';
			if(count >= i)
				count += current;
			else
			{
				ans += i - count;
				count += current + (i - count);
			}
		}
		getchar();
		printf("Case #%lld: %lld\n", quer++, ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
