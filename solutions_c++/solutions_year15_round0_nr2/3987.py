//By Toxyxer
#include <cstdio>
#include <iostream>

int pancakes()
{
	int d, tab[1001], out, max=0;
	scanf("%d", &d);

	for(int i = 0; i < d; i++)
	{
		scanf("%d", &tab[i]);
		if(tab[i]>max)
			max=tab[i];
	}

	out=max;

	for(int i = 1; i < max; i++)
	{
		int special=0;
		for(int j = 0; j < d; j++)
			special += tab[j]/i + (tab[j]%i > 0) - 1;
		
		if(special+i<out)
			out=special+i;
	}
	return out;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
		printf("Case #%d: %d\n", i, pancakes());
}