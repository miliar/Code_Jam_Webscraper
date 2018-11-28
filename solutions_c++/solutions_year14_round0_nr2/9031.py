#include <iostream>

using namespace std;

int main(void)
{
	int t;
	double c, f, x;
	double total,time;
	double prod;

	//Lendo a quantidade de casos de teste
	cin >> t;

	//Lendo e calculando cada caso de teste
	for(int qtd=1 ; (qtd<=t) ; qtd++)
	{
		total=0;
		cin >> c >> f >> x;
		prod = 2;

		while( (x/prod) > ( (c/prod) + (x/(f+prod)) ) )
		{
			time=c/prod;
			total+=time;
			prod+=f;
		}

		total+= (x/prod);

		cout.precision(7);
		cout << fixed << "Case #" << qtd << ": "<< total << endl;

	}
	return 0;
}
