#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int T, n, p = 1;

int main() 
{
	cin >> T; 
	while(T--)
	{
		double ken[15], naomi[15];
		int dwar = 0, war = 0;
		cin >> n; 
		for(int i = 0; i < n; i++) cin >> naomi[i];
		for(int i = 0; i < n; i++) cin >> ken[i];
		
		sort(naomi, naomi + n);
		sort(ken, ken + n);

		for(int i = 0; i < n; i++)
		{
			if(ken[n - i - 1] > naomi[n - i - 1])
			{
				swap(naomi[n - i - 1], naomi[0]);
				sort(naomi, naomi + n - i - 1);
			}
		}
		
		for(int i = 0; i < n; i++)
			dwar += (naomi[i] > ken[i]);
		
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				if(ken[j] > naomi[i])
				{
					ken[j] = -1.0;
					war++;
					break;
				}
		
		printf("Case #%d: %d %d\n", p++, dwar, n - war);
	}
	return 0;
}
