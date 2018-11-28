using namespace std;
#include <iostream>
#include <fstream>
#include <math.h>
#include <string>

int main(){
	int ncasos, j, N, last, lista[10], cont, div, aux;
	bool hayneg = true;

	fstream infile("prueba.in");
	ofstream outfile("solu.out");
	infile >> ncasos;
	for (int i = 0; i < ncasos; i++)
	{
		infile >> N;
			cont = 1;
			if (N == 0)
				outfile << "Case #" << i + 1 << ": INSOMNIA" << endl;
			else
			{
				for (int x = 0; x < 10; x++){
					lista[x] = -1; //inicializo el vector de numeros
				}
				hayneg = true;
				while (hayneg)
				{
					last = N*cont;
					aux = last;
					//separamos en digitos
					while (aux >= 10)
					{
						div = aux % 10;
						aux = aux / 10;
						lista[div] = 1;
					}
					div = aux % 10;
					aux = aux / 10;
					lista[div] = 1;

					j = 0;
					hayneg = false;
					while (j < 10 && !hayneg)
					{
						if (lista[j] == -1) hayneg = true;
						j++;
					}
					if (!hayneg)
						outfile << "Case #" << i + 1 << ": " << last << endl;
					cont++;
				}
			}

	}
	infile.close();
	outfile.close();
	return 0;
}