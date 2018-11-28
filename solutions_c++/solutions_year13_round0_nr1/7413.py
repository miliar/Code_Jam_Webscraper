#include <iostream>
#include <fstream>
using namespace std;

void main()
{
	char matrice[4][4];
	ifstream inputFile;
	ofstream outputFile;
	int i = 1, m = 0, nombreX = 0, nombreO = 0;
	char victoire = 'D';

	inputFile.open("A-large.in");
	outputFile.open("output.txt");

	if(!inputFile.fail() && !outputFile.fail())
	{
		inputFile >> m;
		for(i; i <= m; i++)
		{
			//Rempli la matrice en testant les lignes
			for(int j = 0; j < 4; j++)
			{
				for(int k = 0; k < 4; k++)
				{
					inputFile >> matrice[j][k];
					switch(matrice[j][k])
					{
						case 'X': nombreX++;
							break;
						case 'O': nombreO++;
							break;
						case 'T': nombreX++;
							nombreO++;
							break;
						default: ;
					}
				}
				if(nombreX == 4)
					victoire = 'X';
				if(nombreO == 4)
					victoire = 'O';

				nombreX = 0;
				nombreO = 0;
			}
			
			//Teste les colonnes
			for(int j = 0; j < 4 && victoire == 'D'; j++)
			{
				for(int k = 0; k < 4; k++)
				{
					switch(matrice[k][j])
					{
						case 'X': nombreX++;
							break;
						case 'O': nombreO++;
							break;
						case 'T': nombreX++;
							nombreO++;
							break;
						default: ;
					}
				}
				if(nombreX == 4)
					victoire = 'X';
				if(nombreO == 4)
					victoire = 'O';

				nombreX = 0;
				nombreO = 0;
			}

			//Teste la première diagonale
			for(int j = 0, k = 0; j < 4 && k < 4 && victoire == 'D'; j++, k++)
			{
				switch(matrice[j][k])
				{
					case 'X': nombreX++;
						break;
					case 'O': nombreO++;
						break;
					case 'T': nombreX++;
						nombreO++;
						break;
					default: ;
				}
			}

			if(nombreX == 4)
				victoire = 'X';
			if(nombreO == 4)
				victoire = 'O';

			nombreX = 0;
			nombreO = 0;

			//Teste de la deuxième diagonale
			for(int j = 0, k = 3; j < 4 && k >= 0 && victoire == 'D'; j++, k--)
			{
				switch(matrice[j][k])
				{
					case 'X': nombreX++;
						break;
					case 'O': nombreO++;
						break;
					case 'T': nombreX++;
						nombreO++;
						break;
					default: ;
				}
			}

			if(nombreX == 4)
				victoire = 'X';
			if(nombreO == 4)
				victoire = 'O';

			nombreX = 0;
			nombreO = 0;

			//Teste draw ou incomplet
			for(int j = 0; j < 4 && victoire == 'D'; j++)
			{
				for(int k = 0; k < 4; k++)
				{
					if(matrice[j][k] == '.')
						victoire = 'N';
				}
			}
			
			outputFile << "Case #" << i << ": ";
			if(victoire == 'X')
				outputFile << "X won" << endl;
			else if(victoire == 'O')
				outputFile << "O won" << endl;
			else if(victoire == 'D')
				outputFile << "Draw" << endl;
			else
				outputFile << "Game has not completed" << endl;

			victoire = 'D';
		}
	}

	inputFile.close();
	outputFile.close();
}