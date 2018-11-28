#include <iostream>
#include <fstream>
#include <string>

/*
#define fluxIn cin //cin ou fichier
#define fluxOut cout //cout ou f_out
#define FILE 0 //1 si utilisation fichiers, 0 sinon
*/

#define fluxIn fichier //cin ou fichier
#define fluxOut f_out //cout ou f_out
#define FILE 1 //1 si utilisation fichiers, 0 sinon

using namespace std;
typedef char Grille[4][4];
typedef int Sum[4];
bool winner = false;
ofstream f_out;


int nbOf(char *str, char c, bool *hasT)
{
	int nb = 0;
	*hasT = false;
	for(int i = 0; i < (int)strlen(str); i++)
	{
		if(str[i] == c) nb++;
		else if(str[i] == 'T') *hasT = true;
	}

	return nb;
}

bool Test(char *str, char c)
{
	bool hasT, res = false;
	int nb = nbOf(str, c, &hasT);
	if(nb == 4 || (nb == 3 && hasT)) res = true;
	
	return res;
}

bool Analyse(char *str, int i)
{
	bool win = false;
	if(Test(str,'X')) { fluxOut << "Case #" << i+1 << ": X won"; win = true; }
	else if(Test(str,'O')) { fluxOut << "Case #" << i+1 << ": O won";  win = true; }

	if(win) 
	{
		winner = true;
	}

	return win;
}

int main(int argc, char* argv[])
{
	int T = 0;

	Grille* tab;
	char mot[5] = {0};


	ifstream fichier("input.in", ios::in);  // on ouvre en lecture
	string ligne;


    fluxIn >> T;  // on met dans "contenu" la ligne
	tab = new Grille[T];
		
	for(int i = 0; i < T; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				fluxIn >> tab[i][j][k];
			}
			if(FILE) getline(fluxIn, ligne);
		}
		if(FILE) getline(fluxIn, ligne);
		else cout << endl;
	}
    if(FILE) fichier.close();


	f_out.open("output.out", ios::out | ios::trunc);  // ouverture en écriture avec effacement du fichier ouvert

	int i = 0, j = 0, k = 0;

	for(i = 0; i < T; i++)
	{
		winner = false;
		bool draw = true;


		//Lignes
		for(j = 0; j < 4; j++)
		{
			for(k = 0; k < 4; k++)
			{
				mot[k] = tab[i][j][k];
				if(mot[k] == '.') draw = false;
			}
			if(Analyse(mot, i)) break;
		}

		//Colonnes
		if(!winner)
		{
			for(j = 0; j < 4; j++)
			{
				for(k = 0; k < 4; k++)
				{
					mot[k] = tab[i][k][j];
				}
				if(Analyse(mot, i)) break;
			}
		}

		

		//Diagonales
		if(!winner)
		{
			for(j = 0; j < 4; j++)
			{
				mot[j] = tab[i][j][j];
			}
			Analyse(mot, i);
		}

		if(!winner)
		{
			for(j = 0; j < 4; j++)
			{
				mot[j] = tab[i][3-j][j];
			}
			Analyse(mot, i);
		}

		if(!winner)
		{
			if(draw) fluxOut << "Case #" << i+1 << ": Draw";
			else fluxOut << "Case #" << i+1 << ": Game has not completed";
		}

		fluxOut << endl;
	}

	f_out.close();
	delete[] tab;
	
	return 0;
}
