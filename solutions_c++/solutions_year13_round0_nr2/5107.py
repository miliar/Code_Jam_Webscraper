#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#include <queue>

using namespace std;

bool check(int **plansza, int u, int v, int a, int b, int h)
{
	bool value = true;
	for(int i = 0; i < a; i++)
		if(plansza[i][v] > h)
			value = false;
	if(value)
		return true;

	value = true;
	for(int i = 0; i < b; i++)
		if(plansza[u][i] > h)
			value = false;
	if(value)
		return true;

	return false;
}

int main()
{
	int t;
	cin >> t;

	for(int s = 0; s < t; s++)
	{
		int a, b;
		cin >> a >> b;
		int **plansza = new int*[a];
		for(int i = 0; i < a; i++)
		{
			plansza[i] = new int[b];
			for(int j = 0; j < b; j++)
				cin >> plansza[i][j];
		}
		
		bool value = true;
		for(int i = 0; i < a; i++)
			for(int j = 0; j < b; j++)
				if(!check(plansza, i, j, a, b, plansza[i][j]))
				{
					value = false;
					break;
				}
		if(value)
			printf("Case #%d: YES\n", s + 1);
		else
			printf("Case #%d: NO\n", s + 1);
		
		for(int j = 0; j < a; j++)
			delete[] plansza[j];
		delete[] plansza;
	}

	return 0;
}