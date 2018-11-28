#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstddef>

using namespace std;

int main()
{
	//Nombre de tests
	int T(0);
	cin >> T;
	
	int Smax(0);
	string chaine;
	vector<int> shyness;
	int persoAAjoute(0);
	int persoAAjouteTotal(0);
	int nbPersoLeve(0);
	int diff(0);
	//Boucle sur les tests
	for (int i = 1; i <= T; i++)
	{
		cin >> Smax;
		cin >> chaine;
		shyness.clear();
		
		for (int j = 0; j < (int) chaine.size(); j++)
		{
			shyness.push_back(chaine[j] - '0');
		}

		nbPersoLeve = 0;
		persoAAjouteTotal = 0;
		//On parcoure le tableau
		for (int j = 0; j <= Smax; j++)
		{
			if (nbPersoLeve < j)
			{
				persoAAjoute = 0;
				diff = j - nbPersoLeve;
				persoAAjoute = diff / 9;
				if (diff % 9 > 0)
				{
					persoAAjoute++;
				}
				nbPersoLeve += shyness[j] + persoAAjoute;
				persoAAjouteTotal += persoAAjoute;
			}
			else
			{
				nbPersoLeve += shyness[j];
			}
			
		}


		//nbrPersonneDeboutManquant = nbrPersonneTotal - nbrPersonneLeve;
		std::cout << "Case #" << i << ": " << persoAAjouteTotal <<endl;
	}
}