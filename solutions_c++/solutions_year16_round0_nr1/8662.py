#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	int originalNumber;
	vector<int> digitCount;
	for(int a = 0;a<10;a++)
	{
		digitCount.push_back(0);
	}
	for(int caso = 1; caso<=T;caso++)
	{
		for(int a = 0;a<10;a++)
		{
			digitCount.at(a) = 0;
		}
		cin>>originalNumber;
		bool encontrado = false;
		long long multiplicador = 1;
		long long numeroActual = originalNumber;
		if(originalNumber != 0)
		{
			while(!encontrado)
			{
				numeroActual = originalNumber * multiplicador;
				string numero =to_string(numeroActual);
			
				for(long long letra = 0;letra<numero.size();letra++)
				{
					if(digitCount.at(numero[letra]-48) == 0)
					{
						digitCount.at(numero[letra]-48)=1;
					}
				}

				//Veo si encontre todos los digitos
				bool encontre0 = false;
				for(int x = 0;x<10;x++)
				{
					if(digitCount[x] == 0)
					{
						encontre0 = true;
					}
				}
				if(encontre0 == false)
				{
					encontrado = true;
				}
				multiplicador++;

			}
			cout << "Case #" << caso << ": " << numeroActual << endl;
		}else{
			cout << "Case #" << caso << ": " << "INSOMNIA" << endl;
		}
	}

	return 0;
}