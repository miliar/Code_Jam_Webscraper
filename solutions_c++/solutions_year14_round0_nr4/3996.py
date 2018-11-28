#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

double Naomi[1009];
double Ken[1009];

int visiNaomi[1009];
int visiKen[1009];

int n;

int getIndexMinValue(double x)
{
	int index = n - 1;
	while (index >= 0)
	{
		if (!visiKen[index] && x < Ken[index])
			return index;
		index--;
	}
	return -1;
}

int getTopIndex()
{
	int index = 0;
	while (visiKen[index++]);
	return index - 1;
}

int getBottomIndex()
{
	int index = n - 1;
	while (visiKen[index--]);
	return index + 1;
}

int main()
{
	int k;	

	cin >> k;
	for (int caso = 1; caso <= k; caso++)
	{
		cin >> n;
		
		memset(visiNaomi, 0, sizeof visiNaomi);
		memset(visiKen, 0, sizeof visiKen);

		for (int i = 0; i < n; i++)
			cin >> Naomi[i];
		for (int i = 0; i < n; i++)
			cin >> Ken[i];

		sort(Naomi, Naomi + n);
		sort(Ken, Ken + n);
		reverse(Naomi, Naomi + n);
		reverse(Ken, Ken + n);

		int winNaomiWar = 0;
		for (int i = 0; i < n; i++)
		{
			int a = getIndexMinValue(Naomi[i]);
			if (a != -1)
			{
				// Si hay un elemento ligeramente mayor a la tirada de Naomi
				visiKen[a] = 1; // Lo quitamos
			}
			else
			{
				// Tomamos el de menor tamano, en fin que ya mamamos
				a = getIndexMinValue(0.0);
				visiKen[a] = 1;
				winNaomiWar++; // Aumentamos uno a Naomi
			}

		}

		int winNaomiDWar = 0;
		memset(visiNaomi, 0, sizeof visiNaomi);
		memset(visiKen, 0, sizeof visiKen);

		for (int i = n - 1; i >= 0; i--)
		{
			int index = getBottomIndex();
			if (Ken[index] > Naomi[i])
			{
				// Hay que popear el mayor de Ken
				index = getTopIndex();
				visiKen[index] = 1;
			}
			else
			{
				// Hay que popear el menor
				visiKen[index] = 1;
				winNaomiDWar++;
			}
		}

		printf("Case #%d: %d %d\n", caso, winNaomiDWar, winNaomiWar);
	}
	return 0;
}