//Mateusz Janczura
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector <int> vek;
pair <int, int> f(int a, int v)
{
	int i = 0;
	while(a <= v)
	{
		a += a - 1;
		i++;
	}
	return make_pair(i, a);
}
pair <int, int> kore(int k, int i)
{
	int j = i;
	while(j < vek.size())
	{
		if(k > vek[j]) 
		{
		//	printf("l");
			k += vek[j];
			j++;
		}
		else break;
	}
	return make_pair(j - i + 1, k);		
}
int main()
{
	int Z, i, li, wynik = 0, n, a;
	scanf("%d", &Z);
	for(li = 1; li <= Z; li++)
	{
		scanf("%d %d", &a, &n);
		vek.resize(n);
		for(i = 0; i < n; i++)
			scanf("%d", &vek[i]);
		if(a == 1) 
		{
			printf("Case #%d: %d\n", li, n);
		}
		else
		{
			sort(vek.begin(), vek.end());
			i = wynik = 0;
			while(i < n) 
			{
				if(a > vek[i]) 
				{
					a += vek[i];
					i++;
					//puts("?");
				}
				else
				{
					pair <int, int> 
						tp = f(a, vek[i]), 
						k  = kore(tp.second, i);
					//printf("(%d, %d), (%d, %d)\n",tp.first, tp.second, k.first, k.second);
					if(tp.first + i >= n)
					{
						wynik += n - i;
						break;
					} 
					if(tp.first <= k.first) 
					{
						//puts("!");
						a = k.second;
						wynik += tp.first;
						i += k.first - 1;
					}
					else
					{
						//puts("/");
						wynik += n - i;
						break;
					}
		//			printf("%d, %d ;;;;;", i, n);
				}
			}
			printf("Case #%d: %d\n", li, wynik);
		}
		vek.clear();
	}
	return 0;
}
