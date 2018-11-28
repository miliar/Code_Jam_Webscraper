#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
using namespace std;

string EliminarNumero(string texto, string numero)
{
	bool letraEliminada = false;
	for(int i = 0; i<numero.size();i++)
	{
		letraEliminada = false;
		for(int j = 0;j<texto.size();j++)
		{
			if(numero.at(i) == texto.at(j))
			{
				if(letraEliminada == false)
				{
					texto.at(j) = ' ';
					letraEliminada = true;
				}
			}
		}
	}
	return texto;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	for(int t = 1;t<= T; t++)
	{
		vector<int> NumerosDelTelefono;
		string PalabraIngresada = "";
		cin>>PalabraIngresada;
	

		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'Z')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"ZERO");
			
				NumerosDelTelefono.push_back(0);
			}
		}
		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'W')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"TWO");
			
				NumerosDelTelefono.push_back(2);
			}
		}
		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'G')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"EIGHT");
		
				NumerosDelTelefono.push_back(8);
			}
		}
		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'H')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"THREE");
				NumerosDelTelefono.push_back(3);
		
			}
		}
		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'U')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"FOUR");
				NumerosDelTelefono.push_back(4);
			
			}
		}
		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'F')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"FIVE");
				NumerosDelTelefono.push_back(5);
		
			}
		}
		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'V')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"SEVEN");
				NumerosDelTelefono.push_back(7);
		
			}
		}
		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'X')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"SIX");
				NumerosDelTelefono.push_back(6);
			
			}
		}
		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'O')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"ONE");
				NumerosDelTelefono.push_back(1);
		
			}
		}
		for(int k = 0;k<PalabraIngresada.size();k++)
		{
			if(PalabraIngresada.at(k) == 'I')
			{
				PalabraIngresada = EliminarNumero(PalabraIngresada,"NINE");
				NumerosDelTelefono.push_back(9);
				
			}
		}
		
		for(int x = 0;x<NumerosDelTelefono.size();x++)
		{
			for(int y = 0;y<NumerosDelTelefono.size()-1;y++)
			{
				if(NumerosDelTelefono.at(y)>NumerosDelTelefono.at(y+1))
				{
					int aux;
					aux = NumerosDelTelefono.at(y);
					NumerosDelTelefono.at(y) = NumerosDelTelefono.at(y+1);
					NumerosDelTelefono.at(y+1) = aux;
				}
			}
		}
		
		
		cout << "Case #" << t << ": ";
		for(int z = 0;z<NumerosDelTelefono.size();z++)
		{
			cout << NumerosDelTelefono.at(z);
		}
		cout << "" << endl;

	}
	return 0;
}