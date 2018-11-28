#include <stdio.h>
#include <vector>
#include <string.h>

bool inline isPalindrome(long long num)
{
	register char buf[20];
	sprintf(buf, "%lld", num);
	int len = strlen(buf);
	if (len % 2 != 0)
	{
		int mid = ((len + 1) / 2);
		for(register int j = 0; j < mid; j += 1)
		{
			if (buf[j] != buf[len - 1 - j])
			{
				return false;
			}
		}
			
		return true;
	}
	else 
	{
		int mid = len / 2;
		for(register int j = 0; j < mid; j += 1)
		{
			if (buf[j] != buf[len - 1 - j])
			{
				return false;
			}
		}
			
		return true;
	}
}

void main(void)
{
	register long long a = 1;
	register long long b = 1000000000000000;
	register std::vector<long long> fList;
	for(;a < b; a += 1)
	{
		if (isPalindrome(a))
		{
			if (isPalindrome(a*a))
			{
				fList.push_back(a*a);
			}
		}
		if ((a * a) > b) break;
	}
	
	int T;
	scanf("%d", &T);
	unsigned int len = fList.size();
	for(int cases = 1; cases <= T; cases += 1)
	{
		long long S,E;
		scanf("%lld %lld", &S, &E);
		int count = 0;
		for(register unsigned int i = 0; i < fList.size(); i += 1)
		{
			long long num = fList.at(i);
			if (num >= S && num <= E)
			{
				count += 1;
			}
		}
		printf("Case #%d: %d\n", cases, count);
	}
}