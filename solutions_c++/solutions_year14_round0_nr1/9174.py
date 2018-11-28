#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	int casos;
	cin >> casos;
	for (int caso = 1; caso <= casos; caso++)
	{
		int fila[3];
		bool conjunto[3][17];
		memset(conjunto, false, sizeof(conjunto));

		for (int n = 1; n <= 2; n++)
		{
			int fila;
			cin >> fila;
			for (int i = 1; i<=4; i++)
				for (int j=1; j<=4; j++)
				{
					int x;
					cin >> x;
					if (i == fila) conjunto[n][x] = true;
				}
		}

		int soluciones = 0;
		int solucion;
		for (int i = 1; i <= 16; i++)
		{
 			if (conjunto[1][i] && conjunto[2][i])
			{
				soluciones++;
				solucion = i;
			}
		}

		cout << "Case #" << caso << ": ";
		if (!soluciones) 
			cout << "Volunteer cheated!" << endl;
		else if (soluciones == 1)
			cout << solucion << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}