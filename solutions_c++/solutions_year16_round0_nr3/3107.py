#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <stdlib.h>

using namespace std;

int main()
{
    //string const FichierEntree;
	//cin >> FichierEntree;
    string const FichierEntree("./C-small-practice.in");
    string const FichierSortie("./output.txt");
	ifstream Input(FichierEntree.c_str());
	ofstream Output;
	Output.open(FichierSortie.c_str());//, ios::app);

	if(Input)  //On teste si tout est OK
	{
		int N, J;

		int nbT;
        Input >> nbT;
        
        Input >> N;
        Input >> J;
        
        int* nombre = new int[N];
        nombre[0] = 1;
        nombre[N-1] = 1;
        
        for (int i = 1; i<N-1; i++)
        {
            nombre[i] = 0;
        }
        int* diviseurs = new int[9];
        
        
        Output << "Case #1: "<<endl;
        int it = 0;
        while (it<J)
        {
            bool jamcoin = false;
            int j=0;
            while (!jamcoin)
            {
                j++;
                cout<<"nombre = ";
                for (int i=N-1; i>=0; i--)
                {
                    cout << nombre[i];
                }
                cout<<endl;
                for (int base = 2; base<=10;base++)
                {
                    cout<<"****base = "<<base<<endl;
                    long long int nb = 0;
                    for (int i = 0; i<N; i++)
                    {
                        nb += nombre[i]*pow(base,i);
                    }
                    cout<<"nb = "<<nb<<endl;
                    if (nb % 2 == 0)
                    {
                        jamcoin = true;
                        diviseurs[base-2] = 2;
                        cout<<"paire "<<endl;
                    }
                    else
                    {
                        jamcoin = false;
                        int limite = sqrt(nb) + 1;
                        cout<<"limite = "<<limite<<endl;
                        for (int i = 3 ; i < limite; i+=2)
                        {
                            if (nb % i == 0)
                            {
                                jamcoin = true;
                                diviseurs[base-2] = i;
                                cout<<"i = "<<i<<endl;
                                if (nb-nb/i*i >0)
                                {
                                    cout<<"PROBLEME"<<endl;
                                    exit(EXIT_FAILURE);
                                }
                                i = limite;
                            }
                        }
                        if (!jamcoin)
                        {
                            cout<<"jamcoin = "<<jamcoin<<endl;
                            jamcoin = false;
                            nombre[1] += 1;
                            for (int i=1; i<N-2; i++)
                            {
                                if (nombre[i] > 1)
                                {
                                    nombre[i]=0;
                                    nombre[i+1]+=1;
                                }
                            }
                            base = 10;
                        }
                    }
                }
            }
            if (jamcoin)
            {
                for (int i=N-1; i>=0; i--)
                {
                    Output << nombre[i];
                }
                for (int i=0; i<9; i++)
                {
                    Output << " "<<diviseurs[i];
                }
                Output<<endl;
                it++;
            }
            
            nombre[1] += 1;
            for (int i=1; i<N-2; i++)
            {
                if (nombre[i] > 1)
                {
                    nombre[i]=0;
                    nombre[i+1]+=1;
                }
            }
            cout<<endl;
            
            
        }
		Output.close();
	}
	else
	{
		cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
	}
    return 0;
}