#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	long double temp, tempox, tempoaux, c, f, x, passo;
	int qtd;

	cin >> qtd;

	for(int k = 1; k <= qtd; k++)
	{
		passo = 2.0;
		temp  = 0.0;

		cin >> c >> f >> x;

		while(1)
		{
			tempoaux = c / passo;
			tempoaux += x / (passo + f);

			tempox = x / passo;
			
			if(tempox <= tempoaux)
			{
				temp += tempox;
				break;
			}

			temp += (c / passo);
			passo += f;
		}

		cout << "Case #" << k << ": " << setprecision(7) << fixed << temp << "\n";
	}

	return 0;
}