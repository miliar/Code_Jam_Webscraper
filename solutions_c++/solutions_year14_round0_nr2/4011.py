#include<iostream>
#include <iomanip>
#include<cstdio>
#include<vector>
#include<algorithm>
#define REP(I,N) for(int I = 0; I < N; ++I)
#define REPN(I,N) for(int I = 1; I <= N; ++I)
using namespace std;
typedef vector<int> VI;

int main()
{
	long double kosztLevelu, zyskZaPoziom, wygrana, _teraz, _naNastepnym, _kosztyUpgradow;
	long double aktualnyPrzyrost;
	int testy;
	
	cin>>testy;
	REPN(i, testy)
	{
		cin>>kosztLevelu>>zyskZaPoziom>>wygrana;
		aktualnyPrzyrost = 2.0;
		
		_teraz = wygrana/2.0;
		_kosztyUpgradow = kosztLevelu/2.0;
		_naNastepnym = (_kosztyUpgradow + (wygrana/(zyskZaPoziom+2.0)));
		
		while(_naNastepnym < _teraz)
		{
			aktualnyPrzyrost += zyskZaPoziom;
			
			_teraz = _naNastepnym;
			_kosztyUpgradow += (kosztLevelu/aktualnyPrzyrost);
			_naNastepnym = _kosztyUpgradow + (wygrana/(aktualnyPrzyrost+zyskZaPoziom));
		}
		
		cout<<"Case #"<<i<<": "<<setprecision(7)<<fixed<<_teraz<<"\n";
	}
}
