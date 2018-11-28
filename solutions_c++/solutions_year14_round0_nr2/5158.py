#include <iostream>
#include <iomanip> 

using namespace std;

int main ()
{
	int testes, i;
	double velocidade, custo, extra, numero_maximo;
	double tempo_sem_compra, tempo_com_fazenda;;
	double tempo;

	cin >> testes;
	for (i = 1; i <= testes; i++)
	{
		velocidade = 2;
		cin >> custo >> extra >> numero_maximo;
		while (1)
		{
			tempo_sem_compra = numero_maximo / velocidade;
			tempo_com_fazenda = (custo / velocidade) + (numero_maximo /(velocidade + extra));
			if (tempo_sem_compra < tempo_com_fazenda)
			{
				tempo += tempo_sem_compra;
				break;
			}
			else
			{
				tempo += custo / velocidade;
				velocidade += extra;
			}
		}
		cout << "Case #" << i << ": " << setiosflags (ios::fixed) << setprecision (7) << tempo;
		cout << '\n';
		tempo = 0;
	}
	return 0;
}
