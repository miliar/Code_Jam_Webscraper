#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <stdlib.h>
#include <gmp.h>

using namespace std;

int main()
{
    //string const FichierEntree;
	//cin >> FichierEntree;
    string const FichierEntree("./D-small-practice.in");
    //string const FichierEntree("./input_D.txt");
    string const FichierSortie("./output.txt");
	ifstream Input(FichierEntree.c_str());
	ofstream Output;
	Output.open(FichierSortie.c_str());//, ios::app);

	if(Input)  //On teste si tout est OK
	{
		unsigned long int Ki, ci, S;

		int nbT;
        Input >> nbT;
        for (int i=1; i<=nbT; i++)
        {
        
            Input >> Ki;
            Input >> ci;
            Input >> S;
            cout <<i<<" K = "<<Ki<<" c = "<<ci<<" S = "<<S<<endl;
        
            int Nbnet = Ki-(ci-1);
            cout <<"Nbnet = "<<Nbnet<<endl;
            if (ci > Ki)
            {
                ci = Ki;
                Nbnet = 1;
                cout <<"K = "<<Ki<<" c = "<<ci<<" S = "<<S<<", Nbnet = "<<Nbnet<<endl;
            }
            
            Output << "Case #"<<i<<": ";
            
            if (S >= Nbnet)
            {
                mpz_t posbrique;
                mpz_init (posbrique);
                mpz_set_ui (posbrique,1);
                /*FILE* fichier0;
                FILE* fichier1;
                FILE* fichier2;
                FILE* fichier3;*/
                
                for (int j=1; j < ci; j++)
                {
                    cout<<"boucle BI, j ="<<j<<endl;
                    mpz_t temp;
                    mpz_init (temp);
                    mpz_t tempo;
                    mpz_init (tempo);
                    mpz_ui_pow_ui (temp,Ki,j-1);
                    
                    /*fichier0 = fopen("./fichier0.txt", "w+");
                    string toto;
                    mpz_out_str (fichier0, 10, temp);
                    fclose(fichier0);
                    string const Fichier("./fichier0.txt");
                    ifstream Plop(Fichier.c_str());
                    Plop >> toto;
                    Plop.close();
                    cout <<"pow(Ki,"<<j-1<<") = "<<toto<<endl;*/
                    
                    mpz_mul_ui (tempo,temp,ci-j);
                    
                    /*fichier1 = fopen("./fichier1.txt", "w+");
                    mpz_out_str (fichier1, 10, tempo);
                    fclose(fichier1);
                    ifstream Plop1("./fichier1.txt");
                    Plop1 >> toto;
                    Plop1.close();
                    cout <<"ans*(ci-j) = "<<toto<<endl;*/
                    
                    mpz_add (temp, posbrique,tempo);
                    
                    /*fichier2 = fopen("./fichier2.txt", "w+");
                    mpz_out_str (fichier2, 10, temp);
                    fclose(fichier2);
                    ifstream Plop2("./fichier2.txt");
                    Plop2 >> toto;
                    Plop2.close();
                    cout <<"sum = "<<toto<<endl;*/
                    //exit(EXIT_FAILURE);
                    
                    mpz_set (posbrique,temp);
                    
                    mpz_clear (temp);
                    mpz_clear (tempo);
                    
                    
                    //posbrique[0] += (c-j)*pow(K,j-1);
                }
                
                FILE* fichier;
                string toto;
                fichier = fopen("./fichier.txt", "w+");
                mpz_out_str (fichier, 10, posbrique);
                fclose(fichier);
                string const Fichier("./fichier.txt");
                ifstream Plop(Fichier.c_str());
                Plop >> toto;
                
                Output <<toto<<" ";
            
                for (unsigned long int j = 1; j < Nbnet; j++)
                {
                    mpz_add_ui (posbrique, posbrique,1);
                    //posbrique[j] = posbrique[j-1]+1;
                    
                    fichier = fopen("./fichier.txt", "w+");
                    mpz_out_str (fichier, 10, posbrique);
                    fclose(fichier);
                    string const Fichier("./fichier.txt");
                    ifstream Plop(Fichier.c_str());
                    Plop >> toto;
                    
                    Output <<toto<<" ";
                    
                }
                Output<<endl;
                mpz_clear (posbrique);
                //delete [] posbrique;
            }
            else
            {
                cout<<"IMPOSSIBLE"<<endl;
                Output <<"IMPOSSIBLE"<<endl;
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