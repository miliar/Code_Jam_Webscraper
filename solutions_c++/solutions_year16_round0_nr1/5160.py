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
	int *N;
	string ligne;


	ifstream fichier_open(fichier_in.c_str(), ios::in);
	if(fichier_open)
	{
		getline(fichier_open, string_nb_test);
		cout << "Nombre de tests= " << string_nb_test << endl ;
		stringstream convert(string_nb_test);
		convert >> nb_test;
		N = (int *) malloc(nb_test * sizeof(int));
		for (j=0;j<nb_test;j++)
		{
			getline(fichier_open, ligne);
			stringstream convert(ligne);
			convert >> N[j];
		}
		fichier_open.close();
	}
	else
		cerr << "Pas de fichier input ! " << endl ;

	int t[10];
	int number;
	int sum, max;
	int* res;
	res = (int*) malloc(nb_test * sizeof(int));
	for (i=0;i<nb_test;i++)
		res[i]=-1;


	for (j=0;j<nb_test;j++)
	{
		for (i=0;i<10;i++)
		{
			t[i]=-1;
		}
		sum=0;
		max=1;
		while (sum < 45 && max < 100)
		{
			sum=0;
			number=max*N[j];
			while (number>9)
			{
				i= number%10 ;
				t[i]=i;
				number= (number-i)/10;
			}
			t[number]=number;
			for (i=0;i<10;i++)
				sum=sum+t[i];
			if (sum > 44)
				res[j]=max*N[j];
			max++;
		}
	}

	ofstream fichier_write(fichier_out.c_str(), ios::out | ios::trunc);
	if(fichier_write)
	{
		for (i=1;i<(nb_test+1);i++)
		{
			if (res[i-1]<0)
			{
				fichier_write << "Case #" << i << ": INSOMNIA" << endl ;
			}
			else
			{
				fichier_write << "Case #" << i << ": " << res[i-1] << endl ;
			}
		}
		fichier_write.close();
	}
	else
		cerr << "Impossible de creer le fichier output ! " << endl ;
	
	//system("pause");
	return 0 ;
}

