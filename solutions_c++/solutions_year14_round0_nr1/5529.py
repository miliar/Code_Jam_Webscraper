/*
 * problemA.cpp
 *
 *  Created on: Apr 11, 2014
 *      Author: filipebraida
 */
#include<iostream>

using namespace std;

int main(void)
{
	int test_cases;
	int primeira_pergunta[4][4];
	int segunda_pergunta[4][4];
	int primeira_reposta;
	int segunda_reposta;

	cin >> test_cases;

	for(int n = 0; n < test_cases; n++)
	{
		cin >> primeira_reposta;

		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> primeira_pergunta[i][j];
			}

			cin.get();
		}

		cin >> segunda_reposta;

		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> segunda_pergunta[i][j];
			}

			cin.get();
		}

		bool achei = false;
		bool bad = false;
		int numero;

		for(int i=0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(primeira_pergunta[primeira_reposta - 1][i] == segunda_pergunta[segunda_reposta - 1][j])
				{
					if(!achei)
					{
						achei = true;
						numero = primeira_pergunta[primeira_reposta - 1][i];
					}
					else
					{
						bad = true;
					}
				}

				if(bad)
					break;
			}

				if(bad)
					break;
		}

		if(bad)
			cout << "Case #" << n + 1 << ": Bad magician!" << endl;
		else if(achei)
			cout << "Case #" << n + 1 << ": " << numero << endl;
		else
			cout << "Case #" << n + 1 << ": Volunteer cheated!" << endl;
	}

	return 0;
}
