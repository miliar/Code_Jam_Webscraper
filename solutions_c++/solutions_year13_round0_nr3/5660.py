#include <stdio.h>
#include <string.h>
#include <stdlib.h>

bool IsPalindrome(long long v)
{
    char s[30];
    sprintf(s, "%lld", v);
	int len = strlen(s);
	for(int k=0; k<len/2; ++k)
	{
		if(s[k] != s[len-1-k])
		{
			return false;
		}
	}
	return true;
}

int main(void)
{
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-small-attempt2.out", "w", stdout);
	int x,t;
	long long A,B;
	scanf("%d", &t);
	
	long long i,j;
	int ans;
	for(x=1; x<=t; ++x)
	{
	    scanf("%lld%lld", &A, &B);
		ans = 0;
		for(i=1; i*i<=B; ++i)
		{
			j = i*i;
			if(j>=A && IsPalindrome(i) && IsPalindrome(j))
			{
				ans++;
			}
		}
		printf("Case #%d: %d\n", x, ans);
	}
	
	return 0;
}
