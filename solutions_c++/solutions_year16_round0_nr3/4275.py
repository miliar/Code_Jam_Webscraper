/*************************************
Fichier principal


*************************************/

#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <sstream>
#include <math.h>
#include <iomanip>
using namespace std;





int main()
{
	string fichier_in = "input.txt";
	string fichier_out= "output.txt";
	string string_nb_test;
	string espace;
	int nb_test;
	int i,j;

	int taille;
	int nb;
	int* jamcoin;
	long int num_2;
	int ** final;

	long double res;
	long double num;
	double base;

	int test_jamcoin;
	int test_div;
	int test_base;
	int test_modulo;
	int div;
	int divis[9];
	int marq;
	int sum_marq;
	int z;

	
	ifstream fichier_open(fichier_in.c_str(), ios::in);
	if(fichier_open)
	{
		getline(fichier_open, string_nb_test);
		stringstream convert(string_nb_test);
		convert >> nb_test;
		fichier_open >> taille >> nb;

		fichier_open.close();
	}
	else
		cerr << "Pas de fichier input ! " << endl ;

	jamcoin= (int *) malloc(taille * sizeof(int));
	jamcoin[0]=1;
	jamcoin[taille-1]=1;
	final = new int* [nb];
	for (i=0;i<nb;i++)
		final[i]= new int[taille + 9];

	for (i=0;i<nb;i++)
	{
		for (j=0;j<taille+9;j++)
			final[i][j]=-1;
	}

	z=0;
	while (z<nb)
	{
	test_jamcoin=-1;
	while(test_jamcoin<0)
	{
		for (i=1;i<taille-1;i++)
		{
				jamcoin[i]=rand() % 2;
		}
		if (z>0)
		{
			sum_marq=0;
			for (j=0;j<z;j++)
			{
				marq=-1;
				for (i=1;i<taille-1;i++)
				{
					if (jamcoin[i]!=final[j][i])
					{
						marq=0;
					}
				}
				sum_marq= sum_marq+marq;
			}
			if (sum_marq>-1)
				test_jamcoin=1;
		}
		else
		{
			test_jamcoin=1;
		}
	}

	for (i=0;i<9;i++)
		divis[i]=0;

	base=2;
	test_base=-1;
	while (test_base<0 && base<11)
	{
		res=0;
		for (i=0;i<taille;i++)
		{
			if (jamcoin[i]>0)
			{
				num=pow(base,taille-i-1);
				res= res + num;
			}
		}
		num_2= sqrt(res);
		test_div=-1;
		div=2;
		while (test_div<0 && div<num_2)
		{
			test_modulo = fmod(res,div);
			if (test_modulo < 1)
				test_div=1;
			div++;
		}
		j=base-2;
		divis[j]=div-1;
		if (test_div<0) //pas de div trouve
			test_base=1; //sortie de boucle
		base++;
	}
	if (test_base<0)
	{
		for (i=0;i<taille;i++)
		{
			final[z][i]=jamcoin[i];
		}
		for (i=0;i<9;i++)
			final[z][taille+i]=divis[i];
		z++;
	}
	}

	ofstream fichier_write(fichier_out.c_str(), ios::out | ios::trunc);
	if(fichier_write)
	{
			fichier_write << "Case #1: " << endl ;
			for (z=0;z<nb;z++)
			{
				for (i=0;i<taille;i++)
				{
					fichier_write << final[z][i] ; 
				}
				for (i=0;i<9;i++)
				{
					fichier_write << " " << final[z][taille+i] ;
				}
				fichier_write << endl ;
			}
		fichier_write.close();
	}
	else
		cerr << "Impossible de creer le fichier output ! " << endl ;
	
	return 0 ;
}

