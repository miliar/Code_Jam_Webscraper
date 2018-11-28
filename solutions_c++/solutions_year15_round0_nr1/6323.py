#include <iostream>
#include <cstdio>

int main()
{
	int32_t Z;	scanf("%d", &Z);
	for (int32_t q = 1; q <= Z; q++)
	{
		int32_t n, sta = 0, ret  = 0;
		char tab[1005];
		scanf("%d", &n);
		scanf("%s", tab);
		for (int32_t i = 0; i <= n; i++)
		{
			if (sta < i)
			{
				ret += i - sta;
				sta = i;	
			}
			sta += tab[i]-'0';
		}
		printf("Case #%d: %d\n", q, ret);
	}
	return 0;
}