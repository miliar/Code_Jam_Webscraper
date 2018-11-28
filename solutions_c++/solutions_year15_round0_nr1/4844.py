#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
using namespace std;

int main(){

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int cantidad_casos;
	cin>> cantidad_casos;
	

	for(int i = 1; i<=cantidad_casos;i++)
	{
		int max_shines;
		cin>> max_shines;
		string valores; //Los espectadores con su valor de shines
		cin >> valores;

		vector<int> vec_valores;
		for (int x = 0;x < valores.size();x++)
		{
			vec_valores.push_back(valores[x] - '0');
			
		}
		//Hasta aca funciona
		
		int cantidad_necesito = 0;
		int cant_demas = 0;
		for(int j=0;j<vec_valores.size();j++)
		{
			if(vec_valores.at(j)>1)
			{
				cant_demas = cant_demas + vec_valores.at(j) - 1;
			}
			else if(vec_valores.at(j)==0)
			{
				cant_demas = cant_demas - 1;
			}
			if(cant_demas <0)
			{
				cantidad_necesito++;
				cant_demas = 0;
			}
		}
		cout << "Case #" << i << ": " << cantidad_necesito <<  endl;



	}

	return 0;
}