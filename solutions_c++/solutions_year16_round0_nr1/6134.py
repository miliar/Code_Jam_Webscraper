#include <stdio.h>

int main()
{
	static const size_t digit_size = 10;
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int n = 0;scanf("%d",&n);
		size_t digits[digit_size] = { 0 },count = 0;
		unsigned long long ans = (unsigned long long)(-1);
		for(unsigned long long x = n;digit_size != count && x != 0;x += n)
		{
			for(unsigned long long t = x;t != 0;t /= 10)
			{
				unsigned int d = (unsigned int)(t%10);
				if(0 == digits[d]) ++count,digits[d] = 1;
				if(digit_size == count) { ans = x;break; }
			}
		}
		if((unsigned long long)(-1) != ans) printf("Case #%d: %I64u\n",iCases,ans);
		else printf("Case #%d: INSOMNIA\n",iCases);
	}
	return 0;
}
