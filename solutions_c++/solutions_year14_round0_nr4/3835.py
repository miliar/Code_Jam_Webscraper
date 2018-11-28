#include<iostream>
#include<vector>
#define REPN(I,N) for(int I = 1; I <= N; ++I)
using namespace std;

int main()
{
	vector<long double> listaNaomi, listaNaomi2, listaKena, listaKena2;
	long double tmp;
	int ileTestow, ileKlockow, wynik, wynik2;

	cin>>ileTestow;
	REPN(i, ileTestow)
	{
		wynik = 0;
		wynik2 = 0;

		cin>>ileKlockow;
		REPN(j, ileKlockow) 
		{
			cin>>tmp;
			listaNaomi.push_back(tmp);
			listaNaomi2.push_back(tmp);
		}
		sort(listaNaomi.begin(), listaNaomi.end());
		sort(listaNaomi2.begin(), listaNaomi2.end());

		REPN(j, ileKlockow) 
		{
			cin>>tmp;
			listaKena.push_back(tmp);
			listaKena2.push_back(tmp);
		}
		sort(listaKena.begin(), listaKena.end());
		sort(listaKena2.begin(), listaKena2.end());

		while(!listaNaomi.empty())
		{
			if(listaNaomi[0] < listaKena[0])
			{
				listaNaomi.erase(listaNaomi.begin());
				listaKena.pop_back();
			}
			else
			{
				listaNaomi.erase(listaNaomi.begin());
				listaKena.erase(listaKena.begin());
				++wynik;
			}
		}

		while(!listaNaomi2.empty())
		{
			if(listaNaomi2[0] > listaKena2[0])
			{
				listaNaomi2.pop_back();
				listaKena2.erase(listaKena2.begin());
				++wynik2;
			}
			else
			{
				listaNaomi2.erase(listaNaomi2.begin());
				listaKena2.erase(listaKena2.begin());
			}
		}

		cout<<"Case #"<<i<<": "<<wynik<<" "<<wynik2<<"\n";
	}
}