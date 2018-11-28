#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <algorithm>

using namespace std;

int main()
{
    //string const FichierEntree;
	//cin >> FichierEntree;
    string const FichierEntree("./A-small-practice.in");
    string const FichierSortie("./output.txt");
	ifstream Input(FichierEntree.c_str());
	ofstream Output;
	Output.open(FichierSortie.c_str());//, ios::app);

	if(Input)  //On teste si tout est OK
	{
		int a, b, c;

		int nbT;
		Input >> nbT;

		for (int i=1; i<=nbT; i++)
		{
			int N;
            Input >> N;
            
            int currentN = N;
            if (N != 0)
            {
                bool* chiffres = new bool[10];
                for (int j=0;j<10;j++)
                {
                    chiffres[j] = false;
                }
            
                bool iterateur = false;
                int j=1;
                while (!iterateur )
                {
                    currentN = N*j;
                    //cout<<"currentN = "<<currentN<<endl;
                    int nbcomp = floor(log10(currentN));
                    //cout<<"nbcomp = "<<nbcomp<<endl;
                    int temp = currentN;
                    for (int k = nbcomp; k >= 0; k--)
                    {
                        int chiffre = temp / pow(10,k);
                        temp -= chiffre * pow(10,k);
                        //temp = currentN*pow(10,k)-temp;
                        //cout<<"temp = "<<temp<<endl;
                        //temp /= pow(10,k);
                        //cout<<"chiffre = "<<chiffre<<endl;
                        chiffres[chiffre] = true;
                    }
                    iterateur = chiffres[0];
                    for (int k=0;k<10;k++)
                        iterateur &= chiffres[k];
                    j++;
                }
                Output << "Case #" << i<<": "<<currentN<<endl;
            }
            else
            {
                
                Output << "Case #" << i<<": INSOMNIA"<<endl;
            }
		}

		Output.close();
	}
	else
	{
		cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
	}
    return 0;
}