// CodeJam 2013
// Autor: Benjamín de la Fuente Ranea

#include <stdarg.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>

#define FILE_INPUT	"B-large"

using namespace std;


void main()
{
	freopen(FILE_INPUT".in", "r", stdin);
	freopen(FILE_INPUT".out", "w", stdout);

	int numCases;
	scanf("%d\n", &numCases);

	for (int i = 1; i <= numCases; ++i)
	{
		int nRows, nCols;
		scanf("%d %d\n", &nRows, &nCols);

		int table[100][100];
		for (int r = 0; r < nRows; ++r)
		{
			for (int c = 0; c < nCols; ++c)
			{
				scanf("%d", &table[r][c]);
				if (c < nCols-1)
					scanf(" ");
			}
			scanf("\n");
		}

		bool res = nRows == 1 || nCols == 1;
		if (!res)
		{
			res = true;
			for (int r = 0; r < nRows && res; ++r)
			{
				for (int c = 0; c < nCols && res; ++c)
				{
					const int curVal = table[r][c];

					// Debe haber un camino horizontal o vertical con numeros menores o iguales q curVal
					for (int x = 0; x < nCols && res; ++x)
					{
						if (table[r][x] > curVal)
							res = false;
					}
					if (!res)
					{
						// Vesmo si en la otra direccion hay camino
						res = true;
						for (int y = 0; y < nRows && res; ++y)
						{
							if (table[y][c] > curVal)
								res = false;
						}
					}
				}
			}
		}

		printf("Case #%d: %s\n", i, res ? "YES" : "NO");
	}
}
