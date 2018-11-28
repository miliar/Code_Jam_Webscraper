#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void displayGrille(vector<string> grille)
{
	for(int j = 0; j < grille.size(); j++)
	{
		cerr << grille.at(j) << endl;
	}
	
}

void displayGrilles(std::vector<std::vector<string > > grilles)
{
	for(int i = 0; i < grilles.size(); i++)
	{
		displayGrille(grilles.at(i));
		cerr << endl;
	}
}

string solveTicTacToe(std::vector<string > grille)
{
	displayGrille(grille);
	int nbCasesVides = 0;
	//lignes
	for(int i = 0; i < 4; i++)
	{
		int nbO = 0;
		int nbX = 0;
		for(int j = 0; j < 4; j++)
		{
			if(grille.at(i).at(j) == 'O')
			{
				nbO++;
			}
			if(grille.at(i).at(j) == 'X')
			{
				nbX++;
			}
			if(grille.at(i).at(j) == 'T')
			{
				nbX++;
				nbO++;
			}
			if(grille.at(i).at(j) =='.')
			{
				cerr << grille.at(i).at(j) << " vide ?" << endl;
				nbCasesVides++;
			}
		}
		if(nbO > 3)
		{
			cerr << "ligne " << i << " " << grille.at(i) << endl;
			return "O won";
		}
		if(nbX > 3)
		{
			cerr << "ligne " << i << " " << grille.at(i) << endl;
			return "X won";
		}
	}
	
	//colonnes
	for(int i = 0; i < 4; i++)
	{
		int nbO = 0;
		int nbX = 0;
		for(int j = 0; j < 4; j++)
		{
			if(grille.at(j).at(i) == 'O')
			{
				nbO++;
			}
			if(grille.at(j).at(i) == 'X')
			{
				nbX++;
			}
			if(grille.at(j).at(i) == 'T')
			{
				nbX++;
				nbO++;
			}
		}
		if(nbO > 3)
		{
			cerr << "colonne " << i << " " ;
			return "O won";
		}
		if(nbX > 3)
		{
			cerr << "colonne " << i << endl;
			return "X won";
		}
	}
	
	//diagonales
	int nbODiagA = 0;
	int nbXDiagA = 0;
	int nbODiagB = 0;
	int nbXDiagB = 0;
	for(int i = 0; i < 4; i ++)
	{
		if(grille.at(i).at(i) == 'O')
		{
			nbODiagA++;
		}
		if(grille.at(i).at(i) == 'X')
		{
			nbXDiagA++;
		}
		if(grille.at(i).at(3-i) == 'O')
		{
			nbODiagB++;
		}
		if(grille.at(i).at(3-i) == 'X')
		{
			nbXDiagB++;
		}
		if(grille.at(i).at(i) == 'T')
		{
			nbODiagA++;
			nbXDiagA++;
		}
		if(grille.at(i).at(3-i) == 'T')
		{
			nbODiagB++;
			nbXDiagB++;
		}
	}
	if(nbODiagA > 3)
	{
		cerr << "diagA" << endl ;
		return "O won";
	}
	if(nbODiagB > 3)
	{
		cerr << "diagB" << endl;
		return "O won";
	}
	if(nbXDiagA > 3)
	{
		cerr << "diagA" << endl ;
		return "X won";
	}
	if(nbXDiagB > 3)
	{
		cerr << "diagB" << endl;
		return "X won";
	}
	
	//Draw ou jeu
	if(nbCasesVides == 0)
	{
		cerr << "casesVides: " << nbCasesVides << endl;
		return "Draw";
	}
	else
	{
		cerr << "casesVides: " << nbCasesVides << endl;
		return "Game has not completed";
	}
}

std::vector<std::vector<string > > loadFile(string filename)
{
	ifstream fileStream(filename.c_str());
	std::vector<std::vector<string > > result;
	int nbGrilles = 0;
	fileStream >> nbGrilles;
	for(int i = 0; i < nbGrilles; i++)
	{
		std::vector<string > grille;
		for(int j = 0; j < 4; j++)
		{
			string ligne;
//			getline(fileStream, ligne);
			fileStream >> ligne;
			grille.push_back(ligne);//.replace('\n','');
		}
		
		result.push_back(grille);
	}
	return result;
}

int main(int argc, char **argv) {
    
	string inputFile(argv[1]);
	
	std::vector<std::vector<string > > listGrille
= loadFile(inputFile);
//	displayGrilles(listGrille);
	for(int i = 0; i < listGrille.size(); i++ )
	{
		cout << "Case #"<< i+1 << ": " << solveTicTacToe(listGrille.at(i))
<< endl;
	}

    return 0;
}
