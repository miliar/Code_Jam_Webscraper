#include <iostream>
#include <string>
#include <fstream>

void RemplirTableau(long long int number, int arrayN[10])
{
	//long long int modulo = 10;
	while (number != 0)
	{
		++arrayN[number % 10];
		number /= 10;
	}
}

int main()
{
	std::ifstream input("A-small-attempt0.in");
	std::ofstream output("output.txt");

	unsigned int nbCases;
	input >> nbCases;

	for (unsigned int i = 1; i <= nbCases; ++i)
	{
		long long int N;
		int arrayN[10] = {};
		input >> N;
		if (N == 0)
		{
			output << "Case #" << i << ": INSOMNIA" << std::endl;
		}
		else
		{
			bool estRempli = false;
			unsigned int nbTry = 1;
			long long int nombre;
			while (!estRempli)
			{
				nombre = N * nbTry;
				RemplirTableau(nombre, arrayN);
				for (unsigned int j = 0; j < 10; ++j)
				{
					if (arrayN[j] == 0)
					{
						j = 11;
					}
					else
					{
						if (j == 9)
						{
							estRempli = true;
						}
					}
				}
				++nbTry;
			}
			output << "Case #" << i << ": " << nombre << std::endl;
		}
	}
	return 0;
}