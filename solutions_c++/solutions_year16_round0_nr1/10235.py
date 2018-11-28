#include "bits/stdc++.h"

int cases;

int main(int argc, char const *argv[])
{
	scanf("%d", &cases);
	int n = 1; 
	int N;
	int digits[10];
	for (int z = 0; z < 10; ++z)
	{
		digits[z] = -1;
	}
	while(cases)
	{
		scanf("%d", &N);
		int mult = 2;
		int unit = -1;
		int dig = 0, number = N;
		int start = N, loop = 0;
		//conta os digitos de N
		int fin = 0, added = 0;
		//verifica quais os digitos de N
		while(!fin){
			dig = 0;
			int numb = number;
			while(numb)
			{
				numb /= 10;
				++dig;
			}
			//printf("dig = %d\n", dig);
			numb = number;
			for (int i = 0; i < dig; ++i)
			{
				if(i > 0 && dig > 1) numb /= 10;
				unit = numb % 10;
				//printf("unit = %d\n", unit);
				//somente adiciona no array se for diferente de -1 e nao existir no array
				//verifica se existe no array
				int exist = 0;
				for (int v = 0; v < 10; ++v)
				{
					if(digits[v] == unit) exist = 1;
				}
				if(exist) continue;
				for (int j = 0; j < 10; ++j)
				{
					if (digits[j] == -1)
					{
						digits[j] = unit;
						added = 1;

					}
					if(added) break;
				}

				--added;
				
			}
			if(!N) 
			{
				loop = 1;
				break;
			}
			int found = 0;
			for (int k = 0; k < 10; ++k)
			{
				//printf("digits[%d] = %d\n", k, digits[k]);
				if(digits[k] == -1) found = 1;
			}
			if (found == 0)break;
			else 
			{
				number = N;
				number *= mult;
				//printf("New number = %d\n", number);
			}
			if(start == number)
			{
				loop = 1;
				break;
			}
			++mult;
		}

		if(loop) printf("Case #%d: INSOMNIA\n", n);
		else printf("Case #%d: %d\n", n, number);
		--cases;
		++n;
		for (int f = 0; f < 10; ++f)
		{
			digits[f] = -1;
		}
	}
	return 0;
}