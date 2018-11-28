/*************************************
Fichier principal


*************************************/

#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <sstream>
using namespace std;





int main()
{
	string fichier_in = "input.txt";
	string fichier_out= "output.txt";
	string string_nb_test;
	string espace;
	int nb_test;
	int i,j;
	int* nb_char;
	int* nb_change;
	int* last;
	string ligne;


	ifstream fichier_open(fichier_in.c_str(), ios::in);
	if(fichier_open)
	{
		getline(fichier_open, string_nb_test);
		stringstream convert(string_nb_test);
		convert >> nb_test;
		nb_char = (int *) malloc(nb_test * sizeof(int));
		nb_change= (int *) malloc(nb_test * sizeof(int));
		last= (int *) malloc(nb_test * sizeof(int));
		for (j=0;j<nb_test;j++)
		{
			nb_change[j]=0;
			last[j]=0;
			getline(fichier_open, ligne);
			nb_char[j]= strlen(ligne.c_str());
			for (i=0;i<nb_char[j]-1;i++)
			{
				if (ligne[i] != ligne[i+1])
				{
					nb_change[j]++;
				}
			}
			if (ligne[nb_char[j]-1]=='-')
				{
					last[j]=-1;
				}
		}
		fichier_open.close();
	}
	else
		cerr << "Pas de fichier input ! " << endl ;

	ofstream fichier_write(fichier_out.c_str(), ios::out | ios::trunc);
	if(fichier_write)
	{
		for (i=1;i<(nb_test+1);i++)
		{
			if (last[i-1]<0)
			{
				fichier_write << "Case #" << i << ": " << nb_change[i-1]+1 << endl ;
			}
			else
			{
				fichier_write << "Case #" << i << ": " << nb_change[i-1] << endl ;
			}
		}
		fichier_write.close();
	}
	else
		cerr << "Impossible de creer le fichier output ! " << endl ;
	
	//system("pause");
	return 0 ;
}

