#include <iostream>

using namespace std;

int verificar_igualdade (int *, int *);
void imprimir (int *, int *);

int main ()
{
	int i,j,numero_testes,t,resposta_1,resposta_2;
	int elemento;
	int matriz [4][4];
	int possibilidade_2 [4];
	int possibilidades [4];

	cin >> numero_testes;
	for (t = 1; t <= numero_testes; t++)
	{
		cin >> resposta_1;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				cin >> matriz[i][j];
		for (i = 0; i < 4; i++)
			possibilidades[i] = matriz[resposta_1 - 1][i];
		cin >> resposta_2;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				cin >> matriz[i][j];
		for (i = 0; i < 4; i++)
			possibilidade_2[i] = matriz[resposta_2 - 1][i];

		elemento = verificar_igualdade (possibilidade_2,possibilidades);	
		if (elemento == 0)
			cout << "Case #" << t << ": Bad magician!";
		else
			if (elemento == 20)
				cout << "Case #" << t << ": Volunteer cheated!";
			else
				cout << "Case #" << t << ": " << elemento;
		cout << '\n';
	}
	return 0;
}


int verificar_igualdade (int *possibilidade_2, int *possibilidades)
{
	int elemento_existe = false;
	int i,j, resposta;

	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
			if (possibilidades[i] == possibilidade_2[j])
			{
				if (elemento_existe == true)
					return 0;
				elemento_existe = true;
				resposta = possibilidades[i];
			}
	}
	if (elemento_existe == false)
		return 20;
	else
		return resposta;
}
